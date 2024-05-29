#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Martin Rødvand (@rodvand)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_service_template
short_description: Create, update or delete service templates within NetBox
description:
  - Creates, updates or removes service templates from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Martin Rødvand (@rodvand)
requirements:
  - pynetbox
version_added: '3.10.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    required: true
    description:
      - Defines the service template configuration
    suboptions:
      name:
        description:
          - The name of the service template
        required: true
        type: str
      ports:
        description:
          - The ports attached to the service template
        required: false
        type: list
        elements: int
      protocol:
        description:
          - The protocol
        choices:
          - tcp
          - udp
          - sctp
        required: false
        type: str
      description:
        description:
          - Description of the service template
        required: false
        type: str
      comments:
        description:
          - Comments
        required: false
        type: str
      tags:
        description:
          - Any tags that the service template may need to be associated with
        required: false
        type: list
        elements: raw
      custom_fields:
        description:
          - Must exist in NetBox and in key/value format
        required: false
        type: dict
"""

EXAMPLES = r"""
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: false

  tasks:
    - name: Create service template within NetBox with only required information
      netbox.netbox.netbox_service_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: SSH
          ports:
            - 22
          protocol: tcp
        state: present

    - name: Update service template with other fields
      netbox.netbox.netbox_service_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: SSH
          ports:
            - 22
          protocol: tcp
          description: SSH service template
        state: present

    - name: Delete service template within netbox
      netbox.netbox.netbox_service_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: SSH
        state: absent
"""

RETURN = r"""
service_template:
  description: Serialized object as created or already existent within NetBox
  returned: success (when I(state=present))
  type: dict
msg:
  description: Message indicating failure or info about what has been achieved
  returned: always
  type: str
"""

from ansible_collections.netbox.netbox.plugins.module_utils.netbox_utils import (
    NetboxAnsibleModule,
    NETBOX_ARG_SPEC,
)
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_ipam import (
    NetboxIpamModule,
    NB_SERVICE_TEMPLATES,
)
from copy import deepcopy


def main():
    """
    Main entry point for module execution
    """
    argument_spec = deepcopy(NETBOX_ARG_SPEC)
    argument_spec.update(
        dict(
            data=dict(
                type="dict",
                required=True,
                options=dict(
                    name=dict(required=True, type="str"),
                    ports=dict(required=False, type="list", elements="int"),
                    protocol=dict(
                        required=False,
                        choices=[
                            "tcp",
                            "udp",
                            "sctp",
                        ],
                        type="str",
                    ),
                    description=dict(required=False, type="str"),
                    comments=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["name", "ports", "protocol"]),
        ("state", "absent", ["name"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_service_template = NetboxIpamModule(module, NB_SERVICE_TEMPLATES)
    netbox_service_template.run()


if __name__ == "__main__":  # pragma: no cover
    main()

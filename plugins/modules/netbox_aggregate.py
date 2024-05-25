#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Mikhail Yohman (@FragmentedPacket) <mikhail.yohman@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_aggregate
short_description: Creates or removes aggregates from NetBox
description:
  - Creates or removes aggregates from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Mikhail Yohman (@FragmentedPacket)
requirements:
  - pynetbox
version_added: '0.1.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    description:
      - "Defines the aggregate configuration"
    type: dict
    suboptions:
      prefix:
        description:
          - "The aggregate prefix"
        required: true
        type: raw
      rir:
        description:
          - "The RIR the aggregate will be assigned to"
        required: false
        type: raw
      date_added:
        description:
          - "Date added, format: YYYY-MM-DD"
        required: false
        type: str
      description:
        description:
          - "The description of the aggregate"
        required: false
        type: str
      comments:
        description:
          - Comments that may include additional information in regards to the aggregate
        required: false
        type: str
        version_added: "3.10.0"
      tenant:
        description:
          - Tenant the aggregate will be assigned to.
        required: false
        type: raw
        version_added: "3.12.0"
      tags:
        description:
          - "Any tags that the aggregate may need to be associated with"
        required: false
        type: list
        elements: raw
      custom_fields:
        description:
          - "must exist in NetBox"
        required: false
        type: dict
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox aggregate module"
  connection: local
  hosts: localhost
  gather_facts: false

  tasks:
    - name: Create aggregate within NetBox with only required information
      netbox.netbox.netbox_aggregate:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          prefix: 192.168.0.0/16
          rir: Test RIR
        state: present

    - name: Create aggregate with several specified options
      netbox.netbox.netbox_aggregate:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          prefix: 192.168.0.0/16
          rir: Test RIR
          date_added: 1989-01-18
          description: Test description
          tags:
            - Schnozzberry
        state: present

    - name: Delete aggregate within netbox
      netbox.netbox.netbox_aggregate:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          prefix: 192.168.0.0/16
        state: absent
"""

RETURN = r"""
aggregate:
  description: Serialized object as created or already existent within NetBox
  returned: on creation
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
    NB_AGGREGATES,
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
                    prefix=dict(required=True, type="raw"),
                    rir=dict(required=False, type="raw"),
                    date_added=dict(required=False, type="str"),
                    description=dict(required=False, type="str"),
                    comments=dict(required=False, type="str"),
                    tenant=dict(required=False, type="raw"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [("state", "present", ["prefix"]), ("state", "absent", ["prefix"])]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_aggregate = NetboxIpamModule(module, NB_AGGREGATES)
    netbox_aggregate.run()


if __name__ == "__main__":  # pragma: no cover
    main()

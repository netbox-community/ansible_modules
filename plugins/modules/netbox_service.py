#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Kulakov Ilya  (@TawR1024)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_service
short_description: Creates or removes service from NetBox
description:
  - Creates or removes service from NetBox
notes:
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Kulakov Ilya (@TawR1024)
requirements:
  - pynetbox
version_added: '0.1.5'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the service configuration
    suboptions:
      device:
        description:
          - Specifies on which device the service is running
        required: false
        type: raw
      virtual_machine:
        description:
          - Specifies on which virtual machine the service is running
        required: false
        type: raw
      name:
        description:
          - Name of the region to be created
        required: true
        type: str
      port:
        description:
          - Specifies which port used by service
        required: false
        type: int
      ports:
        description:
          - Specifies which ports used by service (NetBox 2.10 and newer)
        type: list
        elements: int
      protocol:
        description:
          - Specifies which protocol used by service
        required: true
        type: raw
      ipaddresses:
        description:
          - Specifies which IPaddresses to associate with service.
        required: false
        type: raw
      description:
        description:
          - Service description
        required: false
        type: str
      comments:
        description:
          - Comments that may include additional information in regards to the service
        required: false
        type: str
        version_added: "3.10.0"
      tags:
        description:
          - What tags to add/update
        required: false
        type: list
        elements: raw
      custom_fields:
        description:
          - Must exist in NetBox and in key/value format
        required: false
        type: dict
    required: true
"""

EXAMPLES = r"""
- name: "Create netbox service"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create service
      netbox.netbox.netbox_service:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: Test666
          name: node-exporter
          port: 9100
          protocol: TCP
          ipaddresses:
            - address: 127.0.0.1
          tags:
            - prometheus
        state: present

    - name: Delete service
      netbox.netbox.netbox_service:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: Test666
          name: node-exporter
          port: 9100
          protocol: TCP
        state: absent
"""

from ansible_collections.netbox.netbox.plugins.module_utils.netbox_utils import (
    NetboxAnsibleModule,
    NETBOX_ARG_SPEC,
)
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_ipam import (
    NetboxIpamModule,
    NB_SERVICES,
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
                    device=dict(required=False, type="raw"),
                    virtual_machine=dict(required=False, type="raw"),
                    name=dict(required=True, type="str"),
                    port=dict(required=False, type="int"),
                    ports=dict(required=False, type="list", elements="int"),
                    protocol=dict(required=True, type="raw"),
                    ipaddresses=dict(required=False, type="raw"),
                    description=dict(required=False, type="str"),
                    comments=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["name"]),
        ("state", "absent", ["name"]),
    ]
    mutually_exclusive = [("port", "ports")]
    required_one_of = [["device", "virtual_machine"], ["port", "ports"]]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=required_if,
        required_one_of=required_one_of,
        mutually_exclusive=mutually_exclusive,
    )

    netbox_service = NetboxIpamModule(module, NB_SERVICES)

    # Change port to ports for 2.10+ and convert to a list with the single integer
    if netbox_service.data.get("port") and netbox_service._version_check_greater(
        netbox_service.version, "2.10", greater_or_equal=True
    ):
        netbox_service.data["ports"] = [netbox_service.data.pop("port")]

    # Run the normal run() method
    netbox_service.run()


if __name__ == "__main__":  # pragma: no cover
    main()

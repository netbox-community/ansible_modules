#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2020, Kulakov Ilya  (@TawR1024)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: netbox_cables
short_description: Creates or removes service from Netbox
description:
  - Creates or removes cables from Netbox
notes:
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Kulakov Ilya (@TawR1024)
requirements:
  - pynetbox
version_added: '0.1.7'
options:
  netbox_url:
    description:
      - URL of the Netbox instance resolvable by Ansible control host
    required: true
    type: str
  netbox_token:
    description:
      - The token created within Netbox to authorize API access
    required: true
    type: str
  data:
    description:
      - Defines the service configuration
    suboptions:
      device:
        description:
          - Specifies on which device the service is running
        type: raw
      virtual_machine:
        description:
        type: raw
      port:
        description:
          - Specifies which port used by service
        type: int
      protocol:
        description:
          - Specifies which protocol used by service
        type: int
        choices:
            - 6 TCP
            - 17 UDP
      ipaddress:
        description:
          - VRF that prefix is associated with
        type: str
      description:
        description:
          - Service description
        type: str
      custom_fields:
        description:
          - Must exist in Netbox and in key/value format
        type: dict
    required: true
  state:
    description:
      - Use C(present) or C(absent) for adding or removing.
    choices: [ absent, present ]
    default: present
  validate_certs:
    description:
      - If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
    default: "yes"
    type: bool
"""

EXAMPLES = r"""
- name: "Create cable"
  connection: local
  hosts: localhost
  collections:
   - netbox_community.ansible_modules
  gather_facts: False
  tasks:
    - name: Create vrf within Netbox with only required information
      netbox_cables:
        netbox_url: 
        netbox_token: 
        data:
          termination_a_name: comp1
          termination_a_port: eth0
          termination_b_name: sw01
          termination_b_port: GE 0/0/13
        state: present
"""

from ansible_collections.netbox_community.ansible_modules.plugins.module_utils.netbox_utils import (
    NetboxAnsibleModule,
    NETBOX_ARG_SPEC,
)
from ansible_collections.netbox_community.ansible_modules.plugins.module_utils.netbox_cables import (
    NetboxCablesModule,
    NB_CABLES,
)


def main():
    """
    Main entry point for module execution
    """
    argument_spec = NETBOX_ARG_SPEC
    argument_spec.update(
        dict(
            data=dict(
                type="dict",
                required=True,
                options=dict(
                    id=dict(required=False, type="int"),
                    termination_a_type=dict(required=False, type="str"),
                    termination_a_name=dict(required=True, type="str"), #device name
                    termination_a_port=dict(required=True, type="str"), #device port
                    termination_b_type=dict(required=False, type="str"),
                    termination_b_name=dict(required=True, type="str"), #device name
                    termination_b_port=dict(required=True, type="str"), #device port
                    type=dict(required=False, type="int"),
                    status=dict(required=False, type="bool"),
                    label=dict(required=False, type="str"),
                    color=dict(required=False, type="str"),
                    length=dict(required=False, type="int"),
                    length_unit=dict(required=False, type="raw"),
                ),
            ),
        )
    )

    required_if = [
        (
            "state",
            "present",
            [
                "termination_a_name",
                "termination_a_port",
                "termination_b_name",
                "termination_b_port",
            ],
        ),
        ("state", "absent", ["id"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_cable = NetboxCablesModule(module, NB_CABLES)
    netbox_cable.run()


if __name__ == "__main__":
    main()

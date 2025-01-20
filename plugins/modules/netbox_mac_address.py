#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2025, Martin Rødvand (@rodvand) <martin@rodvand.net>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_mac_address
short_description: Create, update or delete MAC addresses within NetBox
description:
  - Creates, updates or removes MAC addresses from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Martin Rødvand (@rodvand)
requirements:
  - pynetbox
version_added: "3.21.0"
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the MAC address configuration
    suboptions:
      mac_address:
        description:
          - The MAC address
        required: true
        type: str
      assigned_object:
        description:
          - The object to assign this MAC address to
        required: false
        type: dict
      description:
        description:
          - Description of the MAC address
        required: false
        type: str
      comments:
        description:
          - Comments for the MAC address
        required: false
        type: str
      tags:
        description:
          - Any tags that the MAC address may need to be associated with
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
- name: "Test NetBox MAC address module"
  connection: local
  hosts: localhost
  gather_facts: false

  tasks:
    - name: Create MAC address within NetBox with only required information
      netbox.netbox.netbox_mac_address:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          mac_address: "00:11:22:33:44:55"
        state: present

    - name: Create MAC address with interface assignment
      netbox.netbox.netbox_mac_address:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          mac_address: "AA:BB:CC:DD:EE:FF"
          assigned_object:
            device: Test Nexus One
            name: Ethernet1/1
          description: "MAC address for eth1/1"
          tags:
            - Network
        state: present

    - name: Delete MAC address within netbox
      netbox.netbox.netbox_mac_address:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          mac_address: "00:11:22:33:44:55"
        state: absent
"""

RETURN = r"""
mac_address:
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_dcim import (
    NetboxDcimModule,
    NB_MAC_ADDRESSES,
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
                    mac_address=dict(required=True, type="str"),
                    assigned_object=dict(required=False, type="dict"),
                    description=dict(required=False, type="str"),
                    comments=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["mac_address"]),
        ("state", "absent", ["mac_address"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=required_if,
    )

    netbox_mac_address = NetboxDcimModule(module, NB_MAC_ADDRESSES)
    netbox_mac_address.run()


if __name__ == "__main__":  # pragma: no cover
    main()

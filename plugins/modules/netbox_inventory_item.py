#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Mikhail Yohman (@FragmentedPacket)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_inventory_item
short_description: Creates or removes inventory items from NetBox
description:
  - Creates or removes inventory items from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Mikhail Yohman (@FragmentedPacket)
requirements:
  - pynetbox
version_added: "0.1.0"
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the inventory item configuration
    suboptions:
      device:
        description:
          - Name of the device the inventory item belongs to
        required: false
        type: raw
      name:
        description:
          - Name of the inventory item to be created
        required: true
        type: str
      parent_inventory_item:
        description:
          - The parent inventory item the inventory item will be associated with
        required: false
        type: raw     
        version_added: "3.5.0"   
      label:
        description:
          - The physical label of the inventory item
        required: false
        type: str
        version_added: "3.4.0"
      manufacturer:
        description:
          - The manufacturer of the inventory item
        required: false
        type: raw
      part_id:
        description:
          - The part ID of the inventory item
        required: false
        type: str
      serial:
        description:
          - The serial number of the inventory item
        required: false
        type: str
      asset_tag:
        description:
          - The asset tag of the inventory item
        required: false
        type: str
      description:
        description:
          - The description of the inventory item
        required: false
        type: str
      discovered:
        description:
          - Set the discovery flag for the inventory item
        required: false
        default: false
        type: bool
      tags:
        description:
          - Any tags that the device may need to be associated with
        required: false
        type: list
        elements: raw
      custom_fields:
        description:
          - must exist in Netbox
        required: false
        type: dict
        version_added: "3.4.0"
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox inventory_item module"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create inventory item within NetBox with only required information
      netbox.netbox.netbox_inventory_item:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: test100
          name: "10G-SFP+"
        state: present

    - name: Update inventory item
      netbox.netbox.netbox_inventory_item:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: test100
          name: "10G-SFP+"
          manufacturer: "Cisco"
          part_id: "10G-SFP+"
          serial: "1234"
          asset_tag: "1234"
          description: "New SFP"
        state: present
        
    - name: Create inventory item with parent
      netbox.netbox.netbox_inventory_item:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          parent_inventory_item:
            name: "Line Card 1"
            device: test100
          name: "10G-SFP+"
          device: test100
        state: present

    - name: Delete inventory item within netbox
      netbox.netbox.netbox_inventory_item:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: test100
          name: "10G-SFP+"
        state: absent
"""

RETURN = r"""
inventory_item:
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_dcim import (
    NetboxDcimModule,
    NB_INVENTORY_ITEMS,
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
                    name=dict(required=True, type="str"),
                    parent_inventory_item=dict(required=False, type="raw"),
                    label=dict(required=False, type="str"),
                    manufacturer=dict(required=False, type="raw"),
                    part_id=dict(required=False, type="str"),
                    serial=dict(required=False, type="str"),
                    asset_tag=dict(required=False, type="str"),
                    description=dict(required=False, type="str"),
                    discovered=dict(required=False, type="bool", default=False),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["device", "name"]),
        ("state", "absent", ["device", "name"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_inventory_item = NetboxDcimModule(module, NB_INVENTORY_ITEMS)
    netbox_inventory_item.run()


if __name__ == "__main__":  # pragma: no cover
    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Martin Rødvand (@rodvand) <martin@rodvand.net>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_module_type
short_description: Create, update or delete module types within NetBox
description:
  - Creates, updates or removes module types from NetBox
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
    description:
      - Defines the device type configuration
    suboptions:
      manufacturer:
        description:
          - The manufacturer of the module type
        required: false
        type: raw
      model:
        description:
          - The model of the module type
        required: true
        type: raw      
      part_number:
        description:
          - The part number of the module type
        required: false
        type: str      
      weight:
        description:
          - The weight of the device type
        required: false
        type: float        
      weight_unit:
        description:
          - The weight unit
        choices:
          - kg
          - g
          - lb
          - oz
        required: false
        type: str
        version_added: "3.10.0" 
      comments:
        description:
          - Comments that may include additional information in regards to the module type
        required: false
        type: str
      tags:
        description:
          - Any tags that the module type may need to be associated with
        required: false
        type: list
        elements: raw
      custom_fields:
        description:
          - must exist in NetBox
        required: false
        type: dict
    required: true
    type: dict
"""

EXAMPLES = r"""
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create module type within NetBox with only required information
      netbox.netbox.netbox_module_type:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:          
          model: ws-test-3750
          manufacturer: Test Manufacturer
        state: present

    - name: Create module type within NetBox
      netbox.netbox.netbox_module_type:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:          
          model: ws-test-3750
          manufacturer: Test Manufacturer
          part_number: ws-3750g-v2          
        state: present

    - name: Delete module type within netbox
      netbox.netbox.netbox_module_type:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          model: ws-test-3750
        state: absent
"""

RETURN = r"""
module_type:
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
    NB_MODULE_TYPES,
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
                    manufacturer=dict(required=False, type="raw"),
                    model=dict(required=True, type="raw"),
                    part_number=dict(required=False, type="str"),
                    weight=dict(required=False, type="float"),
                    weight_unit=dict(
                        required=False,
                        type="str",
                        choices=[
                            "kg",
                            "g",
                            "lb",
                            "oz",
                        ],
                    ),
                    comments=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["model", "manufacturer"]),
        ("state", "absent", ["model"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_device_type = NetboxDcimModule(module, NB_MODULE_TYPES)
    netbox_device_type.run()


if __name__ == "__main__":  # pragma: no cover
    main()

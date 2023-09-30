#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2023, Jeff Groom (@jgroom33) <jgroom@ciena.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_module_bay
short_description: Create, update or delete module bay within NetBox
description:
  - Creates, updates or removes module bay from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Jeff Groom (@jgroom33)
requirements:
  - pynetbox
version_added: '3.13.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    description:
      - Defines the module bay configuration
    suboptions:
      device:
        description:
          - The device of the module bay
        required: true
        type: raw
      name:
        description:
          - The model of the module type
        required: true
        type: raw
      position:
        description:
          - The position of the module bay
        required: true
        type: string
      tags:
        description:
          - Any tags that the module bay may need to be associated with
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
    - name: Create module bay within NetBox with only required information
      netbox.netbox.netbox_module_bay:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: ws-test-3750
          name: ws-test-3750-slot-0
          position: 0
          manufacturer: Test Manufacturer
        state: present

    - name: Delete module bay within netbox
      netbox.netbox.netbox_module_bay:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: ws-test-3750-slot-0
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
    NB_MODULE_BAYS,
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
                    device=dict(required=True, type="raw"),
                    name=dict(required=True, type="raw"),
                    position=dict(required=True, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["device", "name", "position"]),
        ("state", "absent", ["name"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_module_bay = NetboxDcimModule(module, NB_MODULE_BAYS)
    netbox_module_bay.run()


if __name__ == "__main__":  # pragma: no cover
    main()

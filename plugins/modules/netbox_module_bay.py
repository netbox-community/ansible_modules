#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2023, Erwan TONNERRE (@etonnerre) <erwan.tonnerre@thalesgroup.com>
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
  - Erwan TONNERRE (@etonnerre)
requirements:
  - pynetbox
version_added: '3.18.0'
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
          - The model of the module bay
        required: true
        type: raw
      label:
        description:
          - The label of the module bay
        required: false
        type: str
      position:
        description:
          - The position of the module bay
        required: true
        type: str
      description:
        description:
          - The description of the module bay
        required: false
        type: str
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
          device: C9300-DEMO
          name: C9300-DEMO-SLOT-0
          position: 0
        state: present

    - name: Delete module bay within netbox
      netbox.netbox.netbox_module_bay:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: C9300-DEMO-SLOT-0
        state: absent
"""

RETURN = r"""
module_bay:
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
                    label=dict(required=False, type="str"),
                    position=dict(required=True, type="str"),
                    description=dict(required=False, type="str"),
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

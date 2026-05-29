#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2026, Jens Meißner <meissner@b1-systems.de>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_module_bay_template
short_description: Create, update or delete module bay templates within NetBox
description:
  - Creates, updates or removes module bay templates in NetBox
notes:
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Jens Meißner (@heptalium)
requirements:
  - pynetbox
version_added: '3.24.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    description:
      - Defines the module bay template configuration
    suboptions:
      device_type:
        description:
          - The device type of the module bay template
        required: true
        type: raw
      name:
        description:
          - The name of the module bay template
        required: true
        type: str
      label:
        description:
          - The label of the module bay template
        required: false
        type: str
      position:
        description:
          - The position of the module bay template
        required: false
        type: str
      description:
        description:
          - The description of the module bay template
        required: false
        type: str
    required: true
    type: dict
"""

EXAMPLES = r"""
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: false

  tasks:
    - name: Create module bay template within NetBox with only required information
      netbox.netbox.netbox_module_bay_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device_type: Dell PowerEdge R660xs
          name: PSU-1
        state: present

    - name: Delete module bay template within NetBox
      netbox.netbox.netbox_module_bay_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device_type: Dell PowerEdge R660xs
          name: PSU-1
        state: absent
"""

RETURN = r"""
module_bay_template:
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
    NB_MODULE_BAY_TEMPLATES,
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
                    device_type=dict(required=True, type="raw"),
                    name=dict(required=True, type="str"),
                    label=dict(required=False, type="str"),
                    position=dict(required=False, type="str"),
                    description=dict(required=False, type="str"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["device_type", "name"]),
        ("state", "absent", ["device_type", "name"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_module_bay_template = NetboxDcimModule(module, NB_MODULE_BAY_TEMPLATES)
    netbox_module_bay_template.run()


if __name__ == "__main__":  # pragma: no cover
    main()

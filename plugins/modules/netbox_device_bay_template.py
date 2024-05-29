#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2020 Nokia
# Licensed under the GNU General Public License v3.0 only
# SPDX-License-Identifier: GPL-3.0-only

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_device_bay_template
short_description: Create, update or delete device bay templates within NetBox
description:
  - Creates, updates or removes device bay templates from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Tobias Groß (@toerb)
requirements:
  - pynetbox
version_added: '0.3.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    description:
      - Defines the device bay template configuration
    suboptions:
      device_type:
        description:
          - The device type the device bay template will be associated to. The device type must be "parent".
        required: true
        type: raw
      name:
        description:
          - The name of the device bay template
        required: true
        type: str
    type: dict
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: false

  tasks:
    - name: Create device bay template within NetBox with only required information
      netbox.netbox.netbox_device_bay_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: device bay template One
          device_type: Device Type One
        state: present

    - name: Delete device bay template within netbox
      netbox.netbox.netbox_device_bay_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: device bay template One
          device_type: Device Type One
        state: absent
"""

RETURN = r"""
device_bay_template:
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
    NB_DEVICE_BAY_TEMPLATES,
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
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["name", "device_type"]),
        ("state", "absent", ["name", "device_type"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_device_bay_template = NetboxDcimModule(module, NB_DEVICE_BAY_TEMPLATES)
    netbox_device_bay_template.run()


if __name__ == "__main__":  # pragma: no cover
    main()

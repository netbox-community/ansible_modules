#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2020 Nokia
# Licensed under the GNU General Public License v3.0 only
# SPDX-License-Identifier: GPL-3.0-only

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_device_interface_template
short_description: Creates or removes interfaces on devices from NetBox
description:
  - Creates or removes interfaces from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Tobias Groß (@toerb)
requirements:
  - pynetbox
version_added: "0.3.0"
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    description:
      - Defines the interface template configuration
    suboptions:
      device_type:
        description:
          - Name of the device the interface template will be associated with (case-sensitive)
        required: true
        type: raw
      name:
        description:
          - Name of the interface template to be created
        required: true
        type: str
      label:
        description:
          - The label of the interface template
        required: false
        type: str
        version_added: '3.21.0'
      type:
        description:
          - |
            Form factor of the interface:
            ex. 1000Base-T (1GE), Virtual, 10GBASE-T (10GE)
            This has to be specified exactly as what is found within UI
        required: true
        type: str
      enabled:
        description:
          - Whether or not the interface template to be created should be enabled
        required: false
        type: bool
        version_added: '3.21.0'
      mgmt_only:
        description:
          - This interface template is used only for out-of-band management
        required: false
        type: bool
      description:
        description:
          - Description of the interface template
        required: false
        type: str
        version_added: '3.21.0'
      poe_mode:
        description:
          - This interface has PoE ability (NetBox release 3.3 and later)
        required: false
        type: raw
        version_added: "3.8.0"
      poe_type:
        description:
          - This interface's power type (NetBox release 3.3 and later)
        required: false
        type: raw
        version_added: "3.8.0"
    required: true
    type: dict
"""

EXAMPLES = r"""
- name: "Test NetBox interface template module"
  connection: local
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Create interface template within NetBox with only required information
      netbox.netbox.netbox_device_interface_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device_type: Arista Test
          name: 10GBASE-T (10GE)
          type: 10gbase-t
        state: present
    - name: Delete interface template within netbox
      netbox.netbox.netbox_device_interface_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device_type: Arista Test
          name: 10GBASE-T (10GE)
          type: 10gbase-t
        state: absent
"""

RETURN = r"""
interface_template:
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
    NB_INTERFACE_TEMPLATES,
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
                    type=dict(
                        required=True,
                        type="str",
                    ),
                    enabled=dict(required=False, type="bool"),
                    mgmt_only=dict(required=False, type="bool"),
                    description=dict(required=False, type="str"),
                    poe_type=dict(required=False, type="raw"),
                    poe_mode=dict(required=False, type="raw"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["device_type", "name", "type"]),
        ("state", "absent", ["device_type", "name", "type"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_device_interface_template = NetboxDcimModule(module, NB_INTERFACE_TEMPLATES)
    netbox_device_interface_template.run()


if __name__ == "__main__":  # pragma: no cover
    main()

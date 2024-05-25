#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2020 Nokia
# Licensed under the GNU General Public License v3.0 only
# SPDX-License-Identifier: GPL-3.0-only

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_console_port
short_description: Create, update or delete console ports within NetBox
description:
  - Creates, updates or removes console ports from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Tobias Groß (@toerb)
requirements:
  - pynetbox
version_added: '0.2.3'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    required: true
    description:
      - Defines the console port configuration
    suboptions:
      device:
        description:
          - The device the console port is attached to
        required: true
        type: raw
      name:
        description:
          - The name of the console port
        required: true
        type: str
      type:
        description:
          - The type of the console port
        choices:
          - de-9
          - db-25
          - rj-11
          - rj-12
          - rj-45
          - mini-din-8
          - usb-a
          - usb-b
          - usb-c
          - usb-mini-a
          - usb-mini-b
          - usb-micro-a
          - usb-micro-b
          - usb-micro-ab
          - other
        required: false
        type: str
      cable:
        description:
          - cable to connect port to.
        required: false
        type: dict
        version_added: "3.9.0"
      custom_fields:
        description:
          - must exist in netbox
        required: false
        type: dict
        version_added: "3.9.0"
      description:
        description:
          - Description of the console port
        required: false
        type: str
      label:
        description:
          - label of the console port
        required: false
        type: str
        version_added: "3.9.0"
      mark_connected:
        description:
          - Treats as if a cable is connected to the port
        required: false
        type: bool
        version_added: "3.9.0"
      module:
        description:
          - module that provides the console port.
        required: false
        type: int
        version_added: "3.9.0"
      speed:
        description:
          - the port speed
        required: false
        type: int
        version_added: "3.9.0"
      tags:
        description:
          - Any tags that the console port may need to be associated with
        required: false
        type: list
        elements: raw
"""

EXAMPLES = r"""
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: false

  tasks:
    - name: Create console port within NetBox with only required information
      netbox.netbox.netbox_console_port:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Console Port
          device: Test Device
        state: present

    - name: Update console port with other fields
      netbox.netbox.netbox_console_port:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Console Port
          device: Test Device
          type: usb-a
          description: console port description
        state: present

    - name: Delete console port within netbox
      netbox.netbox.netbox_console_port:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Console Port
          device: Test Device
        state: absent
"""

RETURN = r"""
console_port:
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
    NB_CONSOLE_PORTS,
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
                    name=dict(required=True, type="str"),
                    type=dict(
                        required=False,
                        choices=[
                            "de-9",
                            "db-25",
                            "rj-11",
                            "rj-12",
                            "rj-45",
                            "mini-din-8",
                            "usb-a",
                            "usb-b",
                            "usb-c",
                            "usb-mini-a",
                            "usb-mini-b",
                            "usb-micro-a",
                            "usb-micro-b",
                            "usb-micro-ab",
                            "other",
                        ],
                        type="str",
                    ),
                    cable=dict(required=False, type="dict"),
                    custom_fields=dict(required=False, type="dict"),
                    description=dict(required=False, type="str"),
                    module=dict(required=False, type="int"),
                    label=dict(required=False, type="str"),
                    mark_connected=dict(required=False, type="bool"),
                    speed=dict(required=False, type="int"),
                    tags=dict(required=False, type="list", elements="raw"),
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

    netbox_console_port = NetboxDcimModule(module, NB_CONSOLE_PORTS)
    netbox_console_port.run()


if __name__ == "__main__":  # pragma: no cover
    main()

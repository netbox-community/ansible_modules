#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2020 Nokia
# Licensed under the GNU General Public License v3.0 only
# SPDX-License-Identifier: GPL-3.0-only

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_power_port_template
short_description: Create, update or delete power port templates within NetBox
description:
  - Creates, updates or removes power port templates from NetBox
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
      - Defines the power port configuration
    suboptions:
      device_type:
        description:
          - The device type the power port is attached to
          - Either I(device_type) or I(module_type) are required
        type: raw
      module_type:
        description:
          - The module type the power port is attached to
          - Either I(device_type) or I(module_type) are required
        type: raw
        version_added: "3.16.0"
      name:
        description:
          - The name of the power port
        required: true
        type: str
      type:
        description:
          - The type of the power port
        choices:
          - iec-60320-c6
          - iec-60320-c8
          - iec-60320-c14
          - iec-60320-c16
          - iec-60320-c20
          - iec-60320-c22
          - iec-60309-p-n-e-4h
          - iec-60309-p-n-e-6h
          - iec-60309-p-n-e-9h
          - iec-60309-2p-e-4h
          - iec-60309-2p-e-6h
          - iec-60309-2p-e-9h
          - iec-60309-3p-e-4h
          - iec-60309-3p-e-6h
          - iec-60309-3p-e-9h
          - iec-60309-3p-n-e-4h
          - iec-60309-3p-n-e-6h
          - iec-60309-3p-n-e-9h
          - iec-60906-1
          - nbr-14136-10a
          - nbr-14136-20a
          - nema-1-15p
          - nema-5-15p
          - nema-5-20p
          - nema-5-30p
          - nema-5-50p
          - nema-6-15p
          - nema-6-20p
          - nema-6-30p
          - nema-6-50p
          - nema-10-30p
          - nema-10-50p
          - nema-14-20p
          - nema-14-30p
          - nema-14-50p
          - nema-14-60p
          - nema-15-15p
          - nema-15-20p
          - nema-15-30p
          - nema-15-50p
          - nema-15-60p
          - nema-l1-15p
          - nema-l5-15p
          - nema-l5-20p
          - nema-l5-30p
          - nema-l5-50p
          - nema-l6-15p
          - nema-l6-20p
          - nema-l6-30p
          - nema-l6-50p
          - nema-l10-30p
          - nema-l14-20p
          - nema-l14-30p
          - nema-l14-50p
          - nema-l14-60p
          - nema-l15-20p
          - nema-l15-30p
          - nema-l15-50p
          - nema-l15-60p
          - nema-l21-20p
          - nema-l21-30p
          - nema-l22-30p
          - cs6361c
          - cs6365c
          - cs8165c
          - cs8265c
          - cs8365c
          - cs8465c
          - ita-c
          - ita-e
          - ita-f
          - ita-ef
          - ita-g
          - ita-h
          - ita-i
          - ita-j
          - ita-k
          - ita-l
          - ita-m
          - ita-n
          - ita-o
          - usb-a
          - usb-b
          - usb-c
          - usb-mini-a
          - usb-mini-b
          - usb-micro-a
          - usb-micro-b
          - usb-micro-ab
          - usb-3-b
          - usb-3-micro-b
          - dc-terminal
          - saf-d-grid
          - neutrik-powercon-20
          - neutrik-powercon-32
          - neutrik-powercon-true1
          - neutrik-powercon-true1-top
          - ubiquiti-smartpower
          - hardwired
          - other
        required: false
        type: str
      allocated_draw:
        description:
          - The allocated draw of the power port in watt
        required: false
        type: int
      maximum_draw:
        description:
          - The maximum permissible draw of the power port in watt
        required: false
        type: int
"""

EXAMPLES = r"""
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: false

  tasks:
    - name: Create power port within NetBox with only required information
      netbox.netbox.netbox_power_port_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Port Template
          device_type: Test Device Type
        state: present

    - name: Create power port for a module type within NetBox
      netbox.netbox.netbox_power_port_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Port Template
          module_type: Test Module Type
          type: iec-60320-c6
          maximum_draw: 750
        state: present

    - name: Update power port with other fields
      netbox.netbox.netbox_power_port_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Port Template
          device_type: Test Device Type
          type: iec-60320-c6
          allocated_draw: 16
          maximum_draw: 80
        state: present

    - name: Delete power port within netbox
      netbox.netbox.netbox_power_port_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Port Template
          device_type: Test Device Type
        state: absent
"""

RETURN = r"""
power_port_template:
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
    NB_POWER_PORT_TEMPLATES,
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
                    device_type=dict(required=False, type="raw"),
                    module_type=dict(required=False, type="raw"),
                    name=dict(required=True, type="str"),
                    type=dict(
                        required=False,
                        choices=[
                            "iec-60320-c6",
                            "iec-60320-c8",
                            "iec-60320-c14",
                            "iec-60320-c16",
                            "iec-60320-c20",
                            "iec-60320-c22",
                            "iec-60309-p-n-e-4h",
                            "iec-60309-p-n-e-6h",
                            "iec-60309-p-n-e-9h",
                            "iec-60309-2p-e-4h",
                            "iec-60309-2p-e-6h",
                            "iec-60309-2p-e-9h",
                            "iec-60309-3p-e-4h",
                            "iec-60309-3p-e-6h",
                            "iec-60309-3p-e-9h",
                            "iec-60309-3p-n-e-4h",
                            "iec-60309-3p-n-e-6h",
                            "iec-60309-3p-n-e-9h",
                            "iec-60906-1",
                            "nbr-14136-10a",
                            "nbr-14136-20a",
                            "nema-1-15p",
                            "nema-5-15p",
                            "nema-5-20p",
                            "nema-5-30p",
                            "nema-5-50p",
                            "nema-6-15p",
                            "nema-6-20p",
                            "nema-6-30p",
                            "nema-6-50p",
                            "nema-10-30p",
                            "nema-10-50p",
                            "nema-14-20p",
                            "nema-14-30p",
                            "nema-14-50p",
                            "nema-14-60p",
                            "nema-15-15p",
                            "nema-15-20p",
                            "nema-15-30p",
                            "nema-15-50p",
                            "nema-15-60p",
                            "nema-l1-15p",
                            "nema-l5-15p",
                            "nema-l5-20p",
                            "nema-l5-30p",
                            "nema-l5-50p",
                            "nema-l6-15p",
                            "nema-l6-20p",
                            "nema-l6-30p",
                            "nema-l6-50p",
                            "nema-l10-30p",
                            "nema-l14-20p",
                            "nema-l14-30p",
                            "nema-l14-50p",
                            "nema-l14-60p",
                            "nema-l15-20p",
                            "nema-l15-30p",
                            "nema-l15-50p",
                            "nema-l15-60p",
                            "nema-l21-20p",
                            "nema-l21-30p",
                            "nema-l22-30p",
                            "cs6361c",
                            "cs6365c",
                            "cs8165c",
                            "cs8265c",
                            "cs8365c",
                            "cs8465c",
                            "ita-c",
                            "ita-e",
                            "ita-f",
                            "ita-ef",
                            "ita-g",
                            "ita-h",
                            "ita-i",
                            "ita-j",
                            "ita-k",
                            "ita-l",
                            "ita-m",
                            "ita-n",
                            "ita-o",
                            "usb-a",
                            "usb-b",
                            "usb-c",
                            "usb-mini-a",
                            "usb-mini-b",
                            "usb-micro-a",
                            "usb-micro-b",
                            "usb-micro-ab",
                            "usb-3-b",
                            "usb-3-micro-b",
                            "dc-terminal",
                            "saf-d-grid",
                            "neutrik-powercon-20",
                            "neutrik-powercon-32",
                            "neutrik-powercon-true1",
                            "neutrik-powercon-true1-top",
                            "ubiquiti-smartpower",
                            "hardwired",
                            "other",
                        ],
                        type="str",
                    ),
                    allocated_draw=dict(required=False, type="int"),
                    maximum_draw=dict(required=False, type="int"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["name"]),
        ("state", "absent", ["name"]),
    ]

    required_one_of = [
        ("device_type", "module_type"),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=required_if,
        required_one_of=required_one_of,
    )

    netbox_power_port_template = NetboxDcimModule(module, NB_POWER_PORT_TEMPLATES)
    netbox_power_port_template.run()


if __name__ == "__main__":  # pragma: no cover
    main()

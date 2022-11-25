#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2020 Nokia
# Licensed under the GNU General Public License v3.0 only
# SPDX-License-Identifier: GPL-3.0-only

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_power_port
short_description: Create, update or delete power ports within NetBox
description:
  - Creates, updates or removes power ports from NetBox
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
      device:
        description:
          - The device the power port is attached to
        required: true
        type: raw
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
          - nema-5-15p
          - nema-5-20p
          - nema-5-30p
          - nema-5-50p
          - nema-6-15p
          - nema-6-20p
          - nema-6-30p
          - nema-6-50p
          - nema-l5-15p
          - nema-l5-20p
          - nema-l5-30p
          - nema-l5-50p
          - nema-l6-20p
          - nema-l6-30p
          - nema-l6-50p
          - nema-l14-20p
          - nema-l14-30p
          - nema-l21-20p
          - nema-l21-30p
          - cs6361c
          - cs6365c
          - cs8165c
          - cs8265c
          - cs8365c
          - cs8465c
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
      description:
        description:
          - Description of the power port
        required: false
        type: str
      tags:
        description:
          - Any tags that the power port may need to be associated with
        required: false
        type: list
        elements: raw
"""

EXAMPLES = r"""
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create power port within NetBox with only required information
      netbox.netbox.netbox_power_port:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Port
          device: Test Device
        state: present

    - name: Update power port with other fields
      netbox.netbox.netbox_power_port:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Port
          device: Test Device
          type: iec-60320-c6
          allocated_draw: 16
          maximum_draw: 80
          description: power port description
        state: present

    - name: Delete power port within netbox
      netbox.netbox.netbox_power_port:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Port
          device: Test Device
        state: absent
"""

RETURN = r"""
power_port:
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
    NB_POWER_PORTS,
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
                            "iec-60320-c6",
                            "iec-60320-c8",
                            "iec-60320-c14",
                            "iec-60320-c16",
                            "iec-60320-c20",
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
                            "nema-5-15p",
                            "nema-5-20p",
                            "nema-5-30p",
                            "nema-5-50p",
                            "nema-6-15p",
                            "nema-6-20p",
                            "nema-6-30p",
                            "nema-6-50p",
                            "nema-l5-15p",
                            "nema-l5-20p",
                            "nema-l5-30p",
                            "nema-l5-50p",
                            "nema-l6-20p",
                            "nema-l6-30p",
                            "nema-l6-50p",
                            "nema-l14-20p",
                            "nema-l14-30p",
                            "nema-l21-20p",
                            "nema-l21-30p",
                            "cs6361c",
                            "cs6365c",
                            "cs8165c",
                            "cs8265c",
                            "cs8365c",
                            "cs8465c",
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
                        ],
                        type="str",
                    ),
                    allocated_draw=dict(required=False, type="int"),
                    maximum_draw=dict(required=False, type="int"),
                    description=dict(required=False, type="str"),
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

    netbox_power_port = NetboxDcimModule(module, NB_POWER_PORTS)
    netbox_power_port.run()


if __name__ == "__main__":  # pragma: no cover
    main()

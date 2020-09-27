#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2020 Nokia
# Licensed under the GNU General Public License v3.0 only
# SPDX-License-Identifier: GPL-3.0-only

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: netbox_power_port_template
short_description: Create, update or delete power port templates within Netbox
description:
  - Creates, updates or removes power port templates from Netbox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Tobias Groß (@toerb)
requirements:
  - pynetbox
version_added: '0.2.3'
options:
  netbox_url:
    description:
      - URL of the Netbox instance resolvable by Ansible control host
    required: true
    type: str
  netbox_token:
    description:
      - The token created within Netbox to authorize API access
    required: true
    type: str
  data:
    type: dict
    required: true
    description:
      - Defines the power port configuration
    suboptions:
      device_type:
        description:
          - The device type the power port is attached to
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
  state:
    description:
      - Use C(present) or C(absent) for adding or removing.
    choices: [ absent, present ]
    default: present
    type: str
  query_params:
    description:
      - This can be used to override the specified values in ALLOWED_QUERY_PARAMS that is defined
      - in plugins/module_utils/netbox_utils.py and provides control to users on what may make
      - an object unique in their environment.
    required: false
    type: list
    elements: str
  validate_certs:
    description:
      - If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
    default: true
    type: raw
"""

EXAMPLES = r"""
- name: "Test Netbox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create power port within Netbox with only required information
      netbox_power_port_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Port Template
          device_type: Test Device Type
        state: present

    - name: Update power port with other fields
      netbox_power_port_template:
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
      netbox_power_port_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Port Template
          device_type: Test Device Type
        state: absent
"""

RETURN = r"""
power_port_template:
  description: Serialized object as created or already existent within Netbox
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
                    device_type=dict(required=True, type="raw"),
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

    netbox_power_port_template = NetboxDcimModule(module, NB_POWER_PORT_TEMPLATES)
    netbox_power_port_template.run()


if __name__ == "__main__":  # pragma: no cover
    main()

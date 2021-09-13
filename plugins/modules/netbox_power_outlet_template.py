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
module: netbox_power_outlet_template
short_description: Create, update or delete power outlet templates within Netbox
description:
  - Creates, updates or removes power outlet templates from Netbox
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
  cert:
    description:
      - Certificate path
    required: false
    type: raw
  data:
    type: dict
    required: true
    description:
      - Defines the power outlet configuration
    suboptions:
      device_type:
        description:
          - The device type the power outlet is attached to
        required: true
        type: raw
      name:
        description:
          - The name of the power outlet
        required: true
        type: str
      type:
        description:
          - The type of the power outlet
        choices:
          - iec-60320-c5
          - iec-60320-c7
          - iec-60320-c13
          - iec-60320-c15
          - iec-60320-c19
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
          - nema-5-15r
          - nema-5-20r
          - nema-5-30r
          - nema-5-50r
          - nema-6-15r
          - nema-6-20r
          - nema-6-30r
          - nema-6-50r
          - nema-l5-15r
          - nema-l5-20r
          - nema-l5-30r
          - nema-l5-50r
          - nema-l6-20r
          - nema-l6-30r
          - nema-l6-50r
          - nema-l14-20r
          - nema-l14-30r
          - nema-l21-20r
          - nema-l21-30r
          - CS6360C
          - CS6364C
          - CS8164C
          - CS8264C
          - CS8364C
          - CS8464C
          - ita-e
          - ita-f
          - ita-g
          - ita-h
          - ita-i
          - ita-j
          - ita-k
          - ita-l
          - ita-m
          - ita-n
          - ita-o
          - hdot-cx
        required: false
        type: str
      power_port_template:
        description:
          - The attached power port template
        required: false
        type: raw
      feed_leg:
        description:
          - The phase, in case of three-phase feed
        choices:
          - A
          - B
          - C
        required: false
        type: str
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
    - name: Create power outlet template within Netbox with only required information
      netbox_power_outlet_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Outlet Template
          device_type: Test Device Type
        state: present

    - name: Update power outlet template with other fields
      netbox_power_outlet_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Outlet Template
          device_type: Test Device Type
          type: iec-60320-c6
          power_port_template: Test Power Port Template
          feed_leg: A
        state: present

    - name: Delete power outlet template within netbox
      netbox_power_outlet_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Outlet Template
          device_type: Test Device Type
        state: absent
"""

RETURN = r"""
power_outlet_template:
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
    NB_POWER_OUTLET_TEMPLATES,
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
                            "iec-60320-c5",
                            "iec-60320-c7",
                            "iec-60320-c13",
                            "iec-60320-c15",
                            "iec-60320-c19",
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
                            "nema-5-15r",
                            "nema-5-20r",
                            "nema-5-30r",
                            "nema-5-50r",
                            "nema-6-15r",
                            "nema-6-20r",
                            "nema-6-30r",
                            "nema-6-50r",
                            "nema-l5-15r",
                            "nema-l5-20r",
                            "nema-l5-30r",
                            "nema-l5-50r",
                            "nema-l6-20r",
                            "nema-l6-30r",
                            "nema-l6-50r",
                            "nema-l14-20r",
                            "nema-l14-30r",
                            "nema-l21-20r",
                            "nema-l21-30r",
                            "CS6360C",
                            "CS6364C",
                            "CS8164C",
                            "CS8264C",
                            "CS8364C",
                            "CS8464C",
                            "ita-e",
                            "ita-f",
                            "ita-g",
                            "ita-h",
                            "ita-i",
                            "ita-j",
                            "ita-k",
                            "ita-l",
                            "ita-m",
                            "ita-n",
                            "ita-o",
                            "hdot-cx",
                        ],
                        type="str",
                    ),
                    power_port_template=dict(required=False, type="raw"),
                    feed_leg=dict(required=False, choices=["A", "B", "C"], type="str"),
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

    netbox_power_outlet_template = NetboxDcimModule(module, NB_POWER_OUTLET_TEMPLATES)
    netbox_power_outlet_template.run()


if __name__ == "__main__":  # pragma: no cover
    main()

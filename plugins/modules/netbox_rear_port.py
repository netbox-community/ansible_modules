#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2020 Nokia
# Licensed under the GNU General Public License v3.0 only
# SPDX-License-Identifier: GPL-3.0-only

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_rear_port
short_description: Create, update or delete rear ports within NetBox
description:
  - Creates, updates or removes rear ports from NetBox
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
      - Defines the rear port configuration
    suboptions:
      device:
        description:
          - The device the rear port is attached to
        required: true
        type: raw
      name:
        description:
          - The name of the rear port
        required: true
        type: str
      type:
        description:
          - The type of the rear port
        choices:
          - 8p8c
          - 110-punch
          - bnc
          - mrj21
          - fc
          - lc
          - lc-apc
          - lsh
          - lsh-apc
          - mpo
          - mtrj
          - sc
          - sc-apc
          - st
        required: true
        type: str
      positions:
        description:
          - The number of front ports which may be mapped to each rear port
        required: false
        type: int
      description:
        description:
          - Description of the rear port
        required: false
        type: str
      label:
        description:
          - Label of the rear port
        required: false
        type: str
        version_added: "3.7.0"
      tags:
        description:
          - Any tags that the rear port may need to be associated with
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
    - name: Create rear port within NetBox with only required information
      netbox.netbox.netbox_rear_port:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Rear Port
          device: Test Device
          type: bnc
        state: present

    - name: Update rear port with other fields
      netbox.netbox.netbox_rear_port:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Rear Port
          device: Test Device
          type: bnc
          positions: 5
          description: rear port description
        state: present

    - name: Delete rear port within netbox
      netbox.netbox.netbox_rear_port:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Rear Port
          device: Test Device
          type: bnc
        state: absent
"""

RETURN = r"""
rear_port:
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
    NB_REAR_PORTS,
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
                        required=True,
                        choices=[
                            "8p8c",
                            "110-punch",
                            "bnc",
                            "mrj21",
                            "fc",
                            "lc",
                            "lc-apc",
                            "lsh",
                            "lsh-apc",
                            "mpo",
                            "mtrj",
                            "sc",
                            "sc-apc",
                            "st",
                        ],
                        type="str",
                    ),
                    positions=dict(required=False, type="int"),
                    description=dict(required=False, type="str"),
                    label=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["device", "name", "type"]),
        ("state", "absent", ["device", "name", "type"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_rear_port = NetboxDcimModule(module, NB_REAR_PORTS)
    netbox_rear_port.run()


if __name__ == "__main__":  # pragma: no cover
    main()

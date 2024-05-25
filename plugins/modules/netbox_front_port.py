#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2020 Nokia
# Licensed under the GNU General Public License v3.0 only
# SPDX-License-Identifier: GPL-3.0-only

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_front_port
short_description: Create, update or delete front ports within NetBox
description:
  - Creates, updates or removes front ports from NetBox
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
      - Defines the front port configuration
    suboptions:
      device:
        description:
          - The device the front port is attached to
        required: true
        type: raw
      name:
        description:
          - The name of the front port
        required: true
        type: str
      type:
        description:
          - The type of the front port
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
      rear_port:
        description:
          - The rear_port the front port is attached to
        required: true
        type: raw
      rear_port_position:
        description:
          - The position of the rear port this front port is connected to
        required: false
        type: int
      description:
        description:
          - Description of the front port
        required: false
        type: str
      label:
        description:
          - Label of the front port
        required: false
        type: str
        version_added: "3.7.0"
      tags:
        description:
          - Any tags that the front port may need to be associated with
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
    - name: Create front port within NetBox with only required information
      netbox.netbox.netbox_front_port:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Front Port
          device: Test Device
          type: bnc
          rear_port: Test Rear Port
        state: present

    - name: Update front port with other fields
      netbox.netbox.netbox_front_port:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Front Port
          device: Test Device
          type: bnc
          rear_port: Test Rear Port
          rear_port_position: 5
          description: front port description
        state: present

    - name: Delete front port within netbox
      netbox.netbox.netbox_front_port:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Front Port
          device: Test Device
          type: bnc
          rear_port: Test Rear Port
        state: absent
"""

RETURN = r"""
front_port:
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
    NB_FRONT_PORTS,
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
                    rear_port=dict(required=True, type="raw"),
                    rear_port_position=dict(required=False, type="int"),
                    description=dict(required=False, type="str"),
                    label=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["device", "name", "type", "rear_port"]),
        ("state", "absent", ["device", "name", "type", "rear_port"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_front_port = NetboxDcimModule(module, NB_FRONT_PORTS)
    netbox_front_port.run()


if __name__ == "__main__":  # pragma: no cover
    main()

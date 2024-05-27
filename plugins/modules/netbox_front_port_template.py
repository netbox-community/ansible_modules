#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2020 Nokia
# Licensed under the GNU General Public License v3.0 only
# SPDX-License-Identifier: GPL-3.0-only

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_front_port_template
short_description: Create, update or delete front port templates within NetBox
description:
  - Creates, updates or removes front port templates from NetBox
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
      - Defines the front port template configuration
    suboptions:
      device_type:
        description:
          - The device type the front port template is attached to
        required: true
        type: raw
      name:
        description:
          - The name of the front port template
        required: true
        type: str
      type:
        description:
          - The type of the front port template
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
        required: false
        type: str
      rear_port_template:
        description:
          - The rear_port_template the front port template is attached to
        required: true
        type: raw
      rear_port_template_position:
        description:
          - The position of the rear port template this front port template is connected to
        required: false
        type: int
      description:
        description:
          - Description of the front port
        required: false
        type: str
        version_added: "3.7.0"
      label:
        description:
          - Label of the front port
        required: false
        type: str
        version_added: "3.7.0"
"""

EXAMPLES = r"""
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: false

  tasks:
    - name: Create front port template within NetBox with only required information
      netbox.netbox.netbox_front_port_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Front Port Template
          device_type: Test Device Type
          type: bnc
          rear_port_template: Test Rear Port Template
        state: present

    - name: Update front port template with other fields
      netbox.netbox.netbox_front_port_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Front Port Template
          device_type: Test Device Type
          type: bnc
          rear_port_template: Test Rear Port Template
          rear_port_template_position: 5
        state: present

    - name: Delete front port template within netbox
      netbox.netbox.netbox_front_port_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Front Port Template
          device_type: Test Device Type
          type: bnc
          rear_port_template: Test Rear Port Template
        state: absent
"""

RETURN = r"""
front_port_template:
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
    NB_FRONT_PORT_TEMPLATES,
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
                    rear_port_template=dict(required=True, type="raw"),
                    rear_port_template_position=dict(required=False, type="int"),
                    description=dict(required=False, type="str"),
                    label=dict(required=False, type="str"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["device_type", "name", "type", "rear_port_template"]),
        ("state", "absent", ["device_type", "name", "type", "rear_port_template"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_front_port_template = NetboxDcimModule(module, NB_FRONT_PORT_TEMPLATES)
    netbox_front_port_template.run()


if __name__ == "__main__":  # pragma: no cover
    main()

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
module: netbox_rear_port_template
short_description: Create, update or delete rear port templates within Netbox
description:
  - Creates, updates or removes rear port templates from Netbox
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
      - Defines the rear port template configuration
    suboptions:
      device_type:
        description:
          - The device type the rear port template is attached to
        required: true
        type: raw
      name:
        description:
          - The name of the rear port template
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
        required: false
        type: str
      positions:
        description:
          - The number of front ports which may be mapped to each rear port
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
    - name: Create rear port template within Netbox with only required information
      netbox_rear_port_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Rear Port Template
          device_type: Test Device Type
          type: bnc
        state: present

    - name: Update rear port template with other fields
      netbox_rear_port_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Rear Port Template
          device_type: Test Device Type
          type: bnc
          positions: 5
        state: present

    - name: Delete rear port template within netbox
      netbox_rear_port_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Rear Port Template
          device_type: Test Device Type
          type: bnc
        state: absent
"""

RETURN = r"""
rear_port_template:
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
    NB_REAR_PORT_TEMPLATES,
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
                    positions=dict(required=False, type="int"),
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

    netbox_rear_port_template = NetboxDcimModule(module, NB_REAR_PORT_TEMPLATES)
    netbox_rear_port_template.run()


if __name__ == "__main__":  # pragma: no cover
    main()

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
module: netbox_device_interface_template
short_description: Creates or removes interfaces on devices from Netbox
description:
  - Creates or removes interfaces from Netbox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Tobias Groß (@toerb)
requirements:
  - pynetbox
version_added: "0.3.0"
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
    description:
      - Defines the prefix configuration
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
      type:
        description:
          - |
            Form factor of the interface:
            ex. 1000Base-T (1GE), Virtual, 10GBASE-T (10GE)
            This has to be specified exactly as what is found within UI
        required: true
        type: str
      mgmt_only:
        description:
          - This interface template is used only for out-of-band management
        required: false
        type: bool
    required: true
    type: dict
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
      - |
        If C(no), SSL certificates will not be validated.
        This should only be used on personally controlled sites using self-signed certificates.
    default: true
    type: raw
"""

EXAMPLES = r"""
- name: "Test Netbox interface template module"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create interface template within Netbox with only required information
      netbox_device_interface_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device_type: Arista Test
          name: 10GBASE-T (10GE)
          type: 10gbase-t
        state: present
    - name: Delete interface template within netbox
      netbox_device_interface_template:
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
  description: Serialized object as created or already existent within Netbox
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
                    type=dict(required=True, type="str",),
                    mgmt_only=dict(required=False, type="bool"),
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

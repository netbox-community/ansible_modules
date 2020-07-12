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
module: netbox_virtual_chassis
short_description: Create, update or delete virtual chassis within Netbox
description:
  - Creates, updates or removes virtual chassis from Netbox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Tobias Groß (@toerb)
requirements:
  - pynetbox
version_added: '0.3.0'
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
      - Defines the virtual chassis configuration
    suboptions:
      master:
        description:
          - The master device the virtual chassis is attached to
        required: true
        type: raw
      domain:
        description:
          - domain of the virtual chassis
        required: false
        type: str
      tags:
        description:
          - Any tags that the virtual chassis may need to be associated with
        required: false
        type: list
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
    - name: Create virtual chassis within Netbox with only required information
      netbox_virtual_chassis:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          master: Test Device
        state: present

    - name: Update virtual chassis with other fields
      netbox_virtual_chassis:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          master: Test Device
          domain: Domain Text
        state: present

    - name: Delete virtual chassis within netbox
      netbox_virtual_chassis:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          master: Test Device
        state: absent
"""

RETURN = r"""
virtual_chassis:
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
    NB_VIRTUAL_CHASSIS,
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
                    master=dict(required=True, type="raw"),
                    domain=dict(required=False, type="str"),
                    tags=dict(required=False, type="list"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["master"]),
        ("state", "absent", ["master"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_virtual_chassis = NetboxDcimModule(module, NB_VIRTUAL_CHASSIS)
    netbox_virtual_chassis.run()


if __name__ == "__main__":  # pragma: no cover
    main()

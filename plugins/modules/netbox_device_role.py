#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Mikhail Yohman (@FragmentedPacket) <mikhail.yohman@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_device_role
short_description: Create, update or delete devices roles within NetBox
description:
  - Creates, updates or removes devices roles from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Mikhail Yohman (@FragmentedPacket)
requirements:
  - pynetbox
version_added: '0.1.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    description:
      - Defines the device role configuration
    suboptions:
      name:
        description:
          - The name of the device role
        required: true
        type: str
      description:
        description:
          - The description of the device role
        required: false
        type: str
      color:
        description:
          - Hexidecimal code for a color, ex. FFFFFF
        required: false
        type: str
      slug:
        description:
          - The slugified version of the name or custom slug.
          - This is auto-generated following NetBox rules if not provided
        required: false
        type: str
      vm_role:
        description:
          - Whether the role is a VM role
        type: bool
      tags:
        description:
          - The tags to add/update
        required: false
        type: list
        elements: raw
        version_added: "3.6.0"
      custom_fields:
        description:
          - Must exist in NetBox
        required: false
        type: dict
        version_added: "3.6.0"
    required: true
    type: dict
"""

EXAMPLES = r"""
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create device role within NetBox with only required information
      netbox_device_role:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test device role
          color: FFFFFF
        state: present

    - name: Delete device role within netbox
      netbox_device_role:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Rack role
        state: absent
"""

RETURN = r"""
device_role:
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
    NB_DEVICE_ROLES,
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
                    name=dict(required=True, type="str"),
                    description=dict(required=False, type="str"),
                    color=dict(required=False, type="str"),
                    slug=dict(required=False, type="str"),
                    vm_role=dict(required=False, type="bool"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [("state", "present", ["name"]), ("state", "absent", ["name"])]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_device_role = NetboxDcimModule(module, NB_DEVICE_ROLES)
    netbox_device_role.run()


if __name__ == "__main__":  # pragma: no cover
    main()

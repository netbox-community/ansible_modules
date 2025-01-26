#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Daniel Chiquito (@dchiquito) <daniel.chiquito@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_permission
short_description: Creates or removes permissions from NetBox
description:
  - Creates or removes permissions from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Daniel Chiquito (@dchiquito)
requirements:
  - pynetbox
version_added: "3.20.0"
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the permission configuration
    suboptions:
      name:
        description:
          - Name of the permission to be created
        required: true
        type: str
      description:
        description:
          - Description of the permission to be created
        required: false
        type: str
      enabled:
        description:
          - Whether or not the permission to be created should be enabled
        required: false
        type: bool
      actions:
        description:
          - The actions of the permission to be created
        required: false
        type: list
        elements: raw
      object_types:
        description:
          - The object types of the permission to be created
        required: false
        type: list
        elements: raw
      constraints:
        description:
          - The constraints of the permission to be created
        required: false
        type: raw
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox module"
  connection: local
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Create permission within NetBox with only required information
      netbox.netbox.netbox_permission:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: My Permission
          actions:
            - view
          object_types: []
        state: present

    - name: Create user which has the permission
      netbox.netbox.netbox_user:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          username: MyUser
          password: MyPassword
          permissions:
            - My Permission
        state: present

    - name: Create a group which has the permission
      netbox.netbox.netbox_user_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: My Group
          permissions:
            - My Permission
        state: absent

    - name: Delete permission within netbox
      netbox.netbox.netbox_permission:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: My Permission
        state: absent

    - name: Create permission with all parameters
      netbox.netbox.netbox_permission:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: My permission
          description: The permission I made
          enabled: false
          actions:
            - view
            - add
            - change
            - delete
            - extreme_administration
          object_types:
            - vpn.tunneltermination
            - wireless.wirelesslan
          constraints:
            id: 1
        state: present
"""

RETURN = r"""
permissions:
  description: Serialized object as created or already existent within NetBox
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_users import (
    NetboxUsersModule,
    NB_PERMISSIONS,
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
                    enabled=dict(required=False, type="bool"),
                    actions=dict(required=False, type="list", elements="raw"),
                    object_types=dict(required=False, type="list", elements="raw"),
                    constraints=dict(required=False, type="raw"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["name", "actions", "object_types"]),
        ("state", "absent", ["name"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_permission = NetboxUsersModule(module, NB_PERMISSIONS)
    netbox_permission.run()


if __name__ == "__main__":  # pragma: no cover
    main()

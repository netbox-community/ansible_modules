#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Daniel Chiquito (@dchiquito) <daniel.chiquito@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_user
short_description: Creates or removes users from NetBox
description:
  - Creates or removes users from NetBox
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
      - Defines the user configuration
    suboptions:
      username:
        description:
          - Username of the user to be created
        required: true
        type: str
      password:
        description:
          - Password of the user to be created. If this is specified, the password field will always be updated.
        required: false
        type: str
      email:
        description:
          - Email of the user to be created
        required: false
        type: str
      first_name:
        description:
          - First name  of the user to be created
        required: false
        type: str
      last_name:
        description:
          - Last name of the user to be created
        required: false
        type: str
      is_staff:
        description:
          - Staff status of the user to be created
        required: false
        type: bool
      is_active:
        description:
          - Active status of the user to be created
        required: false
        type: bool
      groups:
        description:
          - Groups the user to be created should belong to
        required: false
        type: list
        elements: str
      permissions:
        description:
          - Permissions the user to be created should have
        required: false
        type: list
        elements: str
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox module"
  connection: local
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Create user within NetBox with only required information
      netbox.netbox.netbox_user:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          username: MyUser
          password: MyPassword
        state: present

    - name: Update a user's email
      netbox.netbox.netbox_user:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          username: MyUser
          password: my@user.com
        state: present

    - name: Delete user within netbox
      netbox.netbox.netbox_user:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          username: MyUser
        state: absent

    - name: Create user with all parameters
      netbox.netbox.netbox_user:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          username: MyUser2
          password: MyPassword
          email: my@user.com
          first_name: My
          last_name: User
        state: present
"""

RETURN = r"""
user:
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
    NB_USERS,
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
                    username=dict(required=True, type="str"),
                    password=dict(required=False, type="str", no_log=True),
                    email=dict(required=False, type="str"),
                    first_name=dict(required=False, type="str"),
                    last_name=dict(required=False, type="str"),
                    is_active=dict(required=False, type="bool"),
                    is_staff=dict(required=False, type="bool"),
                    groups=dict(required=False, type="list", elements="str"),
                    permissions=dict(required=False, type="list", elements="str"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["username"]),
        ("state", "absent", ["username"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_user = NetboxUsersModule(module, NB_USERS)
    netbox_user.run()


if __name__ == "__main__":  # pragma: no cover
    main()

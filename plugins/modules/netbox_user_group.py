#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Daniel Chiquito (@dchiquito) <daniel.chiquito@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_user_group
short_description: Creates or removes user groups from NetBox
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
      - Defines the user group configuration
    suboptions:
      name:
        description:
          - Name of the user group to be created
        required: true
        type: str
      description:
        description:
          - Description of the user group to be created
        required: false
        type: str
      permissions:
        description:
          - Permissions the user group to be created should have
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
    - name: Create user group within NetBox with only required information
      netbox.netbox.netbox_user_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: My Group
        state: present

    - name: Create user belonging to the group
      netbox.netbox.netbox_user:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          username: MyUser
          password: MyPassword
          groups:
            - My Group
        state: present

    - name: Delete user group within netbox
      netbox.netbox.netbox_user_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: My Group
        state: absent

    - name: Create user group with all parameters
      netbox.netbox.netbox_user_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: My Group
          description: The group I made
        state: present
"""

RETURN = r"""
user_group:
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
    NB_GROUPS,
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
                    permissions=dict(required=False, type="list", elements="str"),
                ),
            ),
        )
    )

    required_if = [("state", "present", ["name"]), ("state", "absent", ["name"])]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_user_group = NetboxUsersModule(module, NB_GROUPS)
    netbox_user_group.run()


if __name__ == "__main__":  # pragma: no cover
    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Daniel Chiquito (@dchiquito) <daniel.chiquito@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_token
short_description: Creates or removes tokens from NetBox
description:
  - Creates or removes tokens from NetBox
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
      - Defines the token configuration
    suboptions:
      key:
        description:
          - Key of the token to be created. Must be exactly 40 characters
        required: true
        type: str
      user:
        description:
          - User the token to be created belongs to
        required: false
        type: str
      description:
        description:
          - The description of the token to be created
        required: false
        type: str
      write_enabled:
        description:
          - Whether or not the token to be created should allow write operations
        required: false
        type: bool
      expires:
        description:
          - When the token to be created should expire
        required: false
        type: str
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox module"
  connection: local
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Create user to own the token
      netbox.netbox.netbox_user:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          username: MyUser
          password: MyPassword
        state: present

    - name: Create token within NetBox with only required information
      netbox.netbox.netbox_token:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          user: TestUser
          key: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        state: present

    - name: Delete token within netbox
      netbox.netbox.netbox_token:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          key: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        state: absent

    - name: Create token with all parameters
      netbox.netbox.netbox_token:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          user: TestUser
          key: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
          description: The test token
          write_enabled: false
          expires: 2024-08-26T14:49:01.345000+00:00
        state: present
"""

RETURN = r"""
token:
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
    NB_TOKENS,
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
                    key=dict(required=True, type="str", no_log=True),
                    user=dict(required=False, type="str"),
                    description=dict(required=False, type="str"),
                    write_enabled=dict(required=False, type="bool"),
                    expires=dict(required=False, type="str"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["key", "user"]),
        ("state", "absent", ["key"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_token = NetboxUsersModule(module, NB_TOKENS)
    netbox_token.run()


if __name__ == "__main__":  # pragma: no cover
    main()

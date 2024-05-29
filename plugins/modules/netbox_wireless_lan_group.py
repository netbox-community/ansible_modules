#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Martin Rødvand (@rodvand)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_wireless_lan_group
short_description: Creates or removes Wireless LAN Groups from NetBox
description:
  - Creates or removes Wireless LAN Groups from NetBox
notes:
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Martin Rødvand (@rodvand)
requirements:
  - pynetbox
version_added: "3.5.0"
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the contact configuration
    suboptions:
      name:
        description:
          - Name of the Wireless LAN Group to be created
        required: true
        type: str
      slug:
        description:
          - The slug of the Wireless LAN Group
        required: false
        type: str
      parent_wireless_lan_group:
        description:
          - The parent Wireless LAN group
        required: false
        type: raw
      description:
        description:
          - Description of the Wireless LAN Group
        required: false
        type: str
      tags:
        description:
          - Any tags that the Wireless LAN Group may need to be associated with
        required: false
        type: list
        elements: raw
      custom_fields:
        description:
          - must exist in NetBox
        required: false
        type: dict
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox module"
  connection: local
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Create Wireless LAN Group within NetBox with only required information
      netbox_wireless_lan_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Wireless LAN Group One
        state: present

    - name: Delete Wireless LAN within netbox
      netbox_wireless_lan_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Wireless LAN Group One
        state: absent

    - name: Create Wireless LAN Group with all parameters
      netbox_wireless_lan_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Wireless LAN Group One
          description: Wireless LAN Group description
          tags:
            - tagA
            - tagB
            - tagC
        state: present
"""

RETURN = r"""
wireless_lan_group:
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_wireless import (
    NetboxWirelessModule,
    NB_WIRELESS_LAN_GROUPS,
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
                    slug=dict(required=False, type="str"),
                    parent_wireless_lan_group=dict(required=False, type="raw"),
                    description=dict(required=False, type="str"),
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

    netbox_wireless_lan_group = NetboxWirelessModule(module, NB_WIRELESS_LAN_GROUPS)
    netbox_wireless_lan_group.run()


if __name__ == "__main__":  # pragma: no cover
    main()

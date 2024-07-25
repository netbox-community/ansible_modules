#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Rich Bibby, NetBox Labs (@richbibby)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_tunnel_group
short_description: Create, update or delete tunnel groups within NetBox
description:
  - Creates, updates or deletes tunnel groups within NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Rich Bibby, NetBox Labs (@richbibby)
requirements:
  - pynetbox
version_added: '3.20.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    required: true
    type: dict
    description:
      - Defines the tunnel group configuration
    suboptions:
      name:
        description:
          - The name of the tunnel group
        required: true
        type: str
      slug:
        description:
          - The slugified version of the name or custom slug.
          - This is auto-generated following NetBox rules if not provided
        required: false
        type: str
      description:
        description:
          - The description of the tunnel group
        required: false
        type: str
      tags:
        description:
          - The tags to add/update
        required: false
        type: list
        elements: raw
      custom_fields:
        description:
          - Must exist in NetBox
        required: false
        type: dict
"""

EXAMPLES = r"""
- name: "Test NetBox Tunnel Group module"
  connection: local
  hosts: localhost
  gather_facts: false

  tasks:
    - name: Create tunnel group within NetBox with only required information
      netbox.netbox.netbox_tunnel_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Tunnel Group
        state: present

    - name: Delete tunnel group within netbox
      netbox.netbox.netbox_tunnel_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Tunnel Group
        state: absent
"""

RETURN = r"""
tunnel_group:
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_vpn import (
    NetboxVpnModule,
    NB_TUNNEL_GROUPS,
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

    netbox_tunnel_group = NetboxVpnModule(module, NB_TUNNEL_GROUPS)
    netbox_tunnel_group.run()


if __name__ == "__main__":  # pragma: no cover
    main()

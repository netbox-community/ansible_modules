#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Rich Bibby, NetBox Labs (@richbibby)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_tunnel
short_description: Create, update or delete tunnels within NetBox
description:
  - Creates, updates or removes tunnels from NetBox
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
    type: dict
    description:
      - Defines the tunnel configuration
    suboptions:
      name:
        description:
          - The name of the tunnel
        required: true
        type: str
      status:
        description:
          - Status of the tunnel
        required: false
        type: raw
      tunnel_group:
        description:
          - The Tunnel group the VLAN will be associated with. Must exist in NetBox
        required: false
        type: raw
      encapsulation:
        description:
          - The encapsulation protocol or technique employed to effect the tunnel
        choices:
          - ipsec-transport
          - ipsec-tunnel
          - ip-ip
          - gre
        required: true
        type: str
      ipsec_profile:
        description:
          - The IPSec Profile employed to negotiate security associations
        required: false
        type: raw
      tenant:
        description:
          - The tenant that the tunnel will be associated with
        required: false
        type: raw
      tunnel_id:
        description:
          - The ID of the tunnel
        required: false
        type: int
      description:
        description:
          - The description of the tunnel
        required: false
        type: str
      comments:
        description:
          - Comments that may include additional information in regards to the tunnel
        required: false
        type: str
      tags:
        description:
          - Any tags that the tunnel may need to be associated with
        required: false
        type: list
        elements: raw
      custom_fields:
        description:
          - Must exist in NetBox
        required: false
        type: dict
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: false

  tasks:
    - name: Create tunnel within NetBox with only required information
      netbox.netbox.netbox_tunnel:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Tunnel
          encapsulation: ipsec-tunnel
        state: present

    - name: Delete tunnel within NetBox
      netbox.netbox.netbox_tunnel:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Tunnel
          encapsulation: ipsec-tunnel
        state: absent

    - name: Create tunnel with all information
      netbox.netbox.netbox_tunnel:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Tunnel
          status: planned
          tunnel_group: Test Tunnel Group
          encapsulation: ipsec-tunnel
          ipsec_profile: ipsec-profile
          description: Test Description
          tenant: Test Tenant
          tunnel_id: 200
          tags:
            - Schnozzberry
        state: present
"""

RETURN = r"""
tunnel:
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
    NB_TUNNELS,
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
                    status=dict(required=False, type="raw"),
                    tunnel_group=dict(required=False, type="raw"),
                    encapsulation=dict(
                        required=True,
                        type="str",
                        choices=[
                            "ipsec-transport",
                            "ipsec-tunnel",
                            "ip-ip",
                            "gre",
                        ],
                    ),
                    ipsec_profile=dict(required=False, type="raw"),
                    tenant=dict(required=False, type="raw"),
                    tunnel_id=dict(required=False, type="int"),
                    description=dict(required=False, type="str"),
                    comments=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["name", "encapsulation"]),
        ("state", "absent", ["name", "encapsulation"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_tunnel = NetboxVpnModule(module, NB_TUNNELS)
    netbox_tunnel.run()


if __name__ == "__main__":  # pragma: no cover
    main()

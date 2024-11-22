#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2023, Andrii Konts (@andrii-konts) <andrew.konts@uk2group.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_l2vpn_termination
short_description: Create, update or delete L2VPNs terminations within NetBox
description:
  - Creates, updates or removes L2VPNs terminations from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
 - Andrii Konts (@andrii-konts)
requirements:
  - pynetbox
seealso:
  - name: FHRP Group Model reference
    description: NetBox Documentation for FHRP Group Model.
    link: https://docs.netbox.dev/en/stable/models/ipam/l2vpntermination/
version_added: '3.13.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the L2VPN termination configuration
    suboptions:
      l2vpn:
        description:
          - L2vpn object id
        required: true
        type: int
      assigned_object_type:
        description:
          - Assigned object type
        required: true
        choices:
          - dcim.interface
          - ipam.vlan
          - virtualization.vminterface
        type: str
      assigned_object_id:
        description:
          - Assigned object id
        required: true
        type: int
      tags:
        description:
          - Any tags that the L2VPN termination may need to be associated with
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
  hosts: localhost
  connection: local
  module_defaults:
    group/netbox.netbox.netbox:
      netbox_url: "http://netbox.local"
      netbox_token: "thisIsMyToken"
  tasks:
    - name: Create L2VPN termination within NetBox with only required information
      netbox.netbox.netbox_l2vpn_termination:
        data:
          l2vpn: 1
          assigned_object_type: dcim.interface
          assigned_object_id: 32
        state: present

    - name: Delete L2VPN termination within netbox
      netbox.netbox.netbox_l2vpn_termination:
        data:
          l2vpn: 1
          assigned_object_type: dcim.interface
          assigned_object_id: 32
        state: absent
"""

RETURN = r"""
l2vpn_termination:
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
    NetboxModule,
    NETBOX_ARG_SPEC,
)

from ansible_collections.netbox.netbox.plugins.module_utils.netbox_ipam import (
    NetboxIpamModule,
    NB_L2VPN_TERMINATIONS as NB_IPAM_L2VPN_TERMINATIONS,
)
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_vpn import (
    NetboxVpnModule,
    NB_L2VPN_TERMINATIONS as NB_VPN_L2VPN_TERMINATIONS,
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
                    l2vpn=dict(required=True, type="int"),
                    assigned_object_type=dict(
                        required=True,
                        choices=[
                            "dcim.interface",
                            "ipam.vlan",
                            "virtualization.vminterface",
                        ],
                    ),
                    assigned_object_id=dict(required=True, type="int"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    module = NetboxAnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    netbox_l2vpn_termination = NetboxModule(module, "")
    if netbox_l2vpn_termination._find_app(NB_IPAM_L2VPN_TERMINATIONS) == "ipam":
        netbox_l2vpn_termination = NetboxIpamModule(module, NB_IPAM_L2VPN_TERMINATIONS)
    if netbox_l2vpn_termination._find_app(NB_VPN_L2VPN_TERMINATIONS) == "vpn":
        netbox_l2vpn_termination = NetboxVpnModule(module, NB_VPN_L2VPN_TERMINATIONS)

    netbox_l2vpn_termination.run()


if __name__ == "__main__":
    main()

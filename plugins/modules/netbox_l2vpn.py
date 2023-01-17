#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Martin Rødvand (@rodvand) <martin@rodvand.net>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_l2vpn
short_description: Create, update or delete L2VPNs within NetBox
description:
  - Creates, updates or removes L2VPNs from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Martin Rødvand (@rodvand)
requirements:
  - pynetbox
version_added: '3.9.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the L2VPN configuration
    suboptions:
      name:
        description:
          - The name of the L2VPN
        required: true
        type: str              
      type:
        description:
          - The type of L2VPN
        required: true
        type: raw
      identifier:
        description:
          - The identifier of the L2VPN
        required: false
        type: int     
      import_targets:
        description:
          - Route targets to import
        required: false
        type: list
        elements: raw
      export_targets:
        description:
          - Route targets to export
        required: false
        type: list
        elements: raw       
      description:
        description:
          - The description of the L2VPN
        required: false
        type: str
      comments:
        description:
          - Comments that may include additional information in regards to the L2VPN
        required: false
        type: str
        version_added: "3.10.0"
      tenant:
        description:
          - The tenant that the L2VPN will be assigned to
        required: false
        type: raw
      tags:
        description:
          - Any tags that the L2VPN may need to be associated with
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
  gather_facts: False

  tasks:
    - name: Create L2VPN within NetBox with only required information
      netbox.netbox.netbox_l2vpn:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test L2VPN
          type: vxlan
        state: present

    - name: Delete L2VPN within netbox
      netbox.netbox.netbox_l2vpn:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test L2VPN
          type: vxlan
        state: absent

    - name: Create L2VPN with all required information
      netbox.netbox.netbox_l2vpn:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test L2VPN
          type: vpls
          identifier: 43256
          import_targets:
            - "65000:1"
          export_targets:
            - "65000:2"            
          tenant: Test Tenant                    
          description: Just a test
          tags:
            - Schnozzberry
        state: present
"""

RETURN = r"""
l2vpn:
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_ipam import (
    NetboxIpamModule,
    NB_L2VPNS,
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
                    type=dict(required=True, type="raw"),
                    identifier=dict(required=False, type="int"),
                    import_targets=dict(required=False, type="list", elements="raw"),
                    export_targets=dict(required=False, type="list", elements="raw"),
                    description=dict(required=False, type="str"),
                    comments=dict(required=False, type="str"),
                    tenant=dict(required=False, type="raw"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )
    required_if = [
        ("state", "present", ["name", "type"]),
        ("state", "absent", ["name", "type"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_l2vpn = NetboxIpamModule(module, NB_L2VPNS)
    netbox_l2vpn.run()


if __name__ == "__main__":
    main()

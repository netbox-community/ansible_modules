#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2023, Andrii Konts (@andrii-konts) <andrew.konts@uk2group.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_fhrp_group
short_description: Create, update or delete FHRP groups within NetBox
description:
  - Creates, updates or removes FHRP groups from NetBox
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
    link: https://docs.netbox.dev/en/stable/models/ipam/fhrpgroup/
version_added: '3.12.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the FHRP group configuration
    suboptions:
      protocol:
        description:
          - Protocol
        required: False
        type: str
        choices:
          - vrrp2
          - vrrp3
          - carp
          - clusterxl
          - hsrp
          - glbp
          - other
      group_id:
        description:
          - Group ID (0 .. 32767)
        type: int
        required: true
      auth_type:
        description:
          - Authentication type
        choices:
          - plaintext
          - md5
        type: str
      auth_key:
        description:
          - Authentication key (max length 255)
        type: str
      description:
        description:
          - Description (max length 200)
        required: false
        type: str
      tags:
        description:
          - Any tags that the FHRP group may need to be associated with
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
- hosts: localhost
  connection: local
  module_defaults:
    group/netbox.netbox.netbox:
      netbox_url: "http://netbox.local"
      netbox_token: "thisIsMyToken"

  tasks:
    - name: "Create FHRP group within netbox"
      netbox.netbox.netbox_fhrp_group:
        data:
          protocol: "glbp"
          group_id: 111
          auth_type: md5
          auth_key: 11111
          description: test FHRP group
        state: present

    - name: Delete FHRP group within netbox
      netbox.netbox.netbox_fhrp_group:
        data:
          group_id: 111
        state: absent
"""

RETURN = r"""
fhrp_group:
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
    NB_FHRP_GROUPS,
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
                    protocol=dict(
                        type="str",
                        choices=[
                            "vrrp2",
                            "vrrp3",
                            "carp",
                            "clusterxl",
                            "hsrp",
                            "glbp",
                            "other",
                        ],
                    ),
                    group_id=dict(required=True, type="int"),
                    auth_type=dict(type="str", choices=["plaintext", "md5"]),
                    auth_key=dict(type="str", no_log=True),
                    description=dict(type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )
    required_if = [("state", "present", ["protocol"])]
    module = NetboxAnsibleModule(argument_spec=argument_spec, required_if=required_if)
    netbox_fhrp_group = NetboxIpamModule(module, NB_FHRP_GROUPS)
    netbox_fhrp_group.run()


if __name__ == "__main__":
    main()

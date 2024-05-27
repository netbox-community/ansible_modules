#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2023, Andrii Konts (@andrii-konts) <andrew.konts@uk2group.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_fhrp_group_assignment
short_description: Create, update or delete FHRP group assignments within NetBox
description:
  - Creates, updates or removes FHRP group assignments from NetBox
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
    link: https://docs.netbox.dev/en/stable/models/ipam/fhrpgroupassignment/
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the FHRP group assignment configuration
    suboptions:
      fhrp_group:
        description:
          - FHRP Group ID
        required: true
        type: int
      interface_type:
        description:
          - Interface type
        required: true
        choices:
          - dcim.interface
          - virtualization.vminterface
        type: str
      interface_id:
        description:
          - Interface ID
        type: int
        required: true
      priority:
        description:
          - Priority (0 .. 255)
        type: int
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
    - name: "Create FHRP group assignment within netbox"
      netbox.netbox.netbox_fhrp_group_assignment:
        data:
          fhrp_group: 3
          interface_type: dcim.interface
          interface_id: 5
          priority: 1
        state: present

    - name: Delete FHRP group assignment within netbox
      netbox.netbox.netbox_fhrp_group_assignment:
        data:
          fhrp_group: 3
          interface_type: dcim.interface
          interface_id: 5
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
    NB_FHRP_GROUP_ASSIGNMENTS,
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
                    fhrp_group=dict(required=True, type="int"),
                    interface_type=dict(
                        required=True,
                        type="str",
                        choices=["dcim.interface", "virtualization.vminterface"],
                    ),
                    interface_id=dict(required=True, type="int"),
                    priority=dict(type="int"),
                ),
            ),
        )
    )
    required_if = [("state", "present", ["priority"])]

    module = NetboxAnsibleModule(argument_spec=argument_spec, required_if=required_if)

    netbox_fhrp_group = NetboxIpamModule(module, NB_FHRP_GROUP_ASSIGNMENTS)
    netbox_fhrp_group.run()


if __name__ == "__main__":
    main()

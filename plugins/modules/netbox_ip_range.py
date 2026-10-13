#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2026, James Crowley (@james-crowley)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_ip_range
short_description: Creates or removes IP ranges from NetBox
description:
  - Creates or removes IP ranges from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - James Crowley (@james-crowley)
requirements:
  - pynetbox
version_added: '3.24.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the IP range configuration
    suboptions:
      start_address:
        description:
          - Required if state is C(present). The starting address of the range, with mask.
        required: false
        type: str
      end_address:
        description:
          - Required if state is C(present). The ending address of the range, with mask.
        required: false
        type: str
      vrf:
        description:
          - VRF that the IP range is associated with
        required: false
        type: raw
      tenant:
        description:
          - The tenant that the IP range will be assigned to
        required: false
        type: raw
      status:
        description:
          - The status of the IP range
        required: false
        type: raw
      ip_range_role:
        description:
          - The role of the IP range
        required: false
        type: raw
      mark_populated:
        description:
          - Prevent the creation of IP addresses within this range
        required: false
        type: bool
      mark_utilized:
        description:
          - Treat as 100% utilized
        required: false
        type: bool
      description:
        description:
          - The description of the IP range
        required: false
        type: str
      comments:
        description:
          - Comments that may include additional information in regards to the IP range
        required: false
        type: str
      tags:
        description:
          - Any tags that the IP range may need to be associated with
        required: false
        type: list
        elements: raw
      custom_fields:
        description:
          - Must exist in NetBox and in key/value format
        required: false
        type: dict
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox IP range module"
  connection: local
  hosts: localhost
  gather_facts: false

  tasks:
    - name: Create IP range within NetBox with only required information
      netbox.netbox.netbox_ip_range:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          start_address: 10.156.0.10/24
          end_address: 10.156.0.50/24
        state: present

    - name: Delete IP range within NetBox
      netbox.netbox.netbox_ip_range:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          start_address: 10.156.0.10/24
          end_address: 10.156.0.50/24
        state: absent

    - name: Create IP range with several specified options
      netbox.netbox.netbox_ip_range:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          start_address: 10.156.32.10/24
          end_address: 10.156.32.50/24
          vrf: Test VRF
          tenant: Test Tenant
          status: Reserved
          ip_range_role: Network of care
          description: Test description
          mark_populated: true
          mark_utilized: true
          tags:
            - Schnozzberry
        state: present
"""

RETURN = r"""
ip_range:
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_ipam import (
    NetboxIpamModule,
    NB_IP_RANGES,
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
                    start_address=dict(required=False, type="str"),
                    end_address=dict(required=False, type="str"),
                    vrf=dict(required=False, type="raw"),
                    tenant=dict(required=False, type="raw"),
                    status=dict(required=False, type="raw"),
                    ip_range_role=dict(required=False, type="raw"),
                    mark_populated=dict(required=False, type="bool"),
                    mark_utilized=dict(required=False, type="bool"),
                    description=dict(required=False, type="str"),
                    comments=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["start_address", "end_address"]),
        ("state", "absent", ["start_address", "end_address"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_ip_range = NetboxIpamModule(module, NB_IP_RANGES)
    netbox_ip_range.run()


if __name__ == "__main__":  # pragma: no cover
    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2023, Andrii Konts (@andrii-konts) <andrew.konts@uk2group.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_asn
short_description: Create, update or delete ASNs within NetBox
description:
  - Creates, updates or removes ASNs from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Andrii Konts (@andrii-konts)
requirements:
  - pynetbox
version_added: '3.12.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the ASN configuration
    suboptions:
      asn:
        description:
          - 32-bit autonomous system number
        required: true
        type: int
      rir:
        description:
          - RIR
        required: false
        type: raw
      tenant:
        description:
          - Tenant
        required: false
        type: raw
      description:
        description:
          - Description
        required: false
        type: str
      tags:
        description:
          - Any tags that the ASN may need to be associated with
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
    - name: Create ASN within NetBox with only required information
      netbox.netbox.netbox_asn:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          asn: 1111111111
          rir: RFC1111
          description: test ASN
        state: present

    - name: Delete ASN within netbox
      netbox.netbox.netbox_asn:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          asn: 1111111111
        state: absent
"""

RETURN = r"""
asn:
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
    NB_ASNS,
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
                    asn=dict(required=True, type="int"),
                    rir=dict(required=False, type="raw"),
                    tenant=dict(required=False, type="raw"),
                    description=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )
    required_if = [("state", "present", ["rir"])]
    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )
    netbox_cable = NetboxIpamModule(module, NB_ASNS)
    netbox_cable.run()


if __name__ == "__main__":
    main()

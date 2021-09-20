#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Mikhail Yohman (@FragmentedPacket) <mikhail.yohman@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: netbox_prefix
short_description: Creates or removes prefixes from Netbox
description:
  - Creates or removes prefixes from Netbox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Mikhail Yohman (@FragmentedPacket)
  - Anthony Ruhier (@Anthony25)
requirements:
  - pynetbox
version_added: '0.1.0'
options:
  netbox_url:
    description:
      - URL of the Netbox instance resolvable by Ansible control host
    required: true
    type: str
  netbox_token:
    description:
      - The token created within Netbox to authorize API access
    required: true
    type: str
  cert:
    description:
      - Certificate path
    required: false
    type: raw
  data:
    type: dict
    description:
      - Defines the prefix configuration
    suboptions:
      family:
        description:
          - Specifies which address family the prefix prefix belongs to
        required: false
        type: int
      prefix:
        description:
          - Required if state is C(present) and first_available is False. Will allocate or free this prefix.
        required: false
        type: raw
      parent:
        description:
          - Required if state is C(present) and first_available is C(yes). Will get a new available prefix in this parent prefix.
        required: false
        type: raw
      prefix_length:
        description:
          - |
            Required ONLY if state is C(present) and first_available is C(yes).
            Will get a new available prefix of the given prefix_length in this parent prefix.
        required: false
        type: int
      site:
        description:
          - Site that prefix is associated with
        required: false
        type: raw
      vrf:
        description:
          - VRF that prefix is associated with
        required: false
        type: raw
      tenant:
        description:
          - The tenant that the prefix will be assigned to
        required: false
        type: raw
      vlan:
        description:
          - The VLAN the prefix will be assigned to
        required: false
        type: raw
      status:
        description:
          - The status of the prefix
        required: false
        type: raw
      prefix_role:
        description:
          - The role of the prefix
        required: false
        type: raw
      is_pool:
        description:
          - All IP Addresses within this prefix are considered usable
        required: false
        type: bool
      description:
        description:
          - The description of the prefix
        required: false
        type: str
      tags:
        description:
          - Any tags that the prefix may need to be associated with
        required: false
        type: list
        elements: raw
      custom_fields:
        description:
          - Must exist in Netbox and in key/value format
        required: false
        type: dict
    required: true
  state:
    description:
      - Use C(present) or C(absent) for adding or removing.
    choices: [ absent, present ]
    default: present
    type: str
  first_available:
    description:
      - If C(yes) and state C(present), if an parent is given, it will get the
        first available prefix of the given prefix_length inside the given parent (and
        vrf, if given).
        Unused with state C(absent).
    default: false
    type: bool
  query_params:
    description:
      - This can be used to override the specified values in ALLOWED_QUERY_PARAMS that is defined
      - in plugins/module_utils/netbox_utils.py and provides control to users on what may make
      - an object unique in their environment.
    required: false
    type: list
    elements: str
  validate_certs:
    description:
      - If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
    default: true
    type: raw
"""

EXAMPLES = r"""
- name: "Test Netbox prefix module"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create prefix within Netbox with only required information
      netbox_prefix:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          prefix: 10.156.0.0/19
        state: present

    - name: Delete prefix within netbox
      netbox_prefix:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          prefix: 10.156.0.0/19
        state: absent

    - name: Create prefix with several specified options
      netbox_prefix:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          family: 4
          prefix: 10.156.32.0/19
          site: Test Site
          vrf: Test VRF
          tenant: Test Tenant
          vlan:
            name: Test VLAN
            site: Test Site
            tenant: Test Tenant
            vlan_group: Test Vlan Group
          status: Reserved
          prefix_role: Network of care
          description: Test description
          is_pool: true
          tags:
            - Schnozzberry
        state: present

    - name: Get a new /24 inside 10.156.0.0/19 within Netbox - Parent doesn't exist
      netbox_prefix:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          parent: 10.156.0.0/19
          prefix_length: 24
        state: present
        first_available: yes

    - name: Create prefix within Netbox with only required information
      netbox_prefix:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          prefix: 10.156.0.0/19
        state: present

    - name: Get a new /24 inside 10.156.0.0/19 within Netbox
      netbox_prefix:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          parent: 10.156.0.0/19
          prefix_length: 24
        state: present
        first_available: yes

    - name: Get a new /24 inside 10.157.0.0/19 within Netbox with additional values
      netbox_prefix:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          parent: 10.157.0.0/19
          prefix_length: 24
          vrf: Test VRF
          site: Test Site
        state: present
        first_available: yes
"""

RETURN = r"""
prefix:
  description: Serialized object as created or already existent within Netbox
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
    NB_PREFIXES,
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
                    family=dict(required=False, type="int"),
                    prefix=dict(required=False, type="raw"),
                    parent=dict(required=False, type="raw"),
                    prefix_length=dict(required=False, type="int"),
                    site=dict(required=False, type="raw"),
                    vrf=dict(required=False, type="raw"),
                    tenant=dict(required=False, type="raw"),
                    vlan=dict(required=False, type="raw"),
                    status=dict(required=False, type="raw"),
                    prefix_role=dict(required=False, type="raw"),
                    is_pool=dict(required=False, type="bool"),
                    description=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
            first_available=dict(required=False, type="bool", default=False),
        )
    )

    required_if = [
        ("state", "present", ["prefix", "parent"], True),
        ("state", "absent", ["prefix"]),
        ("first_available", "yes", ["parent"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_prefix = NetboxIpamModule(module, NB_PREFIXES)
    netbox_prefix.run()


if __name__ == "__main__":  # pragma: no cover
    main()

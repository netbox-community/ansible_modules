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
module: netbox_vlan_group
short_description: Create, update or delete vlans groups within Netbox
description:
  - Creates, updates or removes vlans groups from Netbox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Mikhail Yohman (@FragmentedPacket)
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
      - Defines the vlan group configuration
    suboptions:
      name:
        description:
          - The name of the vlan group
        required: true
        type: str
      slug:
        description:
          - The slugified version of the name or custom slug.
          - This is auto-generated following NetBox rules if not provided
        required: false
        type: str
      site:
        description:
          - The site the vlan will be assigned to (NetBox < 2.11)
          - Will be removed in version 5.0.0
        required: false
        type: raw
      scope_type:
        description:
          - Type of scope to be applied (NetBox 2.11+)
        required: false
        type: str
        choices:
          - "dcim.location"
          - "dcim.rack"
          - "dcim.region"
          - "dcim.site"
          - "dcim.sitegroup"
          - "virtualization.cluster"
          - "virtualization.clustergroup"
        version_added: "3.1.0"
      scope:
        description:
          - Object related to scope type (NetBox 2.11+)
        required: false
        type: raw
        version_added: "3.1.0"
      description:
        description:
          - Description for VLAN group
        required: false
        type: str
        version_added: "3.1.0"
      custom_fields:
        description:
          - must exist in Netbox
        required: false
        type: dict
        version_added: "3.1.0"
    required: true
  state:
    description:
      - Use C(present) or C(absent) for adding or removing.
    choices: [ absent, present ]
    default: present
    type: str
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
- name: "Test Netbox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create vlan group within Netbox with only required information - Pre 2.11
      netbox_vlan_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test vlan group
          site: Test Site
        state: present

    - name: Create vlan group within Netbox with only required information - Post 2.11
      netbox_vlan_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test vlan group
          scope_type: "dcim.site"
          scope: Test Site
        state: present

    - name: Delete vlan group within netbox
      netbox_vlan_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test vlan group
        state: absent
"""

RETURN = r"""
vlan_group:
  description: Serialized object as created or already existent within Netbox
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
    NB_VLAN_GROUPS,
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
                    site=dict(
                        required=False,
                        type="raw",
                        removed_in_version="5.0.0",
                        removed_from_collection="netbox.netbox",
                    ),
                    scope_type=dict(
                        required=False,
                        type="str",
                        choices=[
                            "dcim.location",
                            "dcim.rack",
                            "dcim.region",
                            "dcim.site",
                            "dcim.sitegroup",
                            "virtualization.cluster",
                            "virtualization.clustergroup",
                        ],
                    ),
                    scope=dict(required=False, type="raw"),
                    description=dict(required=False, type="str"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [("state", "present", ["name"]), ("state", "absent", ["name"])]
    required_together = [("scope_type", "scope")]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=required_if,
        required_together=required_together,
    )

    netbox_vlan_group = NetboxIpamModule(module, NB_VLAN_GROUPS)
    netbox_vlan_group.run()


if __name__ == "__main__":  # pragma: no cover
    main()

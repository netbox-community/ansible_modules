#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2020, Pavel Korovin (@pkorovin) <p@tristero.se>
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
module: netbox_config_context
short_description: Creates, updates or deletes configuration contexts within Netbox
description:
  - Creates, updates or removes configuration contexts from Netbox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Pavel Korovin (@pkorovin)
requirements:
  - pynetbox
version_added: "1.1.1"
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
  data:
    type: dict
    description:
      - Defines the configuration context
    suboptions:
      name:
        description:
          - Name of the context
        required: true
        type: str
      weight:
        description:
          - The weight of the configuration context
        required: false
        type: int
      data:
        description:
          - JSON-formatted configuration context data
        required: true
        type: int
      description:
        description:
          - The description of the configuration context
        required: false
        type: str
      is_active:
        description:
          - Whether configuration context is active
        required: false
        type: bool
      regions:
        description:
          - List of regions where configuration context applies
        required: false
        type: list
      sites:
        description:
          - List of sites where configuration context applies
        required: false
        type: list
      roles:
        description:
          - List of roles to which configuration context applies
        required: false
        type: list
      platforms:
        description:
          - List of platforms to which configuration context applies
        required: false
        type: list
      cluster_groups:
        description:
          - List of cluster_groups to which configuration context applies
        required: false
        type: list
      clusters:
        description:
          - List of clusters to which configuration context applies
        required: false
        type: list
      tenant_groups:
        description:
          - List of tenant_groups to which configuration context applies
        required: false
        type: list
      tenants:
        description:
          - List of tenants to which configuration context applies
        required: false
        type: list
      tags:
        description:
          - Any tags that the configuration context associates with
        required: false
        type: list
    required: true
  state:
    description:
      - Use C(present) or C(absent) for adding or removing.
    choices: [ absent, present ]
    default: present
    type: str
  validate_certs:
    description:
      - |
        If C(no), SSL certificates will not be validated.
        This should only be used on personally controlled sites using self-signed certificates.
    default: true
    type: raw
"""

EXAMPLES = r"""
- name: "Test Netbox config_context module"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create config context and apply it to sites euc1-az1, euc1-az2 with the default weight of 1000
      netbox_config_context:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "dns_nameservers-quadnine"
          description: "9.9.9.9"
          data: "{ \"dns\": { \"nameservers\": [ \"9.9.9.9\" ] } }"
          sites: [ euc1-az1, euc1-az2 ]

    - name: Detach config context from euc1-az1, euc1-az2 and attach to euc1-az3
      netbox_config_context:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "dns_nameservers-quadnine"
          data: "{ \"dns\": { \"nameservers\": [ \"9.9.9.9\" ] } }"
          sites: [ euc1-az3 ]

    - name: Delete config context
      netbox_config_context:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "dns_nameservers-quadnine"
          data: "{ \"dns\": { \"nameservers\": [ \"9.9.9.9\" ] } }"
        state: absent
"""

RETURN = r"""
config_context:
  description: Serialized object as created/existent/updated/deleted within Netbox
  returned: always
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_extras import (
    NetboxExtrasModule,
    NB_CONFIG_CONTEXTS,
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
                    weight=dict(required=False, type="int"),
                    description=dict(required=False, type="str"),
                    is_active=dict(required=False, type="bool"),
                    regions=dict(required=False, type="list"),
                    sites=dict(required=False, type="list"),
                    roles=dict(required=False, type="list"),
                    platforms=dict(required=False, type="list"),
                    cluster_groups=dict(required=False, type="list"),
                    clusters=dict(required=False, type="list"),
                    tenant_groups=dict(required=False, type="list"),
                    tenants=dict(required=False, type="list"),
                    tags=dict(required=False, type="list"),
                    data=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [("state", "present", ["name", "data"]), ("state", "absent", ["name"])]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_config_context = NetboxExtrasModule(module, NB_CONFIG_CONTEXTS)
    netbox_config_context.run()


if __name__ == "__main__":  # pragma: no cover
    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2020, Pavel Korovin (@pkorovin) <p@tristero.se>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_config_context
short_description: Creates, updates or deletes configuration contexts within NetBox
description:
  - Creates, updates or removes configuration contexts from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Pavel Korovin (@pkorovin)
requirements:
  - pynetbox
version_added: "3.3.0"
extends_documentation_fragment:
  - netbox.netbox.common
options:
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
        required: false
        type: dict
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
        elements: str
      site_groups:
        description:
          - List of site groups where configuration context applies
        required: false
        type: list
        elements: str
      sites:
        description:
          - List of sites where configuration context applies
        required: false
        type: list
        elements: str
      roles:
        description:
          - List of roles to which configuration context applies
        required: false
        type: list
        elements: str
      device_types:
        description:
          - List of device_types to which configuration context applies
        required: false
        type: list
        elements: str
      platforms:
        description:
          - List of platforms to which configuration context applies
        required: false
        type: list
        elements: str
      cluster_types:
        description:
          - List of cluster_types to which configuration context applies
        required: false
        type: list
        elements: str
      cluster_groups:
        description:
          - List of cluster_groups to which configuration context applies
        required: false
        type: list
        elements: str
      clusters:
        description:
          - List of clusters to which configuration context applies
        required: false
        type: list
        elements: str
      tenant_groups:
        description:
          - List of tenant_groups to which configuration context applies
        required: false
        type: list
        elements: str
      tenants:
        description:
          - List of tenants to which configuration context applies
        required: false
        type: list
        elements: str
      tags:
        description:
          - Any tags that the configuration context associates with
        required: false
        type: list
        elements: str
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox config_context module"
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
  description: Serialized object as created/existent/updated/deleted within NetBox
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
                    regions=dict(required=False, type="list", elements="str"),
                    sites=dict(required=False, type="list", elements="str"),
                    site_groups=dict(required=False, type="list", elements="str"),
                    roles=dict(required=False, type="list", elements="str"),
                    device_types=dict(required=False, type="list", elements="str"),
                    platforms=dict(required=False, type="list", elements="str"),
                    cluster_types=dict(required=False, type="list", elements="str"),
                    cluster_groups=dict(required=False, type="list", elements="str"),
                    clusters=dict(required=False, type="list", elements="str"),
                    tenant_groups=dict(required=False, type="list", elements="str"),
                    tenants=dict(required=False, type="list", elements="str"),
                    tags=dict(required=False, type="list", elements="str"),
                    data=dict(required=False, type="dict"),
                ),
            )
        )
    )

    required_if = [
        ("state", "present", ["name", "data"]),
        ("state", "absent", ["name"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_config_context = NetboxExtrasModule(module, NB_CONFIG_CONTEXTS)
    netbox_config_context.run()


if __name__ == "__main__":  # pragma: no cover
    main()

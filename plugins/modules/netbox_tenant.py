#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Amy Liebowitz (@amylieb)
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
module: netbox_tenant
short_description: Creates or removes tenants from Netbox
description:
  - Creates or removes tenants from Netbox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Amy Liebowitz (@amylieb)
requirements:
  - pynetbox
version_added: "0.1.0"
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
      - Defines the tenant configuration
    suboptions:
      name:
        description:
          - Name of the tenant to be created
        required: true
        type: str
      tenant_group:
        description:
          - Tenant group this tenant should be in
        required: false
        type: raw
      description:
        description:
          - The description of the tenant
        required: false
        type: str
      comments:
        description:
          - Comments for the tenant. This can be markdown syntax
        required: false
        type: str
      slug:
        description:
          - URL-friendly unique shorthand
        required: false
        type: str
      tags:
        description:
          - Any tags that the tenant may need to be associated with
        required: false
        type: list
      custom_fields:
        description:
          - must exist in Netbox
        required: false
        type: dict
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
      - |
        If C(no), SSL certificates will not be validated.
        This should only be used on personally controlled sites using self-signed certificates.
    default: true
    type: raw
"""

EXAMPLES = r"""
- name: "Test Netbox module"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create tenant within Netbox with only required information
      netbox_tenant:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Tenant ABC
        state: present

    - name: Delete tenant within netbox
      netbox_tenant:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Tenant ABC
        state: absent

    - name: Create tenant with all parameters
      netbox_tenant:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Tenant ABC
          group: Very Special Tenants
          description: ABC Incorporated
          comments: '### This tenant is super cool'
          slug: tenant_abc
          tags:
            - tagA
            - tagB
            - tagC
        state: present
"""

RETURN = r"""
tenant:
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_tenancy import (
    NetboxTenancyModule,
    NB_TENANTS,
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
                    tenant_group=dict(required=False, type="raw"),
                    description=dict(required=False, type="str"),
                    comments=dict(required=False, type="str"),
                    slug=dict(required=False, type="str"),
                    tags=dict(required=False, type="list"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [("state", "present", ["name"]), ("state", "absent", ["name"])]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_tenant = NetboxTenancyModule(module, NB_TENANTS)
    netbox_tenant.run()


if __name__ == "__main__":  # pragma: no cover
    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Alberto Gonzalez (@agonza05) <agonza05@gmail.com>
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
module: netbox_site_group
short_description: Creates or removes site groups from Netbox
description:
  - Creates or removes site groups from Netbox (NetBox 2.11+)
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Alberto Gonzalez (@agonza05)
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
  cert:
    description:
      - Certificate path
    required: false
    type: raw
  data:
    type: dict
    description:
      - Defines the site configuration
    suboptions:
      name:
        description:
          - Name of the site to be created
        required: true
        type: str
      description:
        description:
          - The description of the prefix
        required: false
        type: str
      parent_site_group:
        description:
          - The parent site group this site group should be tied to
        required: false
        type: raw
      slug:
        description:
          - URL-friendly unique shorthand
        required: false
        type: str
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
- name: "Test Netbox site group module"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create site group within Netbox with only required information
      netbox_site_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test - Europe
        state: present

    - name: Delete site group within netbox
      netbox_site:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test - Europe
        state: absent

    - name: Create site group with all parameters
      netbox_site:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test - United Kingdom
          description: This is a test description
          parent_site_group: Test - Europe
          slug: test-uk
        state: present
"""

RETURN = r"""
site_group:
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_dcim import (
    NetboxDcimModule,
    NB_SITE_GROUPS,
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
                    description=dict(required=False, type="str"),
                    slug=dict(required=False, type="str"),
                    parent_site_group=dict(required=False, type="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [("state", "present", ["name"]), ("state", "absent", ["name"])]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_site_group = NetboxDcimModule(module, NB_SITE_GROUPS)
    netbox_site_group.run()


if __name__ == "__main__":  # pragma: no cover
    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Andrew Simmons (@andybro19) <andrewkylesimmons@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_site_group
short_description: Create, update, or delete site groups within NetBox
description:
  - Creates, updates, or deletes site groups within NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Andrew Simmons (@andybro19)
requirements:
  - pynetbox
version_added: '3.4.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the site group configuration
    suboptions:
      name:
        description:
          - Name of the site group to be created
        required: true
        type: str
      slug:
        description:
          - The slugified version of the name or custom slug.
          - This is auto-generated following NetBox rules if not provided
        required: false
        type: str
      parent_site_group:
        description:
          - The parent site group the site group will be associated with
        required: false
        type: raw
      description:
        description:
          - The description of the site group
        required: false
        type: str
      tags:
        description:
          - The tags to add/update
        required: false
        type: list
        elements: raw
        version_added: "3.6.0"
      custom_fields:
        description:
          - Must exist in NetBox
        required: false
        type: dict
        version_added: "3.6.0"
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox site group module"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create site group within NetBox with only required information
      netbox.netbox.netbox_site_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Site group
        state: present

    - name: Create site group within NetBox with a parent site group
      netbox.netbox.netbox_site_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Child site group
          parent_site_group: Site group
        state: present

    - name: Delete site group within NetBox
      netbox.netbox.netbox_site_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Site group
        state: absent
"""

RETURN = r"""
site_group:
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
                    slug=dict(required=False, type="str"),
                    parent_site_group=dict(required=False, type="raw"),
                    description=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
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

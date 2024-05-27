#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Martin Rødvand (@rodvand)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_contact_group
short_description: Creates or removes contact groups from NetBox
description:
  - Creates or removes contact groups from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Martin Rødvand (@rodvand)
requirements:
  - pynetbox
version_added: "3.5.0"
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the contact group configuration
    suboptions:
      name:
        description:
          - Name of the contact group to be created
        required: true
        type: str
      slug:
        description:
          - URL-friendly unique shorthand
        required: false
        type: str
      parent_contact_group:
        description:
          - Slug of the parent contact group
        required: false
        type: str
      description:
        description:
          - The description of the contact group
        required: false
        type: str
      tags:
        description:
          - Any tags that the contact group may need to be associated with
        required: false
        type: list
        elements: raw
      custom_fields:
        description:
          - must exist in NetBox
        required: false
        type: dict
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox contact group module"
  connection: local
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Create contact group within NetBox with only required information
      netbox.netbox.netbox_contact_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Contact Group ABC
          slug: "contact_group_abc"
        state: present

    - name: Delete contact group within netbox
      netbox.netbox.netbox_contact_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Contact Group ABC
        state: absent
"""

RETURN = r"""
contact_group:
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_tenancy import (
    NetboxTenancyModule,
    NB_CONTACT_GROUPS,
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
                    parent_contact_group=dict(required=False, type="str"),
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

    netbox_contact_group = NetboxTenancyModule(module, NB_CONTACT_GROUPS)
    netbox_contact_group.run()


if __name__ == "__main__":  # pragma: no cover
    main()

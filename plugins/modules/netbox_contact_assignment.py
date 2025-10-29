#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2025, Daniel Chiquito (@dchiquito)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_contact_assignment
short_description: Creates or removes contact assignments from NetBox
description:
  - Creates or removes contact assignments from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Daniel Chiquito (@dchiquito)
requirements:
  - pynetbox
version_added: "3.1.0"
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the contact configuration
    suboptions:
      object_type:
        description:
          - The type of the object the contact is assigned to
        required: true
        type: str
        choices:
          - circuit
          - cluster
          - cluster_group
          - device
          - location
          - manufacturer
          - power_panel
          - provider
          - rack
          - region
          - site
          - site_group
          - tenant
          - virtual_machine
      object_name:
        description:
          - The name of the object the contact is assigned to
        required: true
        type: str
      contact:
        description:
          - The name of the contact to assign to the object
        required: true
        type: str
      role:
        description:
          - The name of the role the contact has for this object
        required: true
        type: str
      priority:
        description:
          - The priority of this contact
        required: false
        type: str
        choices:
          - primary
          - secondary
          - tertiary
          - inactive
      tags:
        description:
          - Any tags that the contact may need to be associated with
        required: false
        type: list
        elements: raw
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox module"
  connection: local
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Assign a contact to a location with only required information
      netbox.netbox.netbox_contact_assignment:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          object_type: location
          object_name: My Location
          contact: John Doe
          role: Supervisor Role
        state: present

    - name: Delete contact assignment within netbox
      netbox.netbox.netbox_contact_assignment:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          object_type: location
          object_name: My Location
          contact: John Doe
          role: Supervisor Role
        state: absent

    - name: Create contact with all parameters
      netbox.netbox.netbox_contact:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          object_type: location
          object_name: My Location
          contact: John Doe
          role: Supervisor Role
          priority: tertiary
          tags:
            - tagA
            - tagB
            - tagC
        state: present
"""

RETURN = r"""
contact_assignment:
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
    NB_CONTACT_ASSIGNMENTS,
    OBJECT_TYPES,
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
                    object_type=dict(
                        required=True, type="str", choices=list(OBJECT_TYPES.keys())
                    ),
                    object_name=dict(required=True, type="str"),
                    contact=dict(required=True, type="str"),
                    role=dict(required=True, type="str"),
                    priority=dict(
                        required=False,
                        type="str",
                        choices=["primary", "secondary", "tertiary", "inactive"],
                    ),
                    tags=dict(required=False, type="list", elements="raw"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["object_type", "object_name", "contact", "role"]),
        ("state", "absent", ["object_type", "object_name", "contact", "role"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_contact = NetboxTenancyModule(module, NB_CONTACT_ASSIGNMENTS)
    netbox_contact.run()


if __name__ == "__main__":  # pragma: no cover
    main()

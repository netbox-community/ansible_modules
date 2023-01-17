#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Andrew Simmons (@andybro19) <andrewkylesimmons@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_location
short_description: Create, update or delete locations within NetBox
description:
  - Creates, updates or removes locations from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Andrew Simmons (@andybro19)
requirements:
  - pynetbox
version_added: '3.3.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the location configuration
    suboptions:
      name:
        description:
          - The name of the location
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
          - Required if I(state=present) and the location does not exist yet
        required: false
        type: raw
      parent_location:
        description:
          - The parent location the location will be associated with
        required: false
        type: raw
      tenant:
        description:
          - The tenant that the location will be associated with
        required: false
        type: raw
        version_added: "3.8.0"
      description:
        description:
          - The description of the location
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
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create location within NetBox with only required information
      netbox.netbox.netbox_location:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test location
          site: Test Site
        state: present

    - name: Create location within NetBox with a parent location
      netbox.netbox.netbox_location:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Child location
          site: Test Site
          parent_location: Test location
        state: present

    - name: Delete location within NetBox
      netbox.netbox.netbox_location:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test location
        state: absent
"""

RETURN = r"""
location:
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
    NB_LOCATIONS,
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
                    site=dict(required=False, type="raw"),
                    parent_location=dict(required=False, type="raw"),
                    tenant=dict(required=False, type="raw"),
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

    netbox_location = NetboxDcimModule(module, NB_LOCATIONS)
    netbox_location.run()


if __name__ == "__main__":  # pragma: no cover
    main()

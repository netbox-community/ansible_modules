#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2026, Jim Bartus (@jbartus) <jbartus@netboxlabs.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_rack_type
short_description: Create, update or delete rack types within NetBox
description:
  - Creates, updates or removes rack types from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
  - Rack types require NetBox v4.1 or newer
author:
  - Jim Bartus (@jbartus)
requirements:
  - pynetbox
version_added: '3.24.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    description:
      - Defines the rack type configuration
    suboptions:
      manufacturer:
        description:
          - The manufacturer of the rack type
        required: false
        type: raw
      model:
        description:
          - The model of the rack type
        required: true
        type: raw
      slug:
        description:
          - The slug of the rack type. Must follow slug formatting (URL friendly)
          - If not specified, it will slugify the model
          - ex. test-rack-type
        required: false
        type: str
      form_factor:
        description:
          - The form factor of the rack type
        choices:
          - 2-post-frame
          - 4-post-frame
          - 4-post-cabinet
          - wall-frame
          - wall-frame-vertical
          - wall-cabinet
          - wall-cabinet-vertical
        required: false
        type: str
      width:
        description:
          - The rail-to-rail width
        choices:
          - 10
          - 19
          - 21
          - 23
        required: false
        type: int
      u_height:
        description:
          - The height of the rack type in rack units
        required: false
        type: int
      starting_unit:
        description:
          - The lowest unit number of the rack type
        required: false
        type: int
      desc_units:
        description:
          - Rack units will be numbered top-to-bottom
        required: false
        type: bool
      outer_width:
        description:
          - The outer width of the rack type
        required: false
        type: int
      outer_height:
        description:
          - The outer height of the rack type (requires NetBox v4.4+)
        required: false
        type: int
      outer_depth:
        description:
          - The outer depth of the rack type
        required: false
        type: int
      outer_unit:
        description:
          - Whether the outer dimensions are in Millimeters or Inches and is I(required) if outer dimensions are specified
        choices:
          - mm
          - in
        required: false
        type: str
      weight:
        description:
          - The weight of the rack type
        required: false
        type: float
      max_weight:
        description:
          - Maximum load capacity of the rack type
        required: false
        type: int
      weight_unit:
        description:
          - The weight unit
        choices:
          - kg
          - g
          - lb
          - oz
        required: false
        type: str
      mounting_depth:
        description:
          - The mounting depth of the rack type
        required: false
        type: int
      description:
        description:
          - Description of the rack type
        required: false
        type: str
      comments:
        description:
          - Comments that may include additional information in regards to the rack type
        required: false
        type: str
      tags:
        description:
          - Any tags that the rack type may need to be associated with
        required: false
        type: list
        elements: raw
      custom_fields:
        description:
          - must exist in NetBox
        required: false
        type: dict
    required: true
    type: dict
"""

EXAMPLES = r"""
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: false

  tasks:
    - name: Create rack type within NetBox with only required information
      netbox.netbox.netbox_rack_type:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          model: Test Rack Type
          manufacturer: Test Manufacturer
        state: present

    - name: Create rack type within NetBox with more information
      netbox.netbox.netbox_rack_type:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          model: AR3350B2
          manufacturer: APC
          slug: ar3350b2
          description: APC NetShelter SX Server Rack Gen 2
          form_factor: 4-post-cabinet
          u_height: 42
          outer_width: 750
          outer_depth: 1200
          outer_unit: mm
        state: present

    - name: Delete rack type within netbox
      netbox.netbox.netbox_rack_type:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          model: Test Rack Type
        state: absent
"""

RETURN = r"""
rack_type:
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
    NB_RACK_TYPES,
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
                    manufacturer=dict(required=False, type="raw"),
                    model=dict(required=True, type="raw"),
                    slug=dict(required=False, type="str"),
                    form_factor=dict(
                        required=False,
                        type="str",
                        choices=[
                            "2-post-frame",
                            "4-post-frame",
                            "4-post-cabinet",
                            "wall-frame",
                            "wall-frame-vertical",
                            "wall-cabinet",
                            "wall-cabinet-vertical",
                        ],
                    ),
                    width=dict(
                        required=False,
                        type="int",
                        choices=[10, 19, 21, 23],
                    ),
                    u_height=dict(required=False, type="int"),
                    starting_unit=dict(required=False, type="int"),
                    desc_units=dict(required=False, type="bool"),
                    outer_width=dict(required=False, type="int"),
                    outer_height=dict(required=False, type="int"),
                    outer_depth=dict(required=False, type="int"),
                    outer_unit=dict(
                        required=False,
                        type="str",
                        choices=["mm", "in"],
                    ),
                    weight=dict(required=False, type="float"),
                    max_weight=dict(required=False, type="int"),
                    weight_unit=dict(
                        required=False,
                        type="str",
                        choices=[
                            "kg",
                            "g",
                            "lb",
                            "oz",
                        ],
                    ),
                    mounting_depth=dict(required=False, type="int"),
                    description=dict(required=False, type="str"),
                    comments=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [("state", "present", ["model"]), ("state", "absent", ["model"])]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_rack_type = NetboxDcimModule(module, NB_RACK_TYPES)
    netbox_rack_type.run()


if __name__ == "__main__":  # pragma: no cover
    main()

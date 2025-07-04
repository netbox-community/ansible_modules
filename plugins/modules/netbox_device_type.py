#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Mikhail Yohman (@FragmentedPacket) <mikhail.yohman@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_device_type
short_description: Create, update or delete device types within NetBox
description:
  - Creates, updates or removes device types from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Mikhail Yohman (@FragmentedPacket)
requirements:
  - pynetbox
version_added: '0.1.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    description:
      - Defines the device type configuration
    suboptions:
      manufacturer:
        description:
          - The manufacturer of the device type
        required: false
        type: raw
      model:
        description:
          - The model of the device type
        required: true
        type: raw
      slug:
        description:
          - The slug of the device type. Must follow slug formatting (URL friendly)
          - If not specified, it will slugify the model
          - ex. test-device-type
        required: false
        type: str
      part_number:
        description:
          - The part number of the device type
        required: false
        type: str
      u_height:
        description:
          - The height of the device type in rack units
        required: false
        type: float
      weight:
        description:
          - The weight of the device type
        required: false
        type: float
        version_added: "3.10.0"
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
        version_added: "3.10.0"
      is_full_depth:
        description:
          - Whether or not the device consumes both front and rear rack faces
        required: false
        type: bool
      airflow:
        description:
          - Airflow of the device
        choices:
          - front-to-rear
          - rear-to-front
          - left-to-right
          - right-to-left
          - side-to-rear
          - passive
          - mixed
        required: false
        type: str
        version_added: "3.10.0"
      subdevice_role:
        description:
          - Whether the device type is parent, child, or neither
        choices:
          - Parent
          - parent
          - Child
          - child
        required: false
        type: str
      description:
        description:
          - Description of the provider
        required: false
        type: str
        version_added: "3.10.0"
      comments:
        description:
          - Comments that may include additional information in regards to the device_type
        required: false
        type: str
      default_platform:
        description:
          - Set the default platform used by the device
        required: false
        type: raw
        version_added: "3.15.0"
      tags:
        description:
          - Any tags that the device type may need to be associated with
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
    - name: Create device type within NetBox with only required information
      netbox.netbox.netbox_device_type:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          slug: test-device-type
          model: ws-test-3750
          manufacturer: Test Manufacturer
        state: present

    - name: Create device type within NetBox with more information
      netbox.netbox.netbox_device_type:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          slug: test-device-type
          model: ws-test-3750
          manufacturer: Test Manufacturer
          part_number: ws-3750g-v2
          u_height: 1.5
          is_full_depth: false
          subdevice_role: parent
        state: present

    - name: Delete device type within netbox
      netbox.netbox.netbox_device_type:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          slug: test-device-type
        state: absent
"""

RETURN = r"""
device_type:
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
    NB_DEVICE_TYPES,
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
                    part_number=dict(required=False, type="str"),
                    u_height=dict(required=False, type="float"),
                    weight=dict(required=False, type="float"),
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
                    is_full_depth=dict(required=False, type="bool"),
                    airflow=dict(
                        required=False,
                        type="str",
                        choices=[
                            "front-to-rear",
                            "rear-to-front",
                            "left-to-right",
                            "right-to-left",
                            "side-to-rear",
                            "passive",
                            "mixed",
                        ],
                    ),
                    subdevice_role=dict(
                        required=False,
                        choices=["Parent", "parent", "Child", "child"],
                        type="str",
                    ),
                    description=dict(required=False, type="str"),
                    comments=dict(required=False, type="str"),
                    default_platform=dict(required=False, type="raw"),
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

    netbox_device_type = NetboxDcimModule(module, NB_DEVICE_TYPES)
    netbox_device_type.run()


if __name__ == "__main__":  # pragma: no cover
    main()

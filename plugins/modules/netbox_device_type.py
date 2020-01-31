#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Mikhail Yohman (@FragmentedPacket) <mikhail.yohman@gmail.com>
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
module: netbox_device_type
short_description: Create, update or delete device types within Netbox
description:
  - Creates, updates or removes device types from Netbox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Mikhail Yohman (@FragmentedPacket)
requirements:
  - pynetbox
version_added: '0.1.0'
options:
  netbox_url:
    description:
      - URL of the Netbox instance resolvable by Ansible control host
    required: true
  netbox_token:
    description:
      - The token created within Netbox to authorize API access
    required: true
  data:
    description:
      - Defines the device type configuration
    suboptions:
      manufacturer:
        description:
          - The manufacturer of the device type
        required: true
      model:
        description:
          - The model of the device type
        required: true
      slug:
        description:
          - The slug of the device type. Must follow slug formatting (URL friendly)
          - If not specified, it will slugify the model
          - ex. test-device-type
        required: false
      part_number:
        description:
          - The part number of the device type
      u_height:
        description:
          - The height of the device type in rack units
      is_full_depth:
        description:
          - Whether or not the device consumes both front and rear rack faces
        type: bool
      subdevice_role:
        description:
          - Whether the device type is parent, child, or neither
        choices:
          - Parent
          - Child
      comments:
        description:
          - Comments that may include additional information in regards to the device_type
      tags:
        description:
          - Any tags that the device type may need to be associated with
      custom_fields:
        description:
          - must exist in Netbox
    required: true
  state:
    description:
      - Use C(present) or C(absent) for adding or removing.
    choices: [ absent, present ]
    default: present
  validate_certs:
    description:
      - If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
    default: 'yes'
    type: bool
"""

EXAMPLES = r"""
- name: "Test Netbox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create device type within Netbox with only required information
      netbox_device_type:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          slug: test-device-type
          model: ws-test-3750
          manufacturer: Test Manufacturer
        state: present

    - name: Create device type within Netbox with only required information
      netbox_device_type:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          slug: test-device-type
          model: ws-test-3750
          manufacturer: Test Manufacturer
          part_number: ws-3750g-v2
          u_height: 1
          is_full_depth: False
          subdevice_role: parent
        state: present

    - name: Delete device type within netbox
      netbox_device_type:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          slug: test-device-type
        state: absent
"""

RETURN = r"""
device_type:
  description: Serialized object as created or already existent within Netbox
  returned: success (when I(state=present))
  type: dict
msg:
  description: Message indicating failure or info about what has been achieved
  returned: always
  type: str
"""

from ansible_collections.netbox_community.ansible_modules.plugins.module_utils.netbox_utils import (
    NetboxAnsibleModule,
    NETBOX_ARG_SPEC,
)
from ansible_collections.netbox_community.ansible_modules.plugins.module_utils.netbox_dcim import (
    NetboxDcimModule,
    NB_DEVICE_TYPES,
)


def main():
    """
    Main entry point for module execution
    """
    argument_spec = NETBOX_ARG_SPEC
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
                    u_height=dict(required=False, type="int"),
                    is_full_depth=dict(required=False, type="bool"),
                    subdevice_role=dict(
                        required=False, choices=["Parent", "parent", "Child", "child"]
                    ),
                    comments=dict(required=False, type="str"),
                    tags=dict(required=False, type=list),
                    custom_fields=dict(required=False, type=dict),
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


if __name__ == "__main__":
    main()

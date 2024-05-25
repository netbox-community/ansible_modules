#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Erwan TONNERRE (@etonnerre) <erwan.tonnerre@thalesgroup.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_module
short_description: Create, update or delete module within NetBox
description:
  - Creates, updates or removes module from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Erwan TONNERRE (@etonnerre)
requirements:
  - pynetbox
version_added: '3.18.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    description:
      - Defines the device type configuration
    suboptions:
      device:
        description:
          - The device of the module
        required: true
        type: raw
      module_bay:
        description:
          - The module bay of the module
        required: true
        type: raw
      module_type:
        description:
          - The module type of the module
        required: true
        type: raw
      status:
        description:
          - The status of the module
        choices:
          - offline
          - active
          - planned
          - staged
          - side-to-rear
          - failed
          - decommissioning
        required: false
        type: str
      serial:
        description:
          - The weight of the device type
        required: false
        type: str
      description:
        description:
          - The description of the module
        required: false
        type: str
      asset_tag:
        description:
          - The asset tag of the modyle
        required: false
        type: str
      comments:
        description:
          - Comments that may include additional information in regards to the module
        required: false
        type: str
      tags:
        description:
          - Any tags that the module may need to be associated with
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
    - name: Create module type within NetBox with only required information
      netbox.netbox.netbox_module:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: C9300-DEMO
          module_bay: Network Module
          module_type: C9300-NM-8X
        state: present

    - name: Create module type within NetBox
      netbox.netbox.netbox_module:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device:
            name: C9300-DEMO
            site: EUPARIS
          module_bay:
            name: Network Module
            position: 1
          module_type:
            manufacturer: Cisco
            model: C9300-NM-8X
        state: present

    - name: Delete module type within netbox
      netbox.netbox.netbox_module:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: C9300-DEMO
          module_bay: Network Module
          module_type: C9300-NM-8X
          asset_tag: "00001"
          serial: XXXNNNNXXXX
        state: absent
"""

RETURN = r"""
module:
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
    NB_MODULES,
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
                    device=dict(required=True, type="raw"),
                    module_bay=dict(required=True, type="raw"),
                    module_type=dict(required=True, type="raw"),
                    status=dict(
                        required=False,
                        type="str",
                        choices=[
                            "offline",
                            "active",
                            "planned",
                            "staged",
                            "side-to-rear",
                            "failed",
                            "decommissioning",
                        ],
                    ),
                    serial=dict(required=False, type="str"),
                    description=dict(required=False, type="str"),
                    asset_tag=dict(required=False, type="str"),
                    comments=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )
    required_if = [
        ("state", "present", ["device", "module_bay", "module_type", "status"]),
        ("state", "absent", ["device", "module_bay", "module_type"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_device_type = NetboxDcimModule(module, NB_MODULES)
    netbox_device_type.run()


if __name__ == "__main__":  # pragma: no cover
    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2023, Jeff Groom (@jgroom33) <jgroom@ciena.com>
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
  - Jeff Groom (@jgroom33)
requirements:
  - pynetbox
version_added: '3.13.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    description:
      - Defines the module configuration
    suboptions:
      device:
        description:
          - The device name of the module
        required: true
        type: raw
      module_bay:
        description:
          - The module bay name of the module
        required: true
        type: raw
      module_type:
        description:
          - The module type model of the module
        required: true
        type: string
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
  gather_facts: False

  tasks:
    - name: Create module within NetBox with only required information
      netbox.netbox.netbox_module:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          module_bay: ws-test-3750-slot-0
        state: present

    - name: Delete module within netbox
      netbox.netbox.netbox_module:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          module_bay: ws-test-3750-slot-0
        state: absent
"""

RETURN = r"""
module_type:
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
                    device=dict(required=False, type="raw"),
                    module_bay=dict(required=False, type="raw"),
                    module_type=dict(required=False, type="raw"),
                    status=dict(required=False, type="raw"),
                    serial=dict(required=False, type="str"),
                    asset_tag=dict(required=True, type="str"),
                    description=dict(required=False, type="str"),
                    comments=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["asset_tag", "device", "module_bay", "module_type"]),
        ("state", "absent", ["asset_tag"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_module = NetboxDcimModule(module, NB_MODULES)
    netbox_module.run()


if __name__ == "__main__":  # pragma: no cover
    main()

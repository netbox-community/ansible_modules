#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Martin Rødvand (@rodvand)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_virtual_disk
short_description: Creates or removes disks from virtual machines in NetBox
description:
  - Creates or removes disks from virtual machines in NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Martin Rødvand (@rodvand)
requirements:
  - pynetbox
version_added: "3.17.0"
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    description:
      - Defines the vm disk configuration
    suboptions:
      virtual_machine:
        description:
          - Name of the virtual machine the disk will be associated with (case-sensitive)
        required: false
        type: raw
      name:
        description:
          - Name of the disk to be created
        required: true
        type: str
      description:
        description:
          - The description of the disk
        required: false
        type: str
      size:
        description:
          - The size (in GB) of the disk
        required: false
        type: int
      tags:
        description:
          - Any tags that the virtual disk may need to be associated with
        required: false
        type: list
        elements: raw
      custom_fields:
        description:
          - Must exist in NetBox
        required: false
        type: dict
    required: true
    type: dict
"""

EXAMPLES = r"""
- name: "Test NetBox virtual disk module"
  connection: local
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Create virtual disk
      netbox_virtual_disk:
        data:
          virtual_machine: test100
          name: disk0
          size: 50
        state: present
"""

RETURN = r"""
virtual_disk:
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_virtualization import (
    NetboxVirtualizationModule,
    NB_VIRTUAL_DISKS,
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
                    virtual_machine=dict(required=False, type="raw"),
                    name=dict(required=True, type="str"),
                    description=dict(required=False, type="str"),
                    size=dict(required=False, type="int"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["virtual_machine", "name"]),
        ("state", "absent", ["virtual_machine", "name"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_virtual_disk = NetboxVirtualizationModule(module, NB_VIRTUAL_DISKS)
    netbox_virtual_disk.run()


if __name__ == "__main__":  # pragma: no cover
    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Benjamin Vergnaud (@bvergnaud)
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
module: netbox_vm_interface
short_description: Creates or removes interfaces from virtual machines in NetBox
description:
  - Creates or removes interfaces from virtual machines in NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Benjamin Vergnaud (@bvergnaud)
requirements:
  - pynetbox
version_added: "0.1.0"
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    description:
      - Defines the vm interface configuration
    suboptions:
      virtual_machine:
        description:
          - Name of the virtual machine the interface will be associated with (case-sensitive)
        required: false
        type: raw
      name:
        description:
          - Name of the interface to be created
        required: true
        type: str
      enabled:
        description:
          - Sets whether interface shows enabled or disabled
        required: false
        type: bool
      mtu:
        description:
          - The MTU of the interface
        required: false
        type: int
      mac_address:
        description:
          - The MAC address of the interface
        required: false
        type: str
      description:
        description:
          - The description of the interface
        required: false
        type: str
      mode:
        description:
          - The mode of the interface
        required: false
        type: raw
      parent_vm_interface:
        description:
          - The virtual machine interface's parent interface.
        required: false
        type: raw
        version_added: "3.2.0"
      untagged_vlan:
        description:
          - The untagged VLAN to be assigned to interface
        required: false
        type: raw
      tagged_vlans:
        description:
          - A list of tagged VLANS to be assigned to interface. Mode must be set to either C(Tagged) or C(Tagged All)
        required: false
        type: raw
      tags:
        description:
          - Any tags that the prefix may need to be associated with
        required: false
        type: list
        elements: raw
      custom_fields:
        description:
          - Must exist in NetBox
        required: false
        type: dict
        version_added: "3.4.0"
    required: true
    type: dict
"""

EXAMPLES = r"""
- name: "Test NetBox interface module"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create interface within NetBox with only required information
      netbox_vm_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          virtual_machine: test100
          name: GigabitEthernet1
        state: present

    - name: Delete interface within netbox
      netbox_vm_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          virtual_machine: test100
          name: GigabitEthernet1
        state: absent

    - name: Create interface as a trunk port
      netbox_vm_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          virtual_machine: test100
          name: GigabitEthernet25
          enabled: false
          untagged_vlan:
            name: Wireless
            site: Test Site
          tagged_vlans:
            - name: Data
              site: Test Site
            - name: VoIP
              site: Test Site
          mtu: 1600
          mode: Tagged
        state: present
"""

RETURN = r"""
interface:
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
    NB_VM_INTERFACES,
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
                    enabled=dict(required=False, type="bool"),
                    mtu=dict(required=False, type="int"),
                    mac_address=dict(required=False, type="str"),
                    description=dict(required=False, type="str"),
                    mode=dict(required=False, type="raw"),
                    parent_vm_interface=dict(required=False, type="raw"),
                    untagged_vlan=dict(required=False, type="raw"),
                    tagged_vlans=dict(required=False, type="raw"),
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

    netbox_vm_interface = NetboxVirtualizationModule(module, NB_VM_INTERFACES)
    netbox_vm_interface.run()


if __name__ == "__main__":  # pragma: no cover
    main()

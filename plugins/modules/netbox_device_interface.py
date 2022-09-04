#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Mikhail Yohman (@FragmentedPacket) <mikhail.yohman@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_device_interface
short_description: Creates or removes interfaces on devices from NetBox
description:
  - Creates or removes interfaces from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Mikhail Yohman (@FragmentedPacket)
requirements:
  - pynetbox
version_added: "0.1.0"
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    description:
      - Defines the interface configuration
    suboptions:
      device:
        description:
          - Name of the device the interface will be associated with (case-sensitive)
        required: false
        type: raw
      name:
        description:
          - Name of the interface to be created
        required: true
        type: str
      label:
        description:
          - Physical label of the interface
        required: false
        type: str
      form_factor:
         description:
           - |
             Form factor of the interface:
             ex. 1000Base-T (1GE), Virtual, 10GBASE-T (10GE)
             This has to be specified exactly as what is found within UI
         required: false
         type: raw
      type:
        description:
          - |
            Form factor of the interface:
            ex. 1000Base-T (1GE), Virtual, 10GBASE-T (10GE)
            This has to be specified exactly as what is found within UI
        required: false
        type: str
      enabled:
        description:
          - Sets whether interface shows enabled or disabled
        required: false
        type: bool
      lag:
        description:
          - Parent LAG interface will be a member of
        required: false
        type: raw
      bridge:
        description:
          - Bridge the interface will connected to
        required: false
        type: raw
        version_added: "3.6.0" 
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
      mgmt_only:
        description:
          - This interface is used only for out-of-band management
        required: false
        type: bool
      poe_mode:
        description:
          - This interface has PoE ability (NetBox release 3.3 and later)
        required: false
        type: raw
        version_added: "3.8.0"
      poe_type:
        description:
          - This interface's power type (NetBox release 3.3 and later)
        required: false
        type: raw
        version_added: "3.8.0"
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
      vrf:
        description:
          - The VRF of the interface
        required: false
        type: raw
        version_added: "3.7.0"
      speed:
        description:
          - The speed of the interface
        required: false
        type: int
        version_added: "3.7.0"
      duplex:
        description:
          - The duplex of the interface
        required: false
        choices:
          - half
          - full
          - auto
        type: str
        version_added: "3.7.0"
      parent_interface:
        description:
          - The device's parent interface
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
          - Any tags that the interface may need to be associated with
        required: false
        type: list
        elements: raw
      mark_connected:
        description:
          - Mark an interface as connected without a cable attached (netbox >= 2.11 required)
        required: false
        type: bool
      custom_fields:
        description:
          - must exist in NetBox
        required: false
        type: dict
    required: true
    type: dict
  update_vc_child:
    type: bool
    default: False
    description:
      - |
        Use when master device is specified for C(device) and the specified interface exists on a child device
        and needs updated
"""

EXAMPLES = r"""
- name: "Test NetBox interface module"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create interface within NetBox with only required information
      netbox_device_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: test100
          name: GigabitEthernet1
        state: present
    - name: Delete interface within netbox
      netbox_device_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: test100
          name: GigabitEthernet1
        state: absent
    - name: Create LAG with several specified options
      netbox_device_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: test100
          name: port-channel1
          type: Link Aggregation Group (LAG)
          mtu: 1600
          mgmt_only: false
          mode: Access
        state: present
    - name: Create interface and assign it to parent LAG
      netbox_device_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: test100
          name: GigabitEthernet1
          enabled: false
          type: 1000Base-t (1GE)
          lag:
            name: port-channel1
          mtu: 1600
          mgmt_only: false
          mode: Access
        state: present
    - name: Create interface as a trunk port
      netbox_device_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: test100
          name: GigabitEthernet25
          enabled: false
          type: 1000Base-t (1GE)
          untagged_vlan:
            name: Wireless
            site: Test Site
          tagged_vlans:
            - name: Data
              site: Test Site
            - name: VoIP
              site: Test Site
          mtu: 1600
          mgmt_only: true
          mode: Tagged
        state: present
    - name: Update interface on child device on virtual chassis
      netbox_device_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: test100
          name: GigabitEthernet2/0/1
          enabled: false
        update_vc_child: True
    - name: Mark interface as connected without a cable (netbox >= 2.11 required)
      netbox.netbox.netbox_device_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: test100
          name: GigabitEthernet1
          mark_connected: true
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_dcim import (
    NetboxDcimModule,
    NB_INTERFACES,
)
from copy import deepcopy


def main():
    """
    Main entry point for module execution
    """
    argument_spec = deepcopy(NETBOX_ARG_SPEC)
    argument_spec.update(
        dict(
            update_vc_child=dict(type="bool", required=False, default=False),
            data=dict(
                type="dict",
                required=True,
                options=dict(
                    device=dict(required=False, type="raw"),
                    name=dict(required=True, type="str"),
                    form_factor=dict(
                        required=False,
                        type="raw",
                        removed_in_version="4.0.0",
                        removed_from_collection="netbox.netbox",
                    ),
                    label=dict(required=False, type="str"),
                    type=dict(required=False, type="str"),
                    enabled=dict(required=False, type="bool"),
                    lag=dict(required=False, type="raw"),
                    bridge=dict(required=False, type="raw"),
                    mtu=dict(required=False, type="int"),
                    mac_address=dict(required=False, type="str"),
                    mgmt_only=dict(required=False, type="bool"),
                    poe_type=dict(required=False, type="raw"),
                    poe_mode=dict(required=False, type="raw"),
                    description=dict(required=False, type="str"),
                    mode=dict(required=False, type="raw"),
                    vrf=dict(required=False, type="raw"),
                    speed=dict(required=False, type="int"),
                    duplex=dict(
                        required=False, choices=["half", "full", "auto"], type="str"
                    ),
                    parent_interface=dict(required=False, type="raw"),
                    untagged_vlan=dict(required=False, type="raw"),
                    tagged_vlans=dict(required=False, type="raw"),
                    tags=dict(required=False, type="list", elements="raw"),
                    mark_connected=dict(required=False, type="bool"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["device", "name"]),
        ("state", "absent", ["device", "name"]),
        ("update_vc_child", True, ["device"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_device_interface = NetboxDcimModule(module, NB_INTERFACES)
    netbox_device_interface.run()


if __name__ == "__main__":  # pragma: no cover
    main()

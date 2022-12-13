#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Martin Rødvand (@rodvand)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_wireless_link
short_description: Creates or removes Wireless links from NetBox
description:
  - Creates or removes wireless links from NetBox
notes:  
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Martin Rødvand (@rodvand)
requirements:
  - pynetbox
version_added: "3.5.0"
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the wireless link configuration
    suboptions:
      interface_a:
        description:
          - Interface A of the wireless link
        required: true
        type: raw
      interface_b:
        description:
          - Interface A of the wireless link
        required: true
        type: raw
      ssid:
        description:
          - The SSID of the wireless link
        required: false
        type: str
      description:
        description:
          - Description of the wireless link
        required: false
        type: str    
      status:
        description:
          - The status of the wireless link
        choices:
          - connected
          - planned
          - decommissioning
        required: false
        type: str          
      auth_type:
        description:
          - The authentication type of the wireless link
        choices:
          - open
          - wep
          - wpa-personal
          - wpa-enterprise
        required: false
        type: str
      auth_cipher:
        description:
          - The authentication cipher of the wireless link
        choices:
          - auto
          - tkip
          - aes
        required: false
        type: str
      auth_psk:
        description:
          - The PSK of the wireless link
        required: false
        type: str    
      comments:
        description:
          - Comments of the wireless link
        required: false
        type: str
        version_added: "3.10.0"
      tags:
        description:
          - Any tags that the wireless link may need to be associated with
        required: false
        type: list
        elements: raw
      custom_fields:
        description:
          - must exist in NetBox
        required: false
        type: dict    
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox module"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create wireless link within NetBox with only required information
      netbox_wireless_link:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          interface_a:
            device: Device One
            name: wireless_link_0
          interface_b:
            device: Device Two
            name: wireless_link_0
        state: present

    - name: Delete wireless link within netbox
      netbox_wireless_link:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          interface_a:
            device: Device One
            name: wireless_link_0
          interface_b:
            device: Device Two
            name: wireless_link_0
        state: absent

    - name: Create wireless link with all parameters
      netbox_wireless_link:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          interface_a:
            device: Device One
            name: wireless_link_0
          interface_b:
            device: Device Two
            name: wireless_link_0
          ssid: Wireless Network One          
          description: Cool Wireless Network
          auth_type: wpa-enterprise
          auth_cipher: aes
          auth_psk: psk123456                    
          tags:
            - tagA
            - tagB
            - tagC
        state: present
"""

RETURN = r"""
wireless_link:
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_wireless import (
    NetboxWirelessModule,
    NB_WIRELESS_LINKS,
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
                    interface_a=dict(required=True, type="raw"),
                    interface_b=dict(required=True, type="raw"),
                    ssid=dict(required=False, type="str"),
                    status=dict(
                        required=False,
                        choices=["connected", "planned", "decommissioning"],
                        type="str",
                    ),
                    description=dict(required=False, type="str"),
                    auth_type=dict(
                        required=False,
                        choices=["open", "wep", "wpa-enterprise", "wpa-personal"],
                        type="str",
                    ),
                    auth_cipher=dict(
                        required=False, choices=["auto", "tkip", "aes"], type="str"
                    ),
                    comments=dict(required=False, type="str"),
                    auth_psk=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["interface_a", "interface_b"]),
        ("state", "absent", ["interface_a", "interface_b"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_wireless_link = NetboxWirelessModule(module, NB_WIRELESS_LINKS)
    netbox_wireless_link.run()


if __name__ == "__main__":  # pragma: no cover
    main()

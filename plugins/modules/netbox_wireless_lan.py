#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Martin Rødvand (@rodvand)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_wireless_lan
short_description: Creates or removes Wireless LANs from NetBox
description:
  - Creates or removes wireless LANs from NetBox
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
      - Defines the contact configuration
    suboptions:
      ssid:
        description:
          - Name of the SSID to be created
        required: true
        type: str
      description:
        description:
          - The description of the Wireless LAN
        required: false
        type: str
      wireless_lan_group:
        description:
          - The wireless LAN group
        required: false
        type: raw
      status:
        description:
          - Status of the wireless LAN
        required: false
        type: raw
      vlan:
        description:
          - The VLAN of the Wireless LAN
        required: false
        type: raw
      auth_type:
        description:
          - The authentication type of the Wireless LAN
        choices:
          - open
          - wep
          - wpa-personal
          - wpa-enterprise
        required: false
        type: str
      auth_cipher:
        description:
          - The authentication cipher of the Wireless LAN
        choices:
          - auto
          - tkip
          - aes
        required: false
        type: str
      auth_psk:
        description:
          - The PSK of the Wireless LAN
        required: false
        type: str
      tags:
        description:
          - Any tags that the Wireless LAN may need to be associated with
        required: false
        type: list
        elements: raw
      custom_fields:
        description:
          - must exist in NetBox
        required: false
        type: dict
      comments:
        description:
          - Comments of the wireless LAN
        required: false
        type: str
        version_added: "3.10.0"
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox module"
  connection: local
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Create Wireless LAN within NetBox with only required information
      netbox_wireless_lan:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          ssid: Wireless Network One
        state: present

    - name: Delete Wireless LAN within netbox
      netbox_wireless_lan:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          ssid: Wireless Network One
        state: absent

    - name: Create Wireless LAN with all parameters
      netbox_wireless_lan:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
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
wireless_lan:
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
    NB_WIRELESS_LANS,
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
                    ssid=dict(required=True, type="str"),
                    description=dict(required=False, type="str"),
                    wireless_lan_group=dict(required=False, type="raw"),
                    status=dict(required=False, type="raw"),
                    vlan=dict(required=False, type="raw"),
                    auth_type=dict(
                        required=False,
                        choices=["open", "wep", "wpa-enterprise", "wpa-personal"],
                        type="str",
                    ),
                    auth_cipher=dict(
                        required=False, choices=["auto", "tkip", "aes"], type="str"
                    ),
                    auth_psk=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                    comments=dict(required=False, type="str"),
                ),
            ),
        )
    )

    required_if = [("state", "present", ["ssid"]), ("state", "absent", ["ssid"])]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_wireless_lan = NetboxWirelessModule(module, NB_WIRELESS_LANS)
    netbox_wireless_lan.run()


if __name__ == "__main__":  # pragma: no cover
    main()

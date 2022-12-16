#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2020 Nokia
# Licensed under the GNU General Public License v3.0 only
# SPDX-License-Identifier: GPL-3.0-only

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_power_panel
short_description: Create, update or delete power panels within NetBox
description:
  - Creates, updates or removes power panels from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Tobias Groß (@toerb)
requirements:
  - pynetbox
version_added: '0.2.3'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    required: true
    description:
      - Defines the power panel configuration
    suboptions:
      site:
        description:
          - The site the power panel is located in
        required: true
        type: raw
      rack_group:
        description:
          - The rack group the power panel is assigned to (NetBox < 2.11)
          - Will be removed in version 5.0.0
        required: false
        type: raw
      location:
        description:
          - The location the power panel is assigned to (NetBox 2.11+)
        required: false
        type: raw
        version_added: "3.1.0"
      name:
        description:
          - The name of the power panel
        required: true
        type: str
      description:
        description:
          - Description of the power panel
        required: false
        type: str
        version_added: "3.10.0"
      comments:
        description:
          - Comments related to the power panel
        required: false
        type: str
        version_added: "3.10.0"
      custom_fields:
        description:
          - Must exist in NetBox
        required: false
        type: dict
        version_added: "3.6.0"
      tags:
        description:
          - The tags to add/update
        required: false
        type: list
        elements: raw
        version_added: "3.6.0"
"""

EXAMPLES = r"""
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create power panel within NetBox with only required information
      netbox.netbox.netbox_power_panel:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Panel
          site: Test Site
        state: present

    - name: Update power panel with other fields - Pre 2.11
      netbox.netbox.netbox_power_panel:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Panel
          site: Test Site
          rack_group: Test Rack Group
        state: present

    - name: Create power panel within NetBox with only required information - Post 2.11
      netbox.netbox.netbox_power_panel:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Panel
          site: Test Site
          location: Test Location
        state: present

    - name: Delete power panel within netbox
      netbox.netbox.netbox_power_panel:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Panel
          site: Test Site
        state: absent
"""

RETURN = r"""
power_panel:
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
    NB_POWER_PANELS,
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
                    site=dict(required=True, type="raw"),
                    rack_group=dict(
                        required=False,
                        type="raw",
                        removed_in_version="5.0.0",
                        removed_from_collection="netbox.netbox",
                    ),
                    location=dict(required=False, type="raw"),
                    name=dict(required=True, type="str"),
                    description=dict(required=False, type="str"),
                    comments=dict(required=False, type="str"),
                    custom_fields=dict(required=False, type="dict"),
                    tags=dict(required=False, type="list", elements="raw"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["site", "name"]),
        ("state", "absent", ["site", "name"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_power_panel = NetboxDcimModule(module, NB_POWER_PANELS)
    netbox_power_panel.run()


if __name__ == "__main__":  # pragma: no cover
    main()

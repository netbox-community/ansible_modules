#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2020 Nokia
# Licensed under the GNU General Public License v3.0 only
# SPDX-License-Identifier: GPL-3.0-only

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_power_feed
short_description: Create, update or delete power feeds within NetBox
description:
  - Creates, updates or removes power feeds from NetBox
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
      - Defines the power feed configuration
    suboptions:
      power_panel:
        description:
          - The power panel the power feed is terminated on
        required: true
        type: raw
      rack:
        description:
          - The rack the power feed is assigned to
        required: false
        type: raw
      name:
        description:
          - The name of the power feed
        required: true
        type: str
      status:
        description:
          - The status of the power feed
        choices:
          - offline
          - active
          - planned
          - failed
        required: false
        type: str
      type:
        description:
          - The type of the power feed
        choices:
          - primary
          - redundant
        required: false
        type: str
      supply:
        description:
          - The supply type of the power feed
        choices:
          - ac
          - dc
        required: false
        type: str
      phase:
        description:
          - The phase type of the power feed
        choices:
          - single-phase
          - three-phase
        required: false
        type: str
      voltage:
        description:
          - The voltage of the power feed
        required: false
        type: int
      amperage:
        description:
          - The amperage of the power feed
        required: false
        type: int
      max_utilization:
        description:
          - The maximum permissible draw of the power feed in percent
        required: false
        type: int
      description:
        description:
          - Description of the power feed
        required: false
        type: str
        version_added: "3.10.0"
      comments:
        description:
          - Comments related to the power feed
        required: false
        type: str
      tags:
        description:
          - Any tags that the power feed may need to be associated with
        required: false
        type: list
        elements: raw
      custom_fields:
        description:
          - must exist in NetBox
        required: false
        type: dict
"""

EXAMPLES = r"""
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create power feed within NetBox with only required information
      netbox.netbox.netbox_power_feed:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Feed
          power_panel: Test Power Panel
        state: present

    - name: Update power feed with other fields
      netbox.netbox.netbox_power_feed:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Feed
          power_panel: Test Power Panel
          status: offline
          type: primary
          supply: ac
          phase: single-phase
          voltage: 230
          amperage: 16
          max_utilization: 80
          comments: normal power feed
        state: present

    - name: Delete power feed within netbox
      netbox.netbox.netbox_power_feed:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Power Feed
          power_panel: Test Power Panel
        state: absent
"""

RETURN = r"""
power_feed:
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
    NB_POWER_FEEDS,
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
                    power_panel=dict(required=True, type="raw"),
                    rack=dict(required=False, type="raw"),
                    name=dict(required=True, type="str"),
                    status=dict(
                        required=False,
                        choices=["offline", "active", "planned", "failed"],
                        type="str",
                    ),
                    type=dict(
                        required=False, choices=["primary", "redundant"], type="str"
                    ),
                    supply=dict(required=False, choices=["ac", "dc"], type="str"),
                    phase=dict(
                        required=False,
                        choices=["single-phase", "three-phase"],
                        type="str",
                    ),
                    voltage=dict(required=False, type="int"),
                    amperage=dict(required=False, type="int"),
                    max_utilization=dict(required=False, type="int"),
                    description=dict(required=False, type="str"),
                    comments=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["power_panel", "name"]),
        ("state", "absent", ["power_panel", "name"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_power_feed = NetboxDcimModule(module, NB_POWER_FEEDS)
    netbox_power_feed.run()


if __name__ == "__main__":  # pragma: no cover
    main()

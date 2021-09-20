#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2020 Nokia
# Licensed under the GNU General Public License v3.0 only
# SPDX-License-Identifier: GPL-3.0-only

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: netbox_cable
short_description: Create, update or delete cables within Netbox
description:
  - Creates, updates or removes cables from Netbox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Tobias Groß (@toerb)
requirements:
  - pynetbox
version_added: '0.3.0'
options:
  netbox_url:
    description:
      - URL of the Netbox instance resolvable by Ansible control host
    required: true
    type: str
  netbox_token:
    description:
      - The token created within Netbox to authorize API access
    required: true
    type: str
  cert:
    description:
      - Certificate path
    required: false
    type: raw
  data:
    type: dict
    required: true
    description:
      - Defines the cable configuration
    suboptions:
      termination_a_type:
        description:
          - The type of the termination a
        choices:
          - circuits.circuittermination
          - dcim.consoleport
          - dcim.consoleserverport
          - dcim.frontport
          - dcim.interface
          - dcim.powerfeed
          - dcim.poweroutlet
          - dcim.powerport
          - dcim.rearport
        required: true
        type: str
      termination_a:
        description:
          - The termination a
        required: true
        type: raw
      termination_b_type:
        description:
          - The type of the termination b
        choices:
          - circuits.circuittermination
          - dcim.consoleport
          - dcim.consoleserverport
          - dcim.frontport
          - dcim.interface
          - dcim.powerfeed
          - dcim.poweroutlet
          - dcim.powerport
          - dcim.rearport
        required: true
        type: str
      termination_b:
        description:
          - The termination b
        required: true
        type: raw
      type:
        description:
          - The type of the cable
        choices:
          - cat3
          - cat5
          - cat5e
          - cat6
          - cat6a
          - cat7
          - dac-active
          - dac-passive
          - mrj21-trunk
          - coaxial
          - mmf
          - mmf-om1
          - mmf-om2
          - mmf-om3
          - mmf-om4
          - smf
          - smf-os1
          - smf-os2
          - aoc
          - power
        required: false
        type: str
      status:
        description:
          - The status of the cable
        choices:
          - connected
          - planned
          - decommissioning
        required: false
        type: str
      label:
        description:
          - The label of the cable
        required: false
        type: str
      color:
        description:
          - The color of the cable
        required: false
        type: str
      length:
        description:
          - The length of the cable
        required: false
        type: int
      length_unit:
        description:
          - The unit in which the length of the cable is measured
        choices:
          - m
          - cm
          - ft
          - in
        required: false
        type: str
      tags:
        description:
          - Any tags that the cable may need to be associated with
        required: false
        type: list
        elements: raw
  state:
    description:
      - Use C(present) or C(absent) for adding or removing.
    choices: [ absent, present ]
    default: present
    type: str
  query_params:
    description:
      - This can be used to override the specified values in ALLOWED_QUERY_PARAMS that is defined
      - in plugins/module_utils/netbox_utils.py and provides control to users on what may make
      - an object unique in their environment.
    required: false
    type: list
    elements: str
  validate_certs:
    description:
      - If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
    default: true
    type: raw
"""

EXAMPLES = r"""
- name: "Test Netbox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create cable within Netbox with only required information
      netbox_cable:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          termination_a_type: dcim.interface
          termination_a:
            device: Test Nexus Child One
            name: Ethernet2/2
          termination_b_type: dcim.interface
          termination_b:
            device: Test Nexus Child One
            name: Ethernet2/1
        state: present

    - name: Update cable with other fields
      netbox_cable:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          termination_a_type: dcim.interface
          termination_a:
            device: Test Nexus Child One
            name: Ethernet2/2
          termination_b_type: dcim.interface
          termination_b:
            device: Test Nexus Child One
            name: Ethernet2/1
          type: mmf-om4
          status: planned
          label: label123
          color: abcdef
          length: 30
          length_unit: m
          tags:
            - foo
        state: present

    - name: Delete cable within netbox
      netbox_cable:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          termination_a_type: dcim.interface
          termination_a:
            device: Test Nexus Child One
            name: Ethernet2/2
          termination_b_type: dcim.interface
          termination_b:
            device: Test Nexus Child One
            name: Ethernet2/1
        state: absent
"""

RETURN = r"""
cable:
  description: Serialized object as created or already existent within Netbox
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
    NB_CABLES,
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
                    termination_a_type=dict(
                        required=True,
                        choices=[
                            "circuits.circuittermination",
                            "dcim.consoleport",
                            "dcim.consoleserverport",
                            "dcim.frontport",
                            "dcim.interface",
                            "dcim.powerfeed",
                            "dcim.poweroutlet",
                            "dcim.powerport",
                            "dcim.rearport",
                        ],
                        type="str",
                    ),
                    termination_a=dict(required=True, type="raw"),
                    termination_b_type=dict(
                        required=True,
                        choices=[
                            "circuits.circuittermination",
                            "dcim.consoleport",
                            "dcim.consoleserverport",
                            "dcim.frontport",
                            "dcim.interface",
                            "dcim.powerfeed",
                            "dcim.poweroutlet",
                            "dcim.powerport",
                            "dcim.rearport",
                        ],
                        type="str",
                    ),
                    termination_b=dict(required=True, type="raw"),
                    type=dict(
                        required=False,
                        choices=[
                            "cat3",
                            "cat5",
                            "cat5e",
                            "cat6",
                            "cat6a",
                            "cat7",
                            "dac-active",
                            "dac-passive",
                            "mrj21-trunk",
                            "coaxial",
                            "mmf",
                            "mmf-om1",
                            "mmf-om2",
                            "mmf-om3",
                            "mmf-om4",
                            "smf",
                            "smf-os1",
                            "smf-os2",
                            "aoc",
                            "power",
                        ],
                        type="str",
                    ),
                    status=dict(
                        required=False,
                        choices=["connected", "planned", "decommissioning"],
                        type="str",
                    ),
                    label=dict(required=False, type="str"),
                    color=dict(required=False, type="str"),
                    length=dict(required=False, type="int"),
                    length_unit=dict(
                        required=False, choices=["m", "cm", "ft", "in"], type="str"
                    ),
                    tags=dict(required=False, type="list", elements="raw"),
                ),
            ),
        )
    )

    required_if = [
        (
            "state",
            "present",
            [
                "termination_a_type",
                "termination_a",
                "termination_b_type",
                "termination_b",
            ],
        ),
        (
            "state",
            "absent",
            [
                "termination_a_type",
                "termination_a",
                "termination_b_type",
                "termination_b",
            ],
        ),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_cable = NetboxDcimModule(module, NB_CABLES)
    netbox_cable.run()


if __name__ == "__main__":  # pragma: no cover
    main()

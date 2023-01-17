#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Mikhail Yohman (@FragmentedPacket) <mikhail.yohman@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_circuit_termination
short_description: Create, update or delete circuit terminations within NetBox
description:
  - Creates, updates or removes circuit terminations from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Mikhail Yohman (@FragmentedPacket)
requirements:
  - pynetbox
version_added: '0.1.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    required: true
    type: dict
    description:
      - Defines the circuit termination configuration
    suboptions:
      circuit:
        description:
          - The circuit to assign to circuit termination
        required: true
        type: raw
      term_side:
        description:
          - The side of the circuit termination
        choices:
          - A
          - Z
        required: true
        type: str
      mark_connected:
        description: 
          - Treat as if cable is connected
        required: false
        type: bool
        version_added: 3.5.0
      site:
        description:
          - The site the circuit termination will be assigned to
        required: false
        type: raw
      provider_network:
        description:
          - The provider_network the circuit termination will be assigned to
        required: false
        type: raw
      port_speed:
        description:
          - The speed of the port (Kbps)
        required: false
        type: int
      upstream_speed:
        description:
          - The upstream speed of the circuit termination
        required: false
        type: int
      xconnect_id:
        description:
          - The cross connect ID of the circuit termination
        required: false
        type: str
      pp_info:
        description:
          - Patch panel information
        required: false
        type: str
      description:
        description:
          - Description of the circuit termination
        required: false
        type: str
"""

EXAMPLES = r"""
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create circuit termination within NetBox with only required information
      netbox.netbox.netbox_circuit_termination:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          circuit: Test Circuit
          term_side: A
          site: Test Site
          port_speed: 10000
        state: present

    - name: Update circuit termination with other fields
      netbox.netbox.netbox_circuit_termination:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          circuit: Test Circuit
          term_side: A
          upstream_speed: 1000
          xconnect_id: 10X100
          pp_info: PP10-24
          description: "Test description"
        state: present

    - name: Delete circuit termination within netbox
      netbox.netbox.netbox_circuit_termination:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          circuit: Test Circuit
          term_side: A
        state: absent
"""

RETURN = r"""
circuit_termination:
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_circuits import (
    NetboxCircuitsModule,
    NB_CIRCUIT_TERMINATIONS,
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
                    circuit=dict(required=True, type="raw"),
                    term_side=dict(required=True, choices=["A", "Z"]),
                    mark_connected=dict(required=False, type="bool"),
                    site=dict(required=False, type="raw"),
                    provider_network=dict(required=False, type="raw"),
                    port_speed=dict(required=False, type="int"),
                    upstream_speed=dict(required=False, type="int"),
                    xconnect_id=dict(required=False, type="str"),
                    pp_info=dict(required=False, type="str"),
                    description=dict(required=False, type="str"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["circuit", "term_side"]),
        ("state", "absent", ["circuit", "term_side"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_circuit_termination = NetboxCircuitsModule(module, NB_CIRCUIT_TERMINATIONS)
    netbox_circuit_termination.run()


if __name__ == "__main__":  # pragma: no cover
    main()

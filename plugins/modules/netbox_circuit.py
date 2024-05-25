#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Mikhail Yohman (@FragmentedPacket) <mikhail.yohman@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_circuit
short_description: Create, update or delete circuits within NetBox
description:
  - Creates, updates or removes circuits from NetBox
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
    type: dict
    required: true
    description:
      - Defines the circuit configuration
    suboptions:
      cid:
        description:
          - The circuit id of the circuit
        required: true
        type: str
      provider:
        description:
          - The provider of the circuit
        required: false
        type: raw
      circuit_type:
        description:
          - The circuit type of the circuit
        required: false
        type: raw
      status:
        description:
          - The status of the circuit
        required: false
        type: raw
      tenant:
        description:
          - The tenant assigned to the circuit
        required: false
        type: raw
      install_date:
        description:
          - The date the circuit was installed. e.g. YYYY-MM-DD
        required: false
        type: str
      commit_rate:
        description:
          - Commit rate of the circuit (Kbps)
        required: false
        type: int
      description:
        description:
          - Description of the circuit
        required: false
        type: str
      comments:
        description:
          - Comments related to circuit
        required: false
        type: str
      tags:
        description:
          - Any tags that the device may need to be associated with
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
  gather_facts: false

  tasks:
    - name: Create circuit within NetBox with only required information
      netbox.netbox.netbox_circuit:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          cid: Test Circuit
          provider: Test Provider
          circuit_type: Test Circuit Type
        state: present

    - name: Update circuit with other fields
      netbox.netbox.netbox_circuit:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          cid: Test-Circuit-1000
          provider: Test Provider
          circuit_type: Test Circuit Type
          status: Active
          tenant: Test Tenant
          install_date: "2018-12-25"
          commit_rate: 10000
          description: Test circuit
          comments: "FAST CIRCUIT"
        state: present

    - name: Delete circuit within netbox
      netbox.netbox.netbox_circuit:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          cid: Test-Circuit-1000
        state: absent
"""

RETURN = r"""
circuit:
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
    NB_CIRCUITS,
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
                    cid=dict(required=True, type="str"),
                    provider=dict(required=False, type="raw"),
                    circuit_type=dict(required=False, type="raw"),
                    status=dict(required=False, type="raw"),
                    tenant=dict(required=False, type="raw"),
                    install_date=dict(required=False, type="str"),
                    commit_rate=dict(required=False, type="int"),
                    description=dict(required=False, type="str"),
                    comments=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [("state", "present", ["cid"]), ("state", "absent", ["cid"])]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_circuit = NetboxCircuitsModule(module, NB_CIRCUITS)
    netbox_circuit.run()


if __name__ == "__main__":  # pragma: no cover
    main()

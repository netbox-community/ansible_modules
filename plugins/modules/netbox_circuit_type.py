#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Mikhail Yohman (@FragmentedPacket) <mikhail.yohman@gmail.com>
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
module: netbox_circuit_type
short_description: Create, update or delete circuit types within NetBox
description:
  - Creates, updates or removes circuit types from NetBox
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
      - Defines the circuit type configuration
    suboptions:
      name:
        description:
          - The name of the circuit type
        required: true
        type: str
      slug:
        description:
          - The slugified version of the name or custom slug.
          - This is auto-generated following NetBox rules if not provided
        required: false
        type: str
"""

EXAMPLES = r"""
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create type within NetBox with only required information
      netbox_circuit_type:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Circuit Type
        state: present

    - name: Delete circuit type within netbox
      netbox_circuit_type:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Circuit Type
        state: absent
"""

RETURN = r"""
circuit_type:
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
    NB_CIRCUIT_TYPES,
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
                    name=dict(required=True, type="str"),
                    slug=dict(required=False, type="str"),
                ),
            ),
        )
    )

    required_if = [("state", "present", ["name"]), ("state", "absent", ["name"])]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_circuit_type = NetboxCircuitsModule(module, NB_CIRCUIT_TYPES)
    netbox_circuit_type.run()


if __name__ == "__main__":  # pragma: no cover
    main()

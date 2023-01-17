#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2020 Nokia
# Licensed under the GNU General Public License v3.0 only
# SPDX-License-Identifier: GPL-3.0-only

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_virtual_chassis
short_description: Create, update or delete virtual chassis within NetBox
description:
  - Creates, updates or removes virtual chassis from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Tobias Groß (@toerb)
requirements:
  - pynetbox
version_added: '0.3.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    required: true
    description:
      - Defines the virtual chassis configuration
    suboptions:
      name:
        description:
          - Name
        required: false
        type: str
      master:
        description:
          - The master device the virtual chassis is attached to
        required: false
        type: raw
      domain:
        description:
          - domain of the virtual chassis
        required: false
        type: str
      description:
        description:
          - Description of the virtual chassis
        required: false
        type: str
        version_added: "3.10.0"
      comments:
        description:
          - Comments that may include additional information in regards to the virtual chassis
        required: false
        type: str
        version_added: "3.10.0"
      tags:
        description:
          - Any tags that the virtual chassis may need to be associated with
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
    - name: Create virtual chassis within NetBox with only required information
      netbox_virtual_chassis:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "Virtual Chassis 1"
          master: Test Device
        state: present

    - name: Update virtual chassis with other fields
      netbox_virtual_chassis:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "Virtual Chassis 1"
          domain: Domain Text
        state: present

    - name: Delete virtual chassis within netbox
      netbox_virtual_chassis:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "Virtual Chassis 1"
        state: absent
"""

RETURN = r"""
virtual_chassis:
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
    NB_VIRTUAL_CHASSIS,
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
                    name=dict(required=False, type="str"),
                    master=dict(required=False, type="raw"),
                    domain=dict(required=False, type="str"),
                    description=dict(required=False, type="str"),
                    comments=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_one_of = [["name", "master"]]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_one_of=required_one_of,
    )

    netbox_virtual_chassis = NetboxDcimModule(module, NB_VIRTUAL_CHASSIS)
    netbox_virtual_chassis.run()


if __name__ == "__main__":  # pragma: no cover
    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Philipp Rintz (@p-rintz) <git@rintz.net>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_custom_field_choice_set
short_description: Creates, updates or deletes custom field choice sets within Netbox
description:
  - Creates, updates or removes custom fields choice sets from Netbox
notes:
  - This should be run with connection C(local) and hosts C(localhost)
author:
  - Philipp Rintz (@p-rintz)
requirements:
  - pynetbox
version_added: "3.18.0"
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the choice set
    suboptions:
      name:
        description:
          - Name of the choice set
        required: true
        type: str
      description:
        description:
          - Description of the choice set
        required: false
        type: str
      extra_choices:
        description:
          - List of available choices in the choice set
        required: false
        default: []
        type: list
        elements: list
      base_choices:
        description:
         - Selection of base choice to use in the choice set
        required: false
        type: str
        choices:
         - IATA
         - ISO_3166
         - UN_LOCODE
      order_alphabetically:
        description:
          - Order the choices alphabetically
        required: false
        type: bool
    required: true
"""

EXAMPLES = r"""
- name: "Test Netbox custom_field_choice_set module"
  connection: local
  hosts: localhost
  tasks:
    - name: Create a choice set with choices
      netbox.netbox.netbox_custom_field_choice_set:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "ChoiceSetName"
          description: "Choice Set Description"
          extra_choices:
            - ['choice1', 'label1']
            - ['choice2', 'label2']

    - name: Create a choice set with a base choice
      netbox.netbox.netbox_custom_field_choice_set:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "ChoiceSetName"
          description: "Choice Set Description"
          order_alphabetically: true
          base_choices: "IATA"
"""

RETURN = r"""
custom_field_choice_set:
  description: Serialized object as created/existent/updated/deleted within NetBox
  returned: always
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_extras import (
    NetboxExtrasModule,
    NB_CUSTOM_FIELD_CHOICE_SETS,
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
                    description=dict(required=False, type="str"),
                    base_choices=dict(
                        required=False,
                        type="str",
                        choices=[
                            "IATA",
                            "ISO_3166",
                            "UN_LOCODE",
                        ],
                    ),
                    extra_choices=dict(
                        required=False,
                        default=[],
                        type="list",
                        elements="list",
                    ),
                    order_alphabetically=dict(required=False, type="bool"),
                ),
            )
        )
    )

    required_if = [
        ("state", "present", ["name"]),
        ("state", "absent", ["name"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_custom_field_choice_set = NetboxExtrasModule(
        module, NB_CUSTOM_FIELD_CHOICE_SETS
    )
    netbox_custom_field_choice_set.run()


if __name__ == "__main__":  # pragma: no cover
    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Martin Rødvand (@rodvand) <p@tristero.se>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_custom_field
short_description: Creates, updates or deletes custom fields within NetBox
description:
  - Creates, updates or removes custom fields from NetBox
notes:  
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Martin Rødvand (@rodvand)
requirements:
  - pynetbox
version_added: "3.6.0"
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the custom field
    suboptions:
      content_types:
        description:
          - The content type(s) to apply this custom field to
        required: true
        type: list
        elements: raw
      type: 
        description: 
          - The type of custom field
        required: true
        type: raw
      name:
        description:
          - Name of the custom field
        required: true
        type: str
      label:
        description:
          - Label of the custom field
        required: true
        type: str
      description:
        description:
          - Description of the custom field
        required: true
        type: str
      required:
        description:
          - Whether the custom field is required
        required: false
        type: bool
      filter_logic:
        description:
          - Filter logic of the custom field
        required: false
        type: str
      default:
        description:
          - Default value of the custom field
        required: false
        type: raw
      weight:
        description:
          - Fields with higher weights appear lower in a form
        required: false
        type: int
      validation_minimum:
        description:
          - The minimum allowed value (for numeric fields)
        required: false
        type: int
      validation_maximum:
        description:
          - The maximum allowed value (for numeric fields)
        required: false
        type: int
      validation_regex:
        description:
          - The regular expression to enforce on text fields
        required: false
        type: string      
      choices:
        description:
          - List of available choices (for selection fields) 
        required: false
        type: list
        elements: str                                  
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox config_context module"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create config context and apply it to sites euc1-az1, euc1-az2 with the default weight of 1000
      netbox_config_context:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "dns_nameservers-quadnine"
          description: "9.9.9.9"
          data: "{ \"dns\": { \"nameservers\": [ \"9.9.9.9\" ] } }"
          sites: [ euc1-az1, euc1-az2 ]

    - name: Detach config context from euc1-az1, euc1-az2 and attach to euc1-az3
      netbox_config_context:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "dns_nameservers-quadnine"
          data: "{ \"dns\": { \"nameservers\": [ \"9.9.9.9\" ] } }"
          sites: [ euc1-az3 ]

    - name: Delete config context
      netbox_config_context:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "dns_nameservers-quadnine"
          data: "{ \"dns\": { \"nameservers\": [ \"9.9.9.9\" ] } }"
        state: absent
"""

RETURN = r"""
custom_field:
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
    NB_CUSTOM_FIELDS,
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
                    content_types=dict(required=True, type="list", elements="raw"),
                    type=dict(required=True, type="raw"),
                    name=dict(required=False, type="str"),
                    label=dict(required=False, type="str"),
                    description=dict(required=False, type="str"),
                    required=dict(required=False, type="bool"),
                    filter_logic=dict(required=False, type="raw"),
                    default=dict(required=False, type="raw"),
                    weight=dict(required=False, type="int"),
                    validation_minimum=dict(required=False, type="int"),
                    validation_maximum=dict(required=False, type="int"),
                    validation_regex=dict(required=False, type="str"),
                    choices=dict(required=False, type="list", elements="str"),
                ),
            )
        )
    )

    required_if = [
        ("state", "present", ["content_types", "name"]),
        ("state", "absent", ["name"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_custom_field = NetboxExtrasModule(module, NB_CUSTOM_FIELDS)
    netbox_custom_field.run()


if __name__ == "__main__":  # pragma: no cover
    main()

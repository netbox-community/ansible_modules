#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Martin Rødvand (@rodvand) <martin@rodvand.net>
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
        required: false
        type: list
        elements: raw
      object_types:
        description:
          - The content type(s) to apply this custom field to (NetBox 4.0+)
        required: false
        type: list
        elements: raw
        version_added: "3.19.0"
      type:
        description:
          - The type of custom field
        required: false
        choices:
          - text
          - longtext
          - integer
          - decimal
          - boolean
          - date
          - datetime
          - url
          - json
          - select
          - multiselect
          - object
          - multiobject
        type: str
      object_type:
        description:
          - The object type of the custom field (if any)
        required: false
        type: str
        version_added: "3.7.0"
      related_object_type:
        description:
          - The object type of the custom field (if any) (NetBox 4.0+)
        required: false
        type: str
        version_added: "3.20.0"
      name:
        description:
          - Name of the custom field
        required: true
        type: str
      label:
        description:
          - Label of the custom field
        required: false
        type: str
      description:
        description:
          - Description of the custom field
        required: false
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
        type: raw
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
      search_weight:
        description:
          - Weighting for search. Lower values are considered more important. Fields with a search weight of zero will be ignored.
        required: false
        type: int
        version_added: "3.10.0"
      group_name:
        description:
          - The group to associate the custom field with
        required: false
        type: str
        version_added: "3.10.0"
      ui_visibility:
         description:
           - The UI visibility of the custom field
         required: false
         choices:
           - read-write
           - read-only
           - hidden
           - hidden-ifunset
         type: str
         version_added: "3.10.0"
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
        type: str
      choice_set:
        description:
          - The name of the choice set to use (for selection fields)
        required: false
        type: str
      related_object_filter:
        description:
          - Filter definition for related object selection. To reset the value, set it to an empty dict (null value is ignored by the API)
        required: false
        type: dict
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox custom_fields module"
  connection: local
  hosts: localhost
  tasks:
    - name: Create a custom field on device and virtual machine
      netbox.netbox.netbox_custom_field:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          content_types:
            - dcim.device
            - virtualization.virtualmachine
          name: A Custom Field
          type: text

    - name: Create a custom field of type selection
      netbox.netbox.netbox_custom_field:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "Custom_Field"
          content_types:
            - dcim.device
            - virtualization.virtualmachine
          type: select
          choice_set: A Choice Set name

    - name: Update the custom field to make it required
      netbox.netbox.netbox_custom_field:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: A Custom Field
          required: true

    - name: Update the custom field to make it read only
      netbox.netbox.netbox_custom_field:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: A Custom Field
          ui_visibility: read-only

    - name: Delete the custom field
      netbox.netbox.netbox_custom_field:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: A Custom Field
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
                    content_types=dict(required=False, type="list", elements="raw"),
                    object_types=dict(required=False, type="list", elements="raw"),
                    type=dict(
                        required=False,
                        choices=[
                            "text",
                            "longtext",
                            "integer",
                            "decimal",
                            "boolean",
                            "date",
                            "datetime",
                            "url",
                            "json",
                            "select",
                            "multiselect",
                            "object",
                            "multiobject",
                        ],
                        type="str",
                    ),
                    object_type=dict(required=False, type="str"),
                    related_object_type=dict(required=False, type="str"),
                    name=dict(required=True, type="str"),
                    label=dict(required=False, type="str"),
                    description=dict(required=False, type="str"),
                    required=dict(required=False, type="bool"),
                    filter_logic=dict(required=False, type="raw"),
                    default=dict(required=False, type="raw"),
                    weight=dict(required=False, type="int"),
                    search_weight=dict(required=False, type="int"),
                    group_name=dict(required=False, type="str"),
                    ui_visibility=dict(
                        required=False,
                        choices=[
                            "read-write",
                            "read-only",
                            "hidden",
                            "hidden-ifunset",
                        ],
                        type="str",
                    ),
                    validation_minimum=dict(required=False, type="int"),
                    validation_maximum=dict(required=False, type="int"),
                    validation_regex=dict(required=False, type="str"),
                    choice_set=dict(
                        required=False,
                        type="str",
                    ),
                    related_object_filter=dict(required=False, type="dict"),
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

    netbox_custom_field = NetboxExtrasModule(module, NB_CUSTOM_FIELDS)
    netbox_custom_field.run()


if __name__ == "__main__":  # pragma: no cover
    main()

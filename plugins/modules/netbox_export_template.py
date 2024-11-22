#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Martin Rødvand (@rodvand) <martin@rodvand.net>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_export_template
short_description: Creates, updates or deletes export templates within NetBox
description:
  - Creates, updates or removes export templates from NetBox
notes:
  - This should be ran with connection C(local) and hosts C(localhost)
  - Use the C(!unsafe) data type if you want jinja2 code in template_code
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
      content_type:
        description:
          - The content type to apply this export template to
        required: false
        type: raw
      content_types:
        description:
          - The content type to apply this export template to (NetBox 3.4+)
        required: false
        type: list
        elements: raw
        version_added: "3.10.0"
      object_types:
        description:
          - The object type to apply this export template to (NetBox 4.0+)
        required: false
        type: list
        elements: raw
        version_added: "3.19.0"
      name:
        description:
          - The name of the export template
        required: true
        type: str
      description:
        description:
          - Description of the export template
        required: false
        type: str
      template_code:
        description:
          - Template code of the export template
        required: true
        type: raw
      mime_type:
        description:
          - MIME type of the export template
        required: false
        type: str
      file_extension:
        description:
          - The file extension of the export template
        required: false
        type: str
      as_attachment:
        description:
          - Download file as attachment
        required: false
        type: bool
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox export_templates module"
  connection: local
  hosts: localhost
  tasks:
    - name: "Ensure export template for /etc/hosts entries exists"
      netbox.netbox.netbox_export_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          object_types: ["dcim.device", "virtualization.virtualmachine"]
          name: /etc/hosts
          description: "Generate entries for /etc/hosts"
          as_attachment: true
          template_code: !unsafe |
            {% for vm in queryset -%}
            {%- if vm.primary_ip4 and vm.primary_ip6 %}
            {{ vm.primary_ip4.address.ip }} {{ vm.primary_ip6.address.ip }} {{ vm }}
            {%- elif vm.primary_ip4 %}
            {{ vm.primary_ip4.address.ip }} {{ vm }}
            {%- elif vm.primary_ip6 %}
            {{ vm.primary_ip6.address.ip }} {{ vm }}
            {%- endif -%}
            {%- endfor %}

    - name: Delete the export template
      netbox.netbox.netbox_export_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          content_type: "dcim.device"
          name: /etc/hosts
        state: absent
"""

RETURN = r"""
custom_link:
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
    NB_EXPORT_TEMPLATES,
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
                    content_type=dict(required=False, type="raw"),
                    content_types=dict(required=False, type="list", elements="raw"),
                    object_types=dict(required=False, type="list", elements="raw"),
                    name=dict(required=True, type="str"),
                    description=dict(required=False, type="str"),
                    template_code=dict(required=True, type="raw"),
                    mime_type=dict(required=False, type="str"),
                    file_extension=dict(required=False, type="str"),
                    as_attachment=dict(required=False, type="bool"),
                ),
            )
        )
    )

    required_if = [
        ("state", "present", ["name", "template_code"]),
        ("state", "absent", ["name"]),
    ]

    required_one_of = [["content_type", "content_types", "object_types"]]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=required_if,
        required_one_of=required_one_of,
    )

    netbox_export_template = NetboxExtrasModule(module, NB_EXPORT_TEMPLATES)
    netbox_export_template.run()


if __name__ == "__main__":
    main()

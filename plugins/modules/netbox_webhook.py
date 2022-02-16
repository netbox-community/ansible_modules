#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Martin Rødvand (@rodvand) <martin@rodvand.net>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_webhook
short_description: Creates, updates or deletes webhook configuration within NetBox
description:
  - Creates, updates or removes webhook configuration within NetBox
notes:  
  - This should be ran with connection C(local) and hosts C(localhost)
  - Use C(!unsafe) when adding jinja2 code to C(additional_headers) or C(body_template)
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
          - The content type(s) to apply this webhook to
          - Required when I(state=present)
        required: false
        type: list
        elements: raw      
      name:
        description:
          - Name of the webhook
        required: true
        type: str      
      type_create:
        description:
          - Call this webhook when a matching object is created
        required: false
        type: bool
      type_update:
        description:
          - Call this webhook when a matching object is updated
        required: false
        type: bool
      type_delete:
        description:
          - Call this webhook when a matching object is deleted
        required: false
        type: bool
      payload_url:
        description:
          - URL for the webhook to use.
          - Required when I(state=present)
        required: false
        type: str
      enabled:
        description:
          - Enable/disable the webhook.
        required: false
        type: bool
      http_method:
        description:
          - HTTP method of the webhook.
        required: false
        type: raw
      http_content_type:
        description:
          - The HTTP content type.
        required: false
        type: str
      additional_headers:
        description:
          - User-supplied HTTP headers. Supports jinja2 code.
        required: false
        type: str
      body_template:
        description:
          - Body template for webhook. Supports jinja2 code.
        required: false
        type: str
      secret:
        description:
          - Secret key to generate X-Hook-Signature to include in the payload.
        required: false
        type: str        
      conditions:
        description:
          - A set of conditions which determine whether the webhook will be generated.
        required: false
        type: str      
      ssl_verification:
        description:
          - Enable ssl verification. 
        required: false
        type: bool
      ca_file_path:
        description:
          - CA certificate file to use for SSL verification
        required: false
        type: str                                          
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox webhook module"
  connection: local
  hosts: localhost  
  tasks:
    - name: Create a webhook
      netbox_webhook:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          content_types:
            - dcim.device            
          name: Example Webhook
          type_create: yes
          payload_url: https://payload.url/
          body_template: !unsafe >-
            {{ data }}

    - name: Update the webhook to run on delete
      netbox_webhook:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Example Webhook
          type_create: yes
          type_delete: yes
          payload_url: https://payload.url/
          body_template: !unsafe >-
            {{ data }}         

    - name: Delete the webhook
      netbox_webhook:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Example Webhook
          type_create: yes
          type_delete: yes
          payload_url: https://payload.url/
          body_template: !unsafe >-
            {{ data }}  
        state: absent
"""

RETURN = r"""
webhook:
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
    NB_WEBHOOKS,
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
                    name=dict(required=True, type="str"),
                    type_create=dict(required=False, type="bool"),
                    type_update=dict(required=False, type="bool"),
                    type_delete=dict(required=False, type="bool"),
                    payload_url=dict(required=False, type="str"),
                    enabled=dict(required=False, type="bool"),
                    http_method=dict(required=False, type="raw"),
                    http_content_type=dict(required=False, type="str"),
                    additional_headers=dict(required=False, type="str"),
                    body_template=dict(required=False, type="str"),
                    secret=dict(required=False, type="str", no_log=False),
                    conditions=dict(required=False, type="str"),
                    ssl_verification=dict(required=False, type="bool"),
                    ca_file_path=dict(required=False, type="str"),
                ),
            )
        )
    )

    required_if = [
        ("state", "present", ["content_types", "name", "payload_url"]),
        ("state", "absent", ["name"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_webhook = NetboxExtrasModule(module, NB_WEBHOOKS)
    netbox_webhook.run()


if __name__ == "__main__":  # pragma: no cover
    main()

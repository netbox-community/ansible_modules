#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Martin Rødvand (@rodvand) <martin@rodvand.net>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_custom_link
short_description: Creates, updates or deletes custom links within NetBox
description:
  - Creates, updates or removes custom links from NetBox
notes:  
  - This should be ran with connection C(local) and hosts C(localhost)
  - Use the C(!unsafe) data type if you want jinja2 code in link_text or link_url
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
          - The content type to apply this custom link to
        required: false
        type: raw        
      name: 
        description: 
          - The name of the custom link
        required: true
        type: str
      link_text:
        description:
          - Link text of the custom link
        required: true
        type: raw
      link_url:
        description:
          - Link URL of the custom link
        required: true
        type: raw                
      weight:
        description:
          - Fields with higher weights appear lower in a form
        required: false
        type: int      
      group_name:
        description:
          - The group to associate the custom link with
        required: false
        type: str      
      button_class:
        description:
          - Button class for the custom link 
        required: false
        type: raw
      new_window:
        description:
          - Open link in new window 
        required: false
        type: bool   
      enabled:
        description:
          - Enable/disable custom link 
        required: false
        type: bool
        version_added: "3.7.0"                      
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox custom_link module"
  connection: local
  hosts: localhost  
  tasks:
    - name: Create a custom link on device
      netbox_custom_link:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          content_type: "dcim.device"            
          name: Custom Link
          link_text: "Open Web Management"
          link_url: !unsafe https://{{ obj.name }}.domain.local                        

    - name: Delete the custom link
      netbox_custom_field:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          content_type: "dcim.device"            
          name: Custom Link
          link_text: "Open Web Management"
          link_url: !unsafe https://{{ obj.name }}.domain.local
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
    NB_CUSTOM_LINKS,
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
                    name=dict(required=True, type="str"),
                    link_text=dict(required=True, type="raw"),
                    link_url=dict(required=True, type="raw"),
                    weight=dict(required=False, type="int"),
                    group_name=dict(required=False, type="str"),
                    button_class=dict(required=False, type="raw"),
                    new_window=dict(required=False, type="bool"),
                    enabled=dict(required=False, type="bool"),
                ),
            )
        )
    )

    required_if = [
        ("state", "present", ["content_type", "name", "link_text", "link_url"]),
        ("state", "absent", ["name"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_custom_link = NetboxExtrasModule(module, NB_CUSTOM_LINKS)
    netbox_custom_link.run()


if __name__ == "__main__":
    main()

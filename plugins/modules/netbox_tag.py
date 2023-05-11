#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2020, Pavel Korovin (@pkorovin) <p@tristero.se>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_tag
short_description: Creates or removes tags from NetBox
description:
  - Creates or removes tags from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Pavel Korovin (@pkorovin)
requirements:
  - pynetbox
version_added: "1.2.0"
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the tag configuration
    suboptions:
      name:
        description:
          - Tag name
        required: true
        type: str
      slug:
        description:
          - The slugified version of the name or custom slug.
          - This is auto-generated following NetBox rules if not provided
        required: false
        type: str
      color:
        description:
          - Tag color
        required: false
        type: str
      description:
        description:
          - Tag description
        required: false
        type: str
    required: true
"""

EXAMPLES = r"""
- name: "Test tags creation/deletion"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create tags
      netbox.netbox.netbox_tag:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "{{ item.name }}"
          description: "{{ item.description }}"
      loop:
        - { name: mgmt, description: "management" }
        - { name: tun, description: "tunnel" }

    - name: Delete tags
      netbox.netbox.netbox_tag:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "{{ item }}"
        state: absent
      loop:
        - mgmt
        - tun
"""

RETURN = r"""
tags:
  description: Serialized object as created/existent/updated/deleted within NetBox
  returned: always
  type: dict
msg:
  description: Message indicating failure or info about what has been achieved
  returned: always
  type: str
"""

from copy import deepcopy

from ansible_collections.netbox.netbox.plugins.module_utils.netbox_extras import NB_TAGS, NetboxExtrasModule
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_utils import NETBOX_ARG_SPEC, NetboxAnsibleModule


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
                    color=dict(required=False, type="str"),
                    description=dict(required=False, type="str"),
                    slug=dict(required=False, type="str"),
                ),
            ),
        )
    )

    required_if = [("state", "present", ["name"]), ("state", "absent", ["name"])]

    module = NetboxAnsibleModule(argument_spec=argument_spec, supports_check_mode=True, required_if=required_if)

    netbox_tag = NetboxExtrasModule(module, NB_TAGS)
    netbox_tag.run()


if __name__ == "__main__":  # pragma: no cover
    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2023, Martin Rødvand (@rodvand) <martin@rodvand.net>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_journal_entry
short_description: Creates a journal entry
description:
  - Creates a journal entry in NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Martin Rødvand (@rodvand)
requirements:
  - pynetbox
version_added: '3.12.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the journal entry
    suboptions:
      created_by:
        description:
          - The user ID of the user creating the journal entry. Omit to use the API token user
        required: false
        type: int
      kind:
        description:
          - The kind of journal entry
        required: false
        type: str
      assigned_object_id:
        description:
          - ID of the object to create the journal entry on
        required: true
        type: int
      assigned_object_type:
        description:
          - The object type of the model
        required: true
        type: str
      comments:
        description:
          - The comment associated with the journal entry
        required: true
        type: str
      tags:
        description:
          - Any tags that the journal entry may need to be associated with
        required: false
        type: list
        elements: raw
      custom_fields:
        description:
          - Must exist in NetBox
        required: false
        type: dict
    required: true
  state:
    description:
      - |
        Use C(new) for adding a journal entry.
    choices: [new]
    default: new
    type: str
"""

EXAMPLES = r"""
- name: "Test NetBox Module"
  hosts: localhost
  connection: local
  gather_facts: false
  module_defaults:
    group/netbox.netbox.netbox:
      netbox_url: MYURL
      netbox_token: MYTOKEN
  tasks:
    - name: Create an IP Address
      netbox.netbox.netbox_ip_address:
        data:
          address: 192.168.8.14/24
      register: ip

    - name: Create a journal entry
      netbox.netbox.netbox_journal_entry:
        data:
          assigned_object_type: ipam.ipaddress
          assigned_object_id: "{{ ip.ip_address.id }}"
          kind: success
          comments: |
            This is a journal entry
      when: ip.changed
"""

RETURN = r"""
journal_entry:
  description: Serialized object as created or already existent within NetBox
  returned: on creation
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
    NB_JOURNAL_ENTRIES,
)
from copy import deepcopy


def main():
    """
    Main entry point for module execution
    """
    argument_spec = deepcopy(NETBOX_ARG_SPEC)
    argument_spec["state"] = dict(required=False, default="new", choices=["new"])
    argument_spec.update(
        dict(
            data=dict(
                type="dict",
                required=True,
                options=dict(
                    created_by=dict(required=False, type="int"),
                    kind=dict(required=False, type="str"),
                    assigned_object_type=dict(required=True, type="str"),
                    assigned_object_id=dict(required=True, type="int"),
                    comments=dict(required=True, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [
        (
            "state",
            "new",
            ["comments", "assigned_object_type", "assigned_object_id"],
            True,
        ),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=required_if,
    )

    netbox_journal_entry = NetboxExtrasModule(module, NB_JOURNAL_ENTRIES)
    netbox_journal_entry.run()


if __name__ == "__main__":  # pragma: no cover
    main()

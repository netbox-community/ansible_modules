#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2025, Daniel Chiquito (@dchiquito) <daniel.chiquito@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_data_source
short_description: Creates or removes data sources from NetBox
description:
  - Creates or removes data sources from NetBox
author:
  - Daniel Chiquito (@dchiquito)
requirements:
  - pynetbox
version_added: "3.22.0"
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the data source configuration
    suboptions:
      name:
        description:
          - Name of the data source
        required: true
        type: str
      type:
        description:
          - The origin of the data source
        choices:
          - local
          - git
          - amazon-s3
        required: false
        type: str
      source_url:
        description:
          - URL of the data source to be created
        required: false
        type: str
      enabled:
        description:
          - Whether or not this data source can be synced
        required: false
        type: bool
      description:
        description:
          - Description of the data source
        required: false
        type: str
      ignore_rules:
        description:
          - Patterns (one per line) matching files to ignore when syncing
        required: false
        type: str
      sync_interval:
        description:
          - The interval in seconds between syncs
        required: false
        choices:
          - 1
          - 60
          - 720
          - 1440
          - 10080
          - 43200
        type: int
      comments:
        description:
          - Comments about the data source
        required: false
        type: str
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: false

  tasks:
    - name: "Create a new data source with only required information"
      netbox.netbox.netbox_data_source:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "Data Source 1"
          type: "local"
          source_url: "/tmp/data-source.txt"
          enabled: true
        state: present
    - name: "Update that data source with other fields"
      netbox.netbox.netbox_data_source:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "Data Source 1"
          type: "amazon-s3"
          source_url: "path/to/bucket"
          enabled: false
          description: "My first data source"
          ignore_rules: ".*\nfoo.txt\n*.yml"
          sync_interval: 1440
          comments: "Some commentary on this data source"
        state: present
    - name: "Delete the data source"
      netbox.netbox.netbox_data_source:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "Data Source 1"
        state: absent
"""

RETURN = r"""
data_source:
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_core import (
    NetboxCoreModule,
    NB_DATA_SOURCES,
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
                    type=dict(
                        required=False,
                        choices=["local", "git", "amazon-s3"],
                        type="str",
                    ),
                    source_url=dict(required=False, type="str"),
                    enabled=dict(required=False, type="bool"),
                    description=dict(required=False, type="str"),
                    ignore_rules=dict(required=False, type="str"),
                    sync_interval=dict(
                        required=False,
                        choices=[1, 60, 60 * 12, 60 * 24, 60 * 24 * 7, 60 * 24 * 30],
                        type="int",
                    ),
                    comments=dict(required=False, type="str"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["name", "type", "source_url", "enabled"]),
        ("state", "absent", ["name"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_data_source = NetboxCoreModule(module, NB_DATA_SOURCES)
    netbox_data_source.run()


if __name__ == "__main__":  # pragma: no cover
    main()

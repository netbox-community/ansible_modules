#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Mikhail Yohman (@FragmentedPacket) <mikhail.yohman@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_cluster_group
short_description: Create, update or delete cluster groups within NetBox
description:
  - Creates, updates or removes cluster groups from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Mikhail Yohman (@FragmentedPacket)
requirements:
  - pynetbox
version_added: '0.1.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    required: true
    type: dict
    description:
      - Defines the cluster group configuration
    suboptions:
      name:
        description:
          - The name of the cluster group
        required: true
        type: str
      slug:
        description:
          - The slugified version of the name or custom slug.
          - This is auto-generated following NetBox rules if not provided
        required: false
        type: str
      tags:
        description:
          - The tags to add/update
        required: false
        type: list
        elements: raw
        version_added: "3.6.0"
      custom_fields:
        description:
          - Must exist in NetBox
        required: false
        type: dict
        version_added: "3.6.0"
"""

EXAMPLES = r"""
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create cluster group within NetBox with only required information
      netbox.netbox.netbox_cluster_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Cluster Group
        state: present

    - name: Delete cluster within netbox
      netbox.netbox.netbox_cluster_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Cluster Group
        state: absent
"""

RETURN = r"""
cluster_group:
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_virtualization import (
    NetboxVirtualizationModule,
    NB_CLUSTER_GROUP,
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
                    slug=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [("state", "present", ["name"]), ("state", "absent", ["name"])]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_cluster_group = NetboxVirtualizationModule(module, NB_CLUSTER_GROUP)
    netbox_cluster_group.run()


if __name__ == "__main__":  # pragma: no cover
    main()

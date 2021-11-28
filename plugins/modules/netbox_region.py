#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Mikhail Yohman (@FragmentedPacket)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: netbox_region
short_description: Creates or removes regions from NetBox
description:
  - Creates or removes regions from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Mikhail Yohman (@FragmentedPacket)
requirements:
  - pynetbox
version_added: "0.1.0"
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the region configuration
    suboptions:
      name:
        description:
          - Name of the region to be created
        required: true
        type: str
      slug:
        description:
          - The slugified version of the name or custom slug.
          - This is auto-generated following NetBox rules if not provided
        required: false
        type: str
      parent_region:
        description:
          - The parent region this region should be tied to
        required: false
        type: raw
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox region module"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create region within NetBox with only required information
      netbox.netbox.netbox_region:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "Test Region One"
        state: present

    - name: Delete region within netbox
      netbox.netbox.netbox_region:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "Test Region One"
        state: absent
"""

RETURN = r"""
region:
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_dcim import (
    NetboxDcimModule,
    NB_REGIONS,
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
                    parent_region=dict(required=False, type="raw"),
                ),
            ),
        )
    )

    required_if = [("state", "present", ["name"]), ("state", "absent", ["name"])]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_region = NetboxDcimModule(module, NB_REGIONS)
    netbox_region.run()


if __name__ == "__main__":  # pragma: no cover
    main()

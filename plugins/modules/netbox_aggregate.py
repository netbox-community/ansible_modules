#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Mikhail Yohman (@FragmentedPacket) <mikhail.yohman@gmail.com>
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
module: netbox_aggregate
short_description: Creates or removes aggregates from Netbox
description:
  - Creates or removes aggregates from Netbox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Mikhail Yohman (@FragmentedPacket)
requirements:
  - pynetbox
version_added: '0.1.0'
options:
  netbox_url:
    description:
      - URL of the Netbox instance resolvable by Ansible control host
    required: true
  netbox_token:
    description:
      - The token created within Netbox to authorize API access
    required: true
  data:
    description:
      - Defines the aggregate configuration
    suboptions:
      prefix:
        description:
          - The aggregate prefix
        required: true
      rir:
        description:
          - The RIR the aggregate will be assigned to
        required:true
      date_added:
        description:
          - Date added, format: YYYY-MM-DD
      description:
        description:
          - The description of the aggregate
      tags:
        description:
          - Any tags that the aggregate may need to be associated with
      custom_fields:
        description:
          - must exist in Netbox
    required: true
  state:
    description:
      - The state of the aggregate
    choices: [ present, absent ]
    default: present
  validate_certs:
    description:
      - If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
    default: 'yes'
    type: bool
"""

EXAMPLES = r"""
- name: "Test Netbox aggregate module"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create aggregate within Netbox with only required information
      netbox_aggregate:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          prefix: 192.168.0.0/16
          rir: Test RIR
        state: present

    - name: Create aggregate with several specified options
      netbox_aggregate:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          prefix: 192.168.0.0/16
          rir: Test RIR
          date_added: 1989-01-18
          description: Test description
          tags:
            - Schnozzberry
        state: present

    - name: Delete aggregate within netbox
      netbox_aggregate:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          prefix: 192.168.0.0/16
        state: absent
"""

RETURN = r"""
aggregate:
  description: Serialized object as created or already existent within Netbox
  returned: on creation
  type: dict
msg:
  description: Message indicating failure or info about what has been achieved
  returned: always
  type: str
"""

from ansible_collections.netbox_community.ansible_modules.plugins.module_utils.netbox_utils import (
    NetboxAnsibleModule,
)
from ansible_collections.netbox_community.ansible_modules.plugins.module_utils.netbox_ipam import (
    NetboxIpamModule,
    NB_AGGREGATES,
)


def main():
    """
    Main entry point for module execution
    """
    argument_spec = dict(
        netbox_url=dict(type="str", required=True),
        netbox_token=dict(type="str", required=True, no_log=True),
        data=dict(type="dict", required=True),
        state=dict(required=False, default="present", choices=["present", "absent"]),
        validate_certs=dict(type="bool", default=True),
    )

    required_if = [("state", "present", ["prefix"]), ("state", "absent", ["prefix"])]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_aggregate = NetboxIpamModule(module, NB_AGGREGATES)
    netbox_aggregate.run()


if __name__ == "__main__":
    main()

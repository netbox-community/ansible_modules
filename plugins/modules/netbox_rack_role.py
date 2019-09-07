#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Mikhail Yohman (@FragmentedPacket) <mikhail.yohman@gmail.com>
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
module: netbox_rack_role
short_description: Create, update or delete racks roles within Netbox
description:
  - Creates, updates or removes racks roles from Netbox
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
      - Defines the rack role configuration
    suboptions:
      name:
        description:
          - The name of the rack role
        required: true
      color:
        description:
          - Hexidecimal code for a color, ex. FFFFFF
        required: true
    required: true
  state:
    description:
      - Use C(present) or C(absent) for adding or removing.
    choices: [ absent, present ]
    default: present
  validate_certs:
    description:
      - If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
    default: 'yes'
    type: bool
"""

EXAMPLES = r"""
- name: "Test Netbox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create rack role within Netbox with only required information
      netbox_rack_role:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test rack role
          color: FFFFFF
        state: present

    - name: Delete rack role within netbox
      netbox_rack_role:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Rack role 
        state: absent
"""

RETURN = r"""
rack_role:
  description: Serialized object as created or already existent within Netbox
  returned: success (when I(state=present))
  type: dict
msg:
  description: Message indicating failure or info about what has been achieved
  returned: always
  type: str
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.fragmentedpacket.netbox_modules.plugins.module_utils.netbox_dcim import (
    NetboxDcimModule,
    NB_RACK_ROLES,
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

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    # Fail if name is not given
    if not module.params["data"].get("name"):
        module.fail_json(msg="missing name")

    netbox_rack_role = NetboxDcimModule(module, NB_RACK_ROLES)
    netbox_rack_role.run()


if __name__ == "__main__":
    main()

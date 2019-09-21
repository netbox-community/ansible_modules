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
module: netbox_rir
short_description: Create, update or delete RIRs within Netbox
description:
  - Creates, updates or removes RIRs from Netbox
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
      - Defines the RIR configuration
    suboptions:
      name:
        description:
          - The name of the RIR
        required: true
      is_private:
        description:
          - IP space managed by this RIR is considered private
        type: bool
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
    - name: Create RIR within Netbox with only required information
      netbox_rir:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test RIR One
        state: present

    - name: Update Test RIR One
      netbox_rir:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test RIR One
          is_private: True
        state: present

    - name: Delete RIR within netbox
      netbox_rir:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test RIR One
        state: absent
"""

RETURN = r"""
rir:
  description: Serialized object as created or already existent within Netbox
  returned: success (when I(state=present))
  type: dict
msg:
  description: Message indicating failure or info about what has been achieved
  returned: always
  type: str
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.fragmentedpacket.netbox_modules.plugins.module_utils.netbox_ipam import (
    NetboxIpamModule,
    NB_RIRS,
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

    netbox_rir = NetboxIpamModule(module, NB_RIRS)
    netbox_rir.run()


if __name__ == "__main__":
    main()

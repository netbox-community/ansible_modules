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
module: netbox_provider
short_description: Create, update or delete providers within Netbox
description:
  - Creates, updates or removes providers from Netbox
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
      - Defines the provider configuration
    suboptions:
      name:
        description:
          - The name of the provider
        required: true
      asn:
        description:
          - The provider ASN
      account:
        description:
          - The account number of the provider
      portal_url:
        description:
          - The URL of the provider
      noc_contact:
        description:
          - The NOC contact of the provider
      admin_contact:
        description:
          - The admin contact of the provider
      comments:
        description:
          - Comments related to the provider
      tags:
        description:
          - Any tags that the device may need to be associated with
      custom_fields:
        description:
          - must exist in Netbox
  state:
    description:
      - Use C(present) or C(absent) for adding or removing.
    choices: [ absent, present ]
    default: present
  query_params:
    description:
      - This can be used to override the specified values in ALLOWED_QUERY_PARAMS that is defined
      - in plugins/module_utils/netbox_utils.py and provides control to users on what may make
      - an object unique in their environment.
    required: false
    type: list
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
    - name: Create provider within Netbox with only required information
      netbox_provider:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Provider
        state: present

    - name: Update provider with other fields
      netbox_provider:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Provider
          asn: 65001
          account: 200129104
          portal_url: http://provider.net
          noc_contact: noc@provider.net
          admin_contact: admin@provider.net
          comments: "BAD PROVIDER"
        state: present

    - name: Delete provider within netbox
      netbox_provider:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Provider
        state: absent
"""

RETURN = r"""
provider:
  description: Serialized object as created or already existent within Netbox
  returned: success (when I(state=present))
  type: dict
msg:
  description: Message indicating failure or info about what has been achieved
  returned: always
  type: str
"""

from ansible_collections.netbox.netbox.plugins.module_utils.netbox_utils import (
    NetboxAnsibleModule,
)
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_circuits import (
    NetboxCircuitsModule,
    NB_PROVIDERS,
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

    required_if = [("state", "present", ["name"]), ("state", "absent", ["name"])]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_provider = NetboxCircuitsModule(module, NB_PROVIDERS)
    netbox_provider.run()


if __name__ == "__main__":  # pragma: no cover
    main()

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
module: netbox_provider_network
short_description: Create, update or delete provider networks within NetBox
description:
  - Creates, updates or removes provider networks from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Martin Rødvand (@rodvand)
requirements:
  - pynetbox
version_added: '3.4.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the provider network configuration
    suboptions:
      provider:
        description:
          - The name of the provider
        required: true
        type: raw
      name:
        description:
          - The name of the provider network
        required: true
        type: str
     description:
        description:
          - Description related to the provider network
        required: false
        type: str
     comments:
        description:
          - Comments related to the provider network
        required: false
        type: str
      custom_fields:
        description:
          - must exist in NetBox
        required: false
        type: dict
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create provider within NetBox with only required information
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
provider_network:
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_circuits import (
    NetboxCircuitsModule,
    NB_PROVIDER_NETWORKS,
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
                    provider=dict(required=True, type="raw"),
                    name=dict(required=True, type="str"),
                    description=dict(required=False, type="str"),
                    comments=dict(required=False, type="str"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        ),
    )

    required_if = [("state", "present", ["name"]), ("state", "absent", ["name"])]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_provider_network = NetboxCircuitsModule(module, NB_PROVIDER_NETWORKS)
    netbox_provider_network.run()


if __name__ == "__main__":  # pragma: no cover
    main()

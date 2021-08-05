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
module: netbox_platform
short_description: Create or delete platforms within Netbox
description:
  - Creates or removes platforms from Netbox
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
    type: str
  netbox_token:
    description:
      - The token created within Netbox to authorize API access
    required: true
    type: str
  cert:
    description:
      - Certificate path
    required: false
    type: raw
  data:
    type: dict
    description:
      - Defines the platform configuration
    suboptions:
      name:
        description:
          - The name of the platform
        required: true
        type: str
      slug:
        description:
          - The slugified version of the name or custom slug.
          - This is auto-generated following NetBox rules if not provided
        required: false
        type: str
      description:
        description:
          - The description of the platform
        required: false
        type: str
      manufacturer:
        description:
          - The manufacturer the platform will be tied to
        required: false
        type: raw
      napalm_driver:
        description:
          - The name of the NAPALM driver to be used when using the NAPALM plugin
        required: false
        type: str
      napalm_args:
        description:
          - The optional arguments used for NAPALM connections
        required: false
        type: dict
    required: true
  state:
    description:
      - Use C(present) or C(absent) for adding or removing.
    choices: [ absent, present ]
    default: present
    type: str
  query_params:
    description:
      - This can be used to override the specified values in ALLOWED_QUERY_PARAMS that is defined
      - in plugins/module_utils/netbox_utils.py and provides control to users on what may make
      - an object unique in their environment.
    required: false
    type: list
    elements: str
  validate_certs:
    description:
      - If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
    default: true
    type: raw
"""

EXAMPLES = r"""
- name: "Test Netbox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create platform within Netbox with only required information
      netbox_platform:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Platform
        state: present

    - name: Create platform within Netbox with only required information
      netbox_platform:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Platform All
          manufacturer: Test Manufacturer
          napalm_driver: ios
          napalm_args:
            global_delay_factor: 2
        state: present

    - name: Delete platform within netbox
      netbox_platform:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Platform
        state: absent
"""

RETURN = r"""
platform:
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
    NETBOX_ARG_SPEC,
)
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_dcim import (
    NetboxDcimModule,
    NB_PLATFORMS,
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
                    description=dict(required=False, type="str"),
                    manufacturer=dict(required=False, type="raw"),
                    napalm_driver=dict(required=False, type="str"),
                    napalm_args=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [("state", "present", ["name"]), ("state", "absent", ["name"])]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_platform = NetboxDcimModule(module, NB_PLATFORMS)
    netbox_platform.run()


if __name__ == "__main__":  # pragma: no cover
    main()

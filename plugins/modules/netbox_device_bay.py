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
module: netbox_device_bay
short_description: Create, update or delete device bays within Netbox
description:
  - Creates, updates or removes device bays from Netbox
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
      - Defines the device bay configuration
    suboptions:
      device:
        description:
          - The device the device bay will be associated to. The device type must be "parent".
        required: true
      name:
        description:
          - The name of the device bay
        required: true
      description:
        description:
          - The description of the device bay. This is supported on v2.6+ of Netbox
      installed_device:
        description:
          - The ddevice that will be installed into the bay. The device type must be "child".
      tags:
        description:
          - Any tags that the device bay may need to be associated with
    required: true
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
    - name: Create device bay within Netbox with only required information
      netbox_device_bay:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: Test Nexus One
          name: "Device Bay One"
        state: present

    - name: Add device into device bay
      netbox_device_bay:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          device: Test Nexus One
          name: "Device Bay One"
          description: "First child"
          installed_device: Test Nexus Child One
        state: absent

    - name: Delete device bay within netbox
      netbox_device_bay:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Device Bay One
        state: absent

"""

RETURN = r"""
device_bay:
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
    NB_DEVICE_BAYS,
)


def main():
    """
    Main entry point for module execution
    """
    argument_spec = NETBOX_ARG_SPEC
    argument_spec.update(
        dict(
            data=dict(
                type="dict",
                required=True,
                options=dict(
                    device=dict(required=False, type="raw"),
                    name=dict(required=True, type="str"),
                    description=dict(required=False, type="str"),
                    installed_device=dict(required=False, type="raw"),
                    tags=dict(required=False, type=list),
                ),
            ),
        )
    )

    required_if = [("state", "present", ["name"]), ("state", "absent", ["name"])]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_device_bay = NetboxDcimModule(module, NB_DEVICE_BAYS)
    netbox_device_bay.run()


if __name__ == "__main__":  # pragma: no cover
    main()

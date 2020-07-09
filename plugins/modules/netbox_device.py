#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Mikhail Yohman (@FragmentedPacket) <mikhail.yohman@gmail.com>
# Copyright: (c) 2018, David Gomez (@amb1s1) <david.gomez@networktocode.com>
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
module: netbox_device
short_description: Create, update or delete devices within Netbox
description:
  - Creates, updates or removes devices from Netbox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Mikhail Yohman (@FragmentedPacket)
  - David Gomez (@amb1s1)
requirements:
  - pynetbox
version_added: '2.8'
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
  data:
    description:
      - Defines the device configuration
    suboptions:
      name:
        description:
          - The name of the device
        required: true
        type: str
      device_type:
        description:
          - Required if I(state=present) and the device does not exist yet
        required: false
        type: raw
      device_role:
        description:
          - Required if I(state=present) and the device does not exist yet
        required: false
        type: raw
      tenant:
        description:
          - The tenant that the device will be assigned to
        required: false
        type: raw
      platform:
        description:
          - The platform of the device
        required: false
        type: raw
      serial:
        description:
          - Serial number of the device
        required: false
        type: str
      asset_tag:
        description:
          - Asset tag that is associated to the device
        required: false
        type: str
      site:
        description:
          - Required if I(state=present) and the device does not exist yet
        required: false
        type: raw
      rack:
        description:
          - The name of the rack to assign the device to
        required: false
        type: raw
      position:
        description:
          - The position of the device in the rack defined above
        required: false
        type: int
      face:
        description:
          - Required if I(rack) is defined
        choices:
          - Front
          - front
          - Rear
          - rear
        required: false
        type: str
      status:
        description:
          - The status of the device
        required: false
        type: raw
      primary_ip4:
        description:
          - Primary IPv4 address assigned to the device
        required: false
        type: raw
      primary_ip6:
        description:
          - Primary IPv6 address assigned to the device
        required: false
        type: raw
      cluster:
        description:
          - Cluster that the device will be assigned to
        required: false
        type: raw
      virtual_chassis:
        description:
          - Virtual chassis the device will be assigned to
        required: false
        type: raw
      vc_position:
        description:
          - Position in the assigned virtual chassis
        required: false
        type: int
      vc_priority:
        description:
          - Priority in the assigned virtual chassis
        required: false
        type: int
      comments:
        description:
          - Comments that may include additional information in regards to the device
        required: false
        type: str
      tags:
        description:
          - Any tags that the device may need to be associated with
        required: false
        type: list
      custom_fields:
        description:
          - must exist in Netbox
        required: false
        type: dict
      local_context_data:
        description:
          - Arbitrary JSON data to define the devices configuration variables.
        required: false
        type: dict
    required: true
    type: dict
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
    - name: Create device within Netbox with only required information
      netbox_device:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Device
          device_type: C9410R
          device_role: Core Switch
          site: Main
        state: present

    - name: Create device within Netbox with empty string name to generate UUID
      netbox_device:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: ""
          device_type: C9410R
          device_role: Core Switch
          site: Main
        state: present

    - name: Delete device within netbox
      netbox_device:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Device
        state: absent

    - name: Create device with tags
      netbox_device:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Another Test Device
          device_type: C9410R
          device_role: Core Switch
          site: Main
          local_context_data:
            bgp: "65000"
          tags:
            - Schnozzberry
        state: present

    - name: Update the rack and position of an existing device
      netbox_device:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Device
          rack: Test Rack
          position: 10
          face: Front
        state: present
"""

RETURN = r"""
device:
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
    NB_DEVICES,
)
from copy import deepcopy
import uuid


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
                    device_type=dict(required=False, type="raw"),
                    device_role=dict(required=False, type="raw"),
                    tenant=dict(required=False, type="raw"),
                    platform=dict(required=False, type="raw"),
                    serial=dict(required=False, type="str"),
                    asset_tag=dict(required=False, type="str"),
                    site=dict(required=False, type="raw"),
                    rack=dict(required=False, type="raw"),
                    position=dict(required=False, type="int"),
                    face=dict(
                        required=False,
                        type="str",
                        choices=["Front", "front", "Rear", "rear"],
                    ),
                    status=dict(required=False, type="raw"),
                    primary_ip4=dict(required=False, type="raw"),
                    primary_ip6=dict(required=False, type="raw"),
                    cluster=dict(required=False, type="raw"),
                    virtual_chassis=dict(required=False, type="raw"),
                    vc_position=dict(required=False, type="int"),
                    vc_priority=dict(required=False, type="int"),
                    comments=dict(required=False, type="str"),
                    tags=dict(required=False, type="list"),
                    local_context_data=dict(required=False, type="dict"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [("state", "present", ["name"]), ("state", "absent", ["name"])]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )
    if module.params["data"]["name"] == "":
        module.params["data"]["name"] = str(uuid.uuid4())

    netbox_device = NetboxDcimModule(module, NB_DEVICES)
    netbox_device.run()


if __name__ == "__main__":  # pragma: no cover
    main()

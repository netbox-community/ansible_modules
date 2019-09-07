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
module: netbox_rack
short_description: Create, update or delete racks within Netbox
description:
  - Creates, updates or removes racks from Netbox
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
      - Defines the rack configuration
    suboptions:
      name:
        description:
          - The name of the rack
        required: true
      facility_id:
        description:
          - The unique rack ID assigned by the facility
      site:
        description:
          - Required if I(state=present) and the rack does not exist yet
      rack_group:
        description:
          - The rack group the rack will be associated to
      tenant:
        description:
          - The tenant that the device will be assigned to
      status:
        description:
          - The status of the rack
        choices:
          - Active
          - Planned
          - Reserved
          - Available
          - Deprecated
      rack_role:
        description:
          - The rack role the rack will be associated to
      serial:
        description:
          - Serial number of the rack
      asset_tag:
        description:
          - Asset tag that is associated to the rack
      type:
        description:
          - The type of rack
        choices:
          - 2-post frame
          - 4-post frame
          - 4-post cabinet
          - Wall-mounted frame
          - Wall-mounted cabinet
      width:
        description:
          - The rail-to-rail width
        choices:
          - 19
          - 23
      u_height:
        description:
          - The height of the rack in rack units
      desc_units:
        description:
          - Rack units will be numbered top-to-bottom
        type: bool
      outer_width:
        description:
          - The outer width of the rack
      outer_depth:
        description:
          - The outer depth of the rack
      outer_unit:
        description:
          - Whether the rack unit is in Millimeters or Inches and is I(required) if outer_width/outer_depth is specified
        choices:
          - Millimeters
          - Inches
      comments:
        description:
          - Comments that may include additional information in regards to the rack
      tags:
        description:
          - Any tags that the rack may need to be associated with
      custom_fields:
        description:
          - must exist in Netbox
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
    - name: Create rack within Netbox with only required information
      netbox_rack:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test rack
          site: Test Site
        state: present

    - name: Delete rack within netbox
      netbox_rack:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Rack 
        state: absent
"""

RETURN = r"""
rack:
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
    NB_RACKS,
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

    netbox_rack = NetboxDcimModule(module, NB_RACKS)
    netbox_rack.run()


if __name__ == "__main__":
    main()

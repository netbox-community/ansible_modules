#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Mikhail Yohman (@FragmentedPacket) <mikhail.yohman@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_site
short_description: Creates or removes sites from NetBox
description:
  - Creates or removes sites from NetBox
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
      - Defines the site configuration
    suboptions:
      name:
        description:
          - Name of the site to be created
        required: true
        type: str
      status:
        description:
          - Status of the site
        required: false
        type: raw
      region:
        description:
          - The region that the site should be associated with
        required: false
        type: raw
      site_group:
        description:
          - The site group the site will be associated with (NetBox 2.11+)
        required: false
        type: raw
        version_added: "3.3.0"
      tenant:
        description:
          - The tenant the site will be assigned to
        required: false
        type: raw
      facility:
        description:
          - Data center provider or facility, ex. Equinix NY7
        required: false
        type: str
      asn:
        description:
          - The ASN associated with the site
        required: false
        type: int
      time_zone:
        description:
          - Timezone associated with the site, ex. America/Denver
        required: false
        type: str
      description:
        description:
          - The description of the prefix
        required: false
        type: str
      physical_address:
        description:
          - Physical address of site
        required: false
        type: str
      shipping_address:
        description:
          - Shipping address of site
        required: false
        type: str
      latitude:
        description:
          - Latitude in decimal format
        required: false
        type: float
      longitude:
        description:
          - Longitude in decimal format
        required: false
        type: float
      contact_name:
        description:
          - Name of contact for site
        required: false
        type: str
      contact_phone:
        description:
          - Contact phone number for site
        required: false
        type: str
      contact_email:
        description:
          - Contact email for site
        required: false
        type: str
      comments:
        description:
          - Comments for the site. This can be markdown syntax
        required: false
        type: str
      slug:
        description:
          - URL-friendly unique shorthand
        required: false
        type: str
      tags:
        description:
          - Any tags that the prefix may need to be associated with
        required: false
        type: list
        elements: raw
      custom_fields:
        description:
          - must exist in NetBox
        required: false
        type: dict
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox site module"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create site within NetBox with only required information
      netbox_site:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test - Colorado
        state: present

    - name: Delete site within netbox
      netbox_site:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test - Colorado
        state: absent

    - name: Create site with all parameters
      netbox_site:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test - California
          status: Planned
          region: Test Region
          site_group: Test Site Group
          tenant: Test Tenant
          facility: EquinoxCA7
          asn: 65001
          time_zone: America/Los Angeles
          description: This is a test description
          physical_address: Hollywood, CA, 90210
          shipping_address: Hollywood, CA, 90210
          latitude: 10.100000
          longitude: 12.200000
          contact_name: Jenny
          contact_phone: 867-5309
          contact_email: jenny@changednumber.com
          slug: test-california
          comments: ### Placeholder
        state: present
"""

RETURN = r"""
site:
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
    NB_SITES,
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
                    status=dict(required=False, type="raw"),
                    region=dict(required=False, type="raw"),
                    site_group=dict(required=False, type="raw"),
                    tenant=dict(required=False, type="raw"),
                    facility=dict(required=False, type="str"),
                    asn=dict(required=False, type="int"),
                    time_zone=dict(required=False, type="str"),
                    description=dict(required=False, type="str"),
                    physical_address=dict(required=False, type="str"),
                    shipping_address=dict(required=False, type="str"),
                    latitude=dict(required=False, type="float"),
                    longitude=dict(required=False, type="float"),
                    contact_name=dict(required=False, type="str"),
                    contact_phone=dict(required=False, type="str"),
                    contact_email=dict(required=False, type="str"),
                    comments=dict(required=False, type="str"),
                    slug=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [("state", "present", ["name"]), ("state", "absent", ["name"])]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_site = NetboxDcimModule(module, NB_SITES)
    netbox_site.run()


if __name__ == "__main__":  # pragma: no cover
    main()

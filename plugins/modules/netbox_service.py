#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Kulakov Ilya  (@TawR1024)
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
module: netbox_service
short_description: Creates or removes service from Netbox
description:
  - Creates or removes service from Netbox
notes:
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Kulakov Ilya (@TawR1024)
requirements:
  - pynetbox
version_added: '0.1.5'
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
      - Defines the service configuration
    suboptions:
      device:
        description:
          - Specifies on which device the service is running
        required: false
        type: raw
      virtual_machine:
        description:
          - Specifies on which virtual machine the service is running
        required: false
        type: raw
      name:
        description:
          - Name of the region to be created
        required: true
        type: str
      port:
        description:
          - Specifies which port used by service
        required: false
        type: int
      ports:
        description:
          - Specifies which ports used by service (NetBox 2.10 and newer)
        type: list
        elements: int
      protocol:
        description:
          - Specifies which protocol used by service
        required: true
        type: raw
      ipaddresses:
        description:
          - Specifies which IPaddresses to associate with service.
        required: false
        type: raw
      description:
        description:
          - Service description
        required: false
        type: str
      tags:
        description:
          - What tags to add/update
        required: false
        type: list
        elements: raw
      custom_fields:
        description:
          - Must exist in Netbox and in key/value format
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
- name: "Create netbox service"
  connection: local
  hosts: all
  gather_facts: False

  tasks:
    - name: Create service
      netbox_service:
        netbox_url: netbox_url
        netbox_token: netbox_token
        data:
          device: Test666
          name: node-exporter
          port: 9100
          protocol: TCP
          ipaddresses:
            - address: 127.0.0.1
          tags:
            - prometheus
        state: present

- name: "Delete netbox service"
  connection: local
  hosts: all
  gather_facts: False

  tasks:
    - name: Delete service
      netbox_service:
        netbox_url: netbox_url
        netbox_token: netbox_token
        data:
          device: Test666
          name: node-exporter
          port: 9100
          protocol: TCP
        state: absent
"""

from ansible_collections.netbox.netbox.plugins.module_utils.netbox_utils import (
    NetboxAnsibleModule,
    NETBOX_ARG_SPEC,
)
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_ipam import (
    NetboxIpamModule,
    NB_SERVICES,
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
                    device=dict(required=False, type="raw"),
                    virtual_machine=dict(required=False, type="raw"),
                    name=dict(required=True, type="str"),
                    port=dict(required=False, type="int"),
                    ports=dict(required=False, type="list", elements="int"),
                    protocol=dict(required=True, type="raw"),
                    ipaddresses=dict(required=False, type="raw"),
                    description=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["name"]),
        ("state", "absent", ["name"]),
    ]
    mutually_exclusive = [("port", "ports")]
    required_one_of = [["device", "virtual_machine"], ["port", "ports"]]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=required_if,
        required_one_of=required_one_of,
        mutually_exclusive=mutually_exclusive,
    )

    netbox_service = NetboxIpamModule(module, NB_SERVICES)

    # Change port to ports for 2.10+ and convert to a list with the single integer
    if netbox_service.data.get("port") and netbox_service._version_check_greater(
        netbox_service.version, "2.10", greater_or_equal=True
    ):
        netbox_service.data["ports"] = [netbox_service.data.pop("port")]

    # Run the normal run() method
    netbox_service.run()


if __name__ == "__main__":  # pragma: no cover
    main()

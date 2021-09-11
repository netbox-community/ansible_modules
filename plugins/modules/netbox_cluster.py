#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Gaelle Mangin (@gmangin)
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
module: netbox_cluster
short_description: Create, update or delete clusters within Netbox
description:
  - Creates, updates or removes clusters from Netbox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Gaelle MANGIN (@gmangin)
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
    required: true
    type: dict
    description:
      - Defines the cluster configuration
    suboptions:
      name:
        description:
          - The name of the cluster
        required: true
        type: str
      cluster_type:
        description:
          - type of the cluster
        required: false
        type: raw
      cluster_group:
        description:
          - group of the cluster
        required: false
        type: raw
      site:
        description:
          - Required if I(state=present) and the cluster does not exist yet
        required: false
        type: raw
      comments:
        description:
          - Comments that may include additional information in regards to the cluster
        required: false
        type: str
      tenant:
        description:
          - Tenant the cluster will be assigned to.
        required: false
        type: raw
      tags:
        description:
          - Any tags that the cluster may need to be associated with
        required: false
        type: list
        elements: raw
      custom_fields:
        description:
          - must exist in Netbox
        required: false
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
    - name: Create cluster within Netbox with only required information
      netbox_cluster:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Cluster
          cluster_type: libvirt
        state: present

    - name: Delete cluster within netbox
      netbox_cluster:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Cluster
        state: absent

    - name: Create cluster with tags
      netbox_cluster:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Another Test Cluster
          cluster_type: libvirt
          tags:
            - Schnozzberry
        state: present

    - name: Update the group and site of an existing cluster
      netbox_cluster:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Cluster
          cluster_type: qemu
          cluster_group: GROUP
          site: SITE
        state: present
"""

RETURN = r"""
cluster:
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_virtualization import (
    NetboxVirtualizationModule,
    NB_CLUSTERS,
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
                    cluster_type=dict(required=False, type="raw"),
                    cluster_group=dict(required=False, type="raw"),
                    site=dict(required=False, type="raw"),
                    tenant=dict(required=False, type="raw"),
                    comments=dict(required=False, type="str"),
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

    netbox_cluster = NetboxVirtualizationModule(module, NB_CLUSTERS)
    netbox_cluster.run()


if __name__ == "__main__":  # pragma: no cover
    main()

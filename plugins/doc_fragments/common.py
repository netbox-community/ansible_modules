# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Devon Mar (@devon-mar)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ModuleDocFragment(object):
    DOCUMENTATION = r"""
---
options:
  netbox_url:
    description:
      - The URL of the NetBox instance.
      - Must be accessible by the Ansible control host.
    required: true
    type: str
  netbox_token:
    description:
      - The NetBox API token.
    required: true
    type: str
  state:
    description:
      - The state of the object.
    choices:
      - present
      - absent
    default: present
    type: str
  query_params:
    description:
      - This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined
      - in plugins/module_utils/netbox_utils.py and provides control to users on what may make
      - an object unique in their environment.
    required: false
    type: list
    elements: str
  validate_certs:
    description:
      - If C(false), SSL certificates will not be validated.
      - If a file name/path is provided, it will be used as a CA certificate list for the purposes of server certificate validation.
      - Note that this differs from Ansible core modules' validate_certs, where a separate ca_path parameter is used.
      - This should only be used on personally-controlled sites using a self-signed certificates.
    default: true
    type: raw
  cert:
    description:
      - Certificate path
    required: false
    type: raw
  headers:
    description: Dictionary of headers to be passed to the NetBox API.
    required: false
    type: dict
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2023, Antoine Dunn (@MinDBreaK) <15737031+MinDBreaK@users.noreply.github.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_config_template
short_description: Creates or removes config templates from NetBox
description:
  - Creates or removes config templates from NetBox
notes:
  - Tags should be defined as a YAML list
author:
  - Antoine Dunn (@mindbreak)
requirements:
  - pynetbox
version_added: "3.15.0"
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    required: true
    type: dict
    description:
      - Defines the config template configuration
    suboptions:
      name:
        description:
          - Config template name
        required: true
        type: str
      description:
        description:
          - Template description. Max length 200 characters
        required: false
        type: str
      tags:
        description:
          - Any tags that the device may need to be associated with
        required: false
        type: list
        elements: raw
      environment_params:
        description:
          - Any additional parameters to pass when constructing the Jinja2 environment
        required: false
        type: dict
      template_code:
        description:
          - The template code to be rendered.
        required: false
        type: str
"""

EXAMPLES = r"""
- name: "Test config template creation/deletion"
  connection: local
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Create config template
      netbox.netbox.netbox_config_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "thisIsMyTemplateName"
          tags:
            - Cloud
          template_code: |
            #cloud-config
            packages:
              - ansible

    - name: Delete config template
      netbox.netbox.netbox_config_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "thisIsMyTemplateName"
        state: absent
"""

RETURN = r"""
config_templates:
  description: Serialized object as created/existent/updated/deleted within NetBox
  returned: always
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
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_extras import (
    NetboxExtrasModule,
    NB_CONFIG_TEMPLATES,
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
                    description=dict(required=False, type="str"),
                    template_code=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    environment_params=dict(required=False, type="dict"),
                ),
            ),
        )
    )

    module = NetboxAnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    netbox_config_template = NetboxExtrasModule(module, NB_CONFIG_TEMPLATES)
    netbox_config_template.run()


if __name__ == "__main__":  # pragma: no cover
    main()

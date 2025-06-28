#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2025, Chris Caldwell (@squirrel289) <chris@calan.co>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
# Documentation for netbox_event_rule module

Synopsis:
- Manages Netbox Event Rule objects.

Parameters:
- state:
    description:
      - Whether the event rule should be present or absent.
    type: str
    choices: [ 'present', 'absent' ]
    required: true
    # Inherited from NETBOX_ARG_SPEC
- data:
    description:
      - Dictionary containing the event rule parameters.
    type: dict
    required: true
    options:
      object_types:
        description:
          - List of content types (e.g., 'dcim.device') the event rule applies to.
        type: list
        elements: raw
        required: false # Required if state is 'present'
      name:
        description:
          - The name of the event rule.
        type: str
        required: true
      enabled:
        description:
          - Whether the event rule is enabled.
        type: bool
        required: false
      event_types:
        description:
          - List of event types that trigger the rule.
        type: list
        required: false # Required if state is 'present'
        options:
          - object_created
          - object_updated
          - object_deleted
          - job_started
          - job_completed
          - job_failed
          - job_errored
      conditions: # Note: if `conditions` is specified the, due to a limitation in the serialization in netbox_utils, Ansible will always mark as changed
        description:
          - Dictionary defining conditions for the event rule to trigger.
        type: dict
        required: false
        options:
          attr:
            description:
              - The attribute name to check.
            type: str
            required: false
            # Required together with 'value'
            # Required by 'negate' and 'op'
            # Mutually exclusive with 'or' and 'and'
          value:
            description:
              - The value to compare the attribute against.
            type: str
            required: false
            # Required together with 'attr'
            # Required by 'negate' and 'op'
            # Mutually exclusive with 'or' and 'and'
          negate:
            description:
              - Whether to negate the condition.
            type: bool
            required: false
            # Requires 'attr' and 'value'
          op:
            description:
              - The comparison operator.
            type: str
            required: false
            choices: [ '=', '>', '<', '>=', '<=' ]
            # Requires 'attr' and 'value'
          or:
            description:
              - A list of condition dictionaries to be evaluated with logical OR.
            type: list
            elements: dict
            required: false
            # Mutually exclusive with 'and' and 'attr'
          and:
            description:
              - A list of condition dictionaries to be evaluated with logical AND.
            type: list
            elements: dict
            required: false
            # Mutually exclusive with 'or' and 'attr'
      action_type:
        description:
          - The type of action to perform when the rule triggers.
        type: str
        required: false
        choices:
          - webhook
          - script
          - notification
      action_object_type:
        description:
          - The content type of the action object (e.g., 'extras.webhook').
        type: str
        required: false # Required if state is 'present'
      action_object_id:
        description:
          - The ID of the action object (e.g., the webhook ID).
        type: int
        required: false # Required if state is 'present'
      description:
        description:
          - A description for the event rule.
        type: str
        required: false
      tags:
        description:
          - List of tags to apply to the event rule.
        type: list
        elements: raw
        required: false
      custom_fields:
        description:
          - Dictionary of custom fields for the event rule.
        type: dict
        required: false

# Note: Standard Netbox connection parameters (url, token, validate_certs, etc.) are inherited from NETBOX_ARG_SPEC.

Notes:
- The following parameters are required when `state` is `present`: `data.object_types`, `data.event_types`, `data.action_object_type`, `data.action_object_id`.
- The following parameter is required when `state` is `absent`: `data.name`.
- Within `data.conditions`, the parameters `or`, `and`, and `attr` are mutually exclusive.
- Within `data.conditions`, the parameters `value` and `attr` are required together.
- Within `data.conditions`, the parameters `negate` and `op` require both `value` and `attr` to be present.

"""
EXAMPLES = r"""
# Example 1: Create an event rule using attr and value conditions (based on sample JSON)
- name: Create Netbox Event Rule for Virtual Disk Creation with specific name
  netbox.netbox.netbox_event_rule:
    netbox_url: "http://localhost:32768" # Replace with your Netbox URL
    netbox_token: "0123456789abcdef0123456789abcdef01234567" # Replace with your Netbox token
    state: present
    data:
      name: "test-webhook-event"
      action_type: "webhook"
      action_object_type: "extras.webhook"
      action_object_id: -1 # Replace with your webhook ID
      enabled: true
      object_types:
        - virtualization.virtualdisk
      event_types:
        - object_created
      conditions:
        attr: "name"
        value: "scsi0"
        negate: true # This condition triggers if the name is NOT "scsi0"

# Example 2: Create an event rule using 'and' conditions
- name: Update Netbox Event Rule for Virtual Disk Creation or Update in specific names
  netbox.netbox.netbox_event_rule:
    netbox_url: "http://localhost:32768" # Replace with your Netbox URL
    netbox_token: "0123456789abcdef0123456789abcdef01234567" # Replace with your Netbox token
    state: present
    data:
      name: "test-webhook-event"
      event_types:
        - object_created
      conditions:
            "and": 
              - "attr": "name",
                "value": "scsi0"
                "negate": true,
              - "attr": "name",
                "value": "rootfs"
                "negate": true,

      description: "Triggered when a virtual disk is created that is NOT named 'scsi0' or 'rootfs'."
      tags:
        - automation
        - netbox-event-rule

# Example 3: Ensure an event rule is absent
- name: Ensure test-webhook-event rule is absent
  netbox.netbox.netbox_event_rule:
    netbox_url: "http://localhost:32768" # Replace with your Netbox URL
    netbox_token: "0123456789abcdef0123456789abcdef01234567" # Replace with your Netbox token
    state: absent
    data:
      name: "test-webhook-event"
"""

RETURN = r"""
webhook:
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
    NB_EVENT_RULES,
)
from copy import deepcopy


def main():
    """
    Main entry point for module execution
    """
    conditions_spec = {
        "type": "dict",
        "required": False,
        "options": {
            "attr": dict(
                required=False,
                type="str",
            ),
            "value": dict(
                required=False,
                type="str",
            ),
            "negate": dict(
                required=False,
                type="bool",
            ),
            "op": dict(required=False, choices=["=", ">", "<", ">=", "<="], type="str"),
            "or": dict(type="list", required=False, elements="dict"),
            "and": dict(type="list", required=False, elements="dict"),
        },
        "required_together": [
            ["value", "attr"],
        ],
        "required_by": { 
            "negate": ["value", "attr"],
            "op": ["value", "attr"],
        },
        "mutually_exclusive": [
            ["or", "and", "attr"],
        ],
    }

    argument_spec = deepcopy(NETBOX_ARG_SPEC)
    argument_spec.update(
        dict(
            data=dict(
                type="dict",
                required=True,
                options=dict(
                    object_types=dict(required=False, type="list", elements="raw"),
                    name=dict(required=True, type="str"),
                    enabled=dict(required=False, type="bool"),
                    event_types=dict(
                        required=False,
                        options=[
                            "object_created",
                            "object_updated",
                            "object_deleted",
                            "job_started",
                            "job_completed",
                            "job_failed",
                            "job_errored",
                        ],
                        type="list",
                    ),
                    # Note: if `conditions` is specified then, due to a limitation in the serialization in netbox_utils, Ansible will always mark as changed
                    # TODO: Fix this limitation in netbox_utils
                    conditions=conditions_spec,
                    action_type=dict(
                        required=False,
                        choices=[
                            "webhook",
                            "script",
                            "notification",
                        ],
                        type="str",
                    ),
                    action_object_type=dict(required=False, type="str"),
                    action_object_id=dict(required=False, type="int"),
                    description=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            )
        )
    )
    required_if = [
        (
            "state",
            "present",
            ["object_types", "event_types", "action_object_type", "action_object_id"],
        ),
        ("state", "absent", ["name"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=required_if,
    )

    netbox_event_rule = NetboxExtrasModule(module, NB_EVENT_RULES)
    netbox_event_rule.run()


if __name__ == "__main__":  # pragma: no cover
    main()

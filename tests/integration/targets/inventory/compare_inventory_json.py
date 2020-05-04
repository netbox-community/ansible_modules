#!/usr/bin/env python

# Inspired by community.aws collection script_inventory_ec2 test
# https://github.com/ansible-collections/community.aws/blob/master/tests/integration/targets/script_inventory_ec2/inventory_diff.py

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import sys
import json
from jsondiff import diff
from typing import Iterable

# Netbox includes created and last_updated times on objects.
# These end up in the interfaces objects that are included verbatim from the Netbox API.
# Ignore these when performing diffs as they will be different for each test run
ignored_keys = set(
    ["created", "last_updated", "form_factor", "type", "status", "protocol"]
)
# interface "form_factor", "type", ip_addresses "status", and service "protocol" are differnt in Netbox 2.6 vs 2.7 APIs


# Assume the object will not be recursive, as it originally came from JSON
def remove_ignored_keys(obj):

    if isinstance(obj, dict):
        keys_to_remove = ignored_keys.intersection(obj.keys())
        for key in keys_to_remove:
            del obj[key]

        for (key, value) in obj.items():
            remove_ignored_keys(value)

    elif isinstance(obj, list):
        for item in obj:
            remove_ignored_keys(item)


def remove_specifics(obj):
    try:
        # Netbox 2.6 doesn't output "tags" for services
        # I don't just want to ignore the "tags" key everywhere, as it's a host var that users care about
        services = obj["_meta"]["hostvars"]["test100"]["services"]
        for item in services:
            item.pop("tags", None)
    except Exception:
        pass


def main():
    if len(sys.argv) != 3:
        print(
            "Error: Must have exactly 2 file to compare passed as arguments. Received %i."
            % (len(sys.argv) - 1),
            file=sys.stderr,
        )
        sys.exit(2)

    a = sys.argv[1]
    b = sys.argv[2]

    with open(a, "r") as f:
        adata = json.loads(f.read())
    with open(b, "r") as f:
        bdata = json.loads(f.read())

    # Remove keys that we don't want to diff
    # ie. times that will change on each run of tests
    remove_ignored_keys(adata)
    remove_ignored_keys(bdata)
    remove_specifics(adata)
    remove_specifics(bdata)

    # Perform the diff
    # syntax='symmetric' will produce output that prints both the before and after as "$insert" and "$delete"
    # marshal=True removes any special types, allowing to be dumped as json
    result = diff(adata, bdata, marshal=True, syntax="symmetric")

    if result:
        # Dictionary is not empty - print differences
        print(json.dumps(result, sort_keys=True, indent=4))
        sys.exit(1)
    else:
        # Success, no differences
        sys.exit(0)


if __name__ == "__main__":
    main()

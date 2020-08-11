#!/usr/bin/env python

# Inspired by community.aws collection script_inventory_ec2 test
# https://github.com/ansible-collections/community.aws/blob/master/tests/integration/targets/script_inventory_ec2/inventory_diff.py

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import sys
import json
import argparse
from jsondiff import diff
from typing import Iterable
from operator import itemgetter

# Netbox includes "created" and "last_updated" times on objects. These end up in the interfaces objects that are included verbatim from the Netbox API.
# "url" may be different if local tests use a different host/port
# Remove these from files saved in git as test data
KEYS_REMOVE = frozenset(["created", "last_updated", "url"])

# Ignore these when performing diffs as they will be different for each test run
# (Was previously keys specific to NetBox 2.6)
KEYS_IGNORE = frozenset()

# Rack Groups became hierarchical in NetBox 2.8. Don't bother comparing against test data in NetBox 2.7
KEYS_IGNORE_27 = frozenset(
    [
        "rack_groups",  # host var
        "rack_group_parent_rack_group",  # group, group_names_raw = False
        "parent_rack_group",  # group, group_names_raw = True
    ]
)


def all_keys_to_ignore(netbox_version):
    keys = KEYS_REMOVE.union(KEYS_IGNORE)

    if netbox_version == "v2.7":
        return keys.union(KEYS_IGNORE_27)
    else:
        return keys


# Assume the object will not be recursive, as it originally came from JSON
def remove_keys(obj, keys):

    if isinstance(obj, dict):
        keys_to_remove = keys.intersection(obj.keys())
        for key in keys_to_remove:
            del obj[key]

        for (key, value) in obj.items():
            remove_keys(value, keys)

    elif isinstance(obj, list):
        # Iterate over temporary copy, as we may remove items
        for item in obj[:]:
            if isinstance(item, str) and item in keys:
                # List contains a string that we want to remove
                # eg. a group name in list of groups
                obj.remove(item)
            remove_keys(item, keys)


def sort_hostvar_arrays(obj):
    meta = obj.get("_meta")
    if not meta:
        return

    hostvars = meta.get("hostvars")
    if not hostvars:
        return

    for hostname, host in hostvars.items():
        interfaces = host.get("interfaces")
        if interfaces:
            host["interfaces"] = sorted(interfaces, key=itemgetter("id"))

        services = host.get("services")
        if services:
            host["services"] = sorted(services, key=itemgetter("id"))


def read_json(filename):
    with open(filename, "r") as f:
        return json.loads(f.read())


def write_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def main():
    parser = argparse.ArgumentParser(description="Diff Ansible inventory JSON output")
    parser.add_argument(
        "filename_a",
        metavar="ORIGINAL.json",
        type=str,
        help="Original json to test against",
    )
    parser.add_argument(
        "filename_b",
        metavar="NEW.json",
        type=str,
        help="Newly generated json to compare against original",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help=(
            "When comparing files, various keys are removed. "
            "This option will not compare the files, and instead writes ORIGINAL.json to NEW.json after removing these keys. "
            "This is used to clean the test json files before saving to the git repo. "
            "For example, this removes dates. "
        ),
    )
    parser.add_argument(
        "--netbox-version",
        metavar="VERSION",
        type=str,
        help=(
            "Apply comparison specific to NetBox version. "
            "For example, rack_groups arrays will only contain a single item in v2.7, so are ignored in the comparison."
        ),
    )

    args = parser.parse_args()

    data_a = read_json(args.filename_a)

    if args.write:
        # When writing test data, only remove "remove_keys" that will change on every git commit.
        # This makes diffs more easily readable to ensure changes to test data look correct.
        remove_keys(data_a, KEYS_REMOVE)
        sort_hostvar_arrays(data_a)
        write_json(args.filename_b, data_a)

    else:
        data_b = read_json(args.filename_b)

        # Ignore keys that we don't want to diff, in addition to the ones removed that change on every commit
        keys = all_keys_to_ignore(args.netbox_version)
        remove_keys(data_a, keys)
        remove_keys(data_b, keys)

        sort_hostvar_arrays(data_a)
        sort_hostvar_arrays(data_b)

        # Perform the diff
        # syntax='symmetric' will produce output that prints both the before and after as "$insert" and "$delete"
        # marshal=True removes any special types, allowing to be dumped as json
        result = diff(data_a, data_b, marshal=True, syntax="symmetric")

        if result:
            # Dictionary is not empty - print differences
            print(json.dumps(result, sort_keys=True, indent=4))
            sys.exit(1)
        else:
            # Success, no differences
            sys.exit(0)


if __name__ == "__main__":
    main()

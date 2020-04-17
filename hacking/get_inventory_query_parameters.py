#!/usr/bin/env python

# Usage: ./get_inventory_query_filters.py https://netbox/api/docs/?format=openapi

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import sys
import json
import urllib.request
from ansible.module_utils.urls import open_url


def get_parameters(data, path):
    output = list()

    parameters = data["paths"][path]["get"]["parameters"]
    for p in parameters:
        output.append(p["name"])

    # Sort, so git diffs are nice and consistent when parameters are updated
    output.sort()
    return output


url = sys.argv[1]

print("Getting from %s" % url, file=sys.stderr)

response = open_url(url)
data = json.load(response)

print("ALLOWED_DEVICE_QUERY_PARAMETERS = (")
for p in get_parameters(data, "/dcim/devices/"):
    print('    "%s",' % p)
print(")")
print()
print("ALLOWED_VM_QUERY_PARAMETERS = (")
for p in get_parameters(data, "/virtualization/virtual-machines/"):
    print('    "%s",' % p)
print(")")
print()

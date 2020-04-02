#!/usr/bin/env python3

# Usage: ./get_inventory_query_filters.py https://netbox/api/docs/?format=openapi

import sys
import json
import urllib.request


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

response = urllib.request.urlopen(url)
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

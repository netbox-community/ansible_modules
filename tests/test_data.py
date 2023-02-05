# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Bruno Inec (@sweenu) <bruno@inec.fr>
# Copyright: (c) 2019, Mikhail Yohman (@FragmentedPacket) <mikhail.yohman@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json


# Load test data from a json file, for a pytest parametrize
def load_test_data(path, test_path):
    with open(f"{path}/test_data/{test_path}/data.json", "r") as f:
        data = json.loads(f.read())
    tests = []
    for test in data:
        tuple_data = tuple(test.values())
        tests.append(tuple_data)
    return tests

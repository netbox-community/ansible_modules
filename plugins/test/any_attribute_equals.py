# Copyright (c) 2026 Mikulas Willaschek
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


def _resolve_attribute(item, attribute_path):
    node = item
    for part in attribute_path.split("."):
        if not isinstance(node, dict) or part not in node:
            return None
        node = node[part]
    return node


def any_attribute_equals(items, attribute_path, value):
    if not items:
        return False
    return any(_resolve_attribute(item, attribute_path) == value for item in items)


class TestModule(object):
    def tests(self):
        return {"any_attribute_equals": any_attribute_equals}

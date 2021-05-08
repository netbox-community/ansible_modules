# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Network to Code <opensource@networktocode.com>

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from pathlib import Path


def gather_manufacturers(path):
    library_path = Path(f"{path}").expanduser()
    manufacturers = [x.name for x in library_path.iterdir() if x.is_dir()]

    return manufacturers


def gather_device_types(path, manufacturers):
    device_types = []
    for m in manufacturers:
        m_path = Path(f"{path}/{m}/").expanduser()
        device_types.extend([x.stem for x in m_path.glob("*.yaml")])

    return device_types


class FilterModule(object):
    """Nautobot Ansible Filter Plugins."""

    def filters(self):
        filters = {
            "gather_manufacturers": gather_manufacturers,
            "gather_device_types": gather_device_types,
        }

        return filters

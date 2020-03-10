# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Mikhail Yohman (@fragmentedpacket) <mikhail.yohman@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

# Import necessary packages
import traceback
from ansible.module_utils.basic import missing_required_lib

try:
    from ansible_collections.netbox_community.ansible_modules.plugins.module_utils.netbox_utils import (
        NetboxModule,
        ENDPOINT_NAME_MAPPING,
        SLUG_REQUIRED,
    )
except ImportError:
    import sys

    sys.path.append(".")
    from netbox_utils import NetboxModule, ENDPOINT_NAME_MAPPING, SLUG_REQUIRED


NB_DEVICE_BAYS = "device_bays"
NB_DEVICES = "devices"
NB_DEVICE_ROLES = "device_roles"
NB_DEVICE_TYPES = "device_types"
NB_INTERFACES = "interfaces"
NB_INVENTORY_ITEMS = "inventory_items"
NB_MANUFACTURERS = "manufacturers"
NB_PLATFORMS = "platforms"
NB_RACKS = "racks"
NB_RACK_ROLES = "rack_roles"
NB_RACK_GROUPS = "rack_groups"
NB_REGIONS = "regions"
NB_SITES = "sites"


class NetboxDcimModule(NetboxModule):
    def __init__(self, module, endpoint):
        super().__init__(module, endpoint)

    def run(self):
        """
        This function should have all necessary code for endpoints within the application
        to create/update/delete the endpoint objects
        Supported endpoints:
        - device_bays
        - devices
        - device_roles
        - device_types
        - interfaces
        - inventory_items
        - manufacturers
        - platforms
        - sites
        - racks
        - rack_roles
        - rack_groups
        - regions
        """
        # Used to dynamically set key when returning results
        endpoint_name = ENDPOINT_NAME_MAPPING[self.endpoint]

        self.result = {"changed": False}

        application = self._find_app(self.endpoint)
        nb_app = getattr(self.nb, application)
        nb_endpoint = getattr(nb_app, self.endpoint)

        data = self.data

        # Used for msg output
        if data.get("name"):
            name = data["name"]
        elif data.get("model") and not data.get("slug"):
            name = data["model"]
        elif data.get("slug"):
            name = data["slug"]

        if self.endpoint in SLUG_REQUIRED:
            if not data.get("slug"):
                data["slug"] = self._to_slug(name)

        # Make color params lowercase
        if data.get("color"):
            data["color"] = data["color"].lower()

        object_query_params = self._build_query_params(endpoint_name, data)
        self.nb_object = self._nb_endpoint_get(nb_endpoint, object_query_params, name)

        # This is logic to handle interfaces on a VC
        if self.endpoint == "interfaces":
            if self.nb_object:
                if self.nb_object.device:
                    device = nb_endpoint.get(self.nb_object.device.id)
                    if (
                        device["virtual_chassis"]
                        and self.nb_object.device.id != self.data["device"]
                    ):
                        self.object = None

        if self.state == "present":
            self._ensure_object_exists(nb_endpoint, endpoint_name, name, data)

        elif self.state == "absent":
            self._ensure_object_absent(endpoint_name, name)

        try:
            serialized_object = self.nb_object.serialize()
        except AttributeError:
            serialized_object = self.nb_object

        self.result.update({endpoint_name: serialized_object})

        self.module.exit_json(**self.result)

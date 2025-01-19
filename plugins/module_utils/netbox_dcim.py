# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Mikhail Yohman (@fragmentedpacket) <mikhail.yohman@gmail.com>
# Copyright: (c) 2020, Nokia, Tobias Groß (@toerb) <tobias.gross@nokia.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils.basic import missing_required_lib
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_utils import (
    NetboxModule,
    ENDPOINT_NAME_MAPPING,
    SLUG_REQUIRED,
)


NB_CABLES = "cables"
NB_CONSOLE_PORTS = "console_ports"
NB_CONSOLE_PORT_TEMPLATES = "console_port_templates"
NB_CONSOLE_SERVER_PORTS = "console_server_ports"
NB_CONSOLE_SERVER_PORT_TEMPLATES = "console_server_port_templates"
NB_DEVICE_BAYS = "device_bays"
NB_DEVICE_BAY_TEMPLATES = "device_bay_templates"
NB_DEVICES = "devices"
NB_DEVICE_ROLES = "device_roles"
NB_DEVICE_TYPES = "device_types"
NB_FRONT_PORTS = "front_ports"
NB_FRONT_PORT_TEMPLATES = "front_port_templates"
NB_INTERFACES = "interfaces"
NB_INTERFACE_TEMPLATES = "interface_templates"
NB_INVENTORY_ITEMS = "inventory_items"
NB_INVENTORY_ITEM_ROLES = "inventory_item_roles"
NB_LOCATIONS = "locations"
NB_MANUFACTURERS = "manufacturers"
NB_MODULES = "modules"
NB_MODULE_BAYS = "module_bays"
NB_MODULE_TYPES = "module_types"
NB_PLATFORMS = "platforms"
NB_POWER_FEEDS = "power_feeds"
NB_POWER_OUTLETS = "power_outlets"
NB_POWER_OUTLET_TEMPLATES = "power_outlet_templates"
NB_POWER_PANELS = "power_panels"
NB_POWER_PORTS = "power_ports"
NB_POWER_PORT_TEMPLATES = "power_port_templates"
NB_RACKS = "racks"
NB_RACK_ROLES = "rack_roles"
NB_RACK_GROUPS = "rack_groups"
NB_REAR_PORTS = "rear_ports"
NB_REAR_PORT_TEMPLATES = "rear_port_templates"
NB_REGIONS = "regions"
NB_SITES = "sites"
NB_SITE_GROUPS = "site_groups"
NB_VIRTUAL_CHASSIS = "virtual_chassis"
NB_MAC_ADDRESSES = "mac_addresses"

try:
    from packaging.version import Version

    HAS_PACKAGING = True
    PACKAGING_IMPORT_ERROR = ""
except ImportError as imp_exc:
    PACKAGING_IMPORT_ERROR = imp_exc
    HAS_PACKAGING = False


class NetboxDcimModule(NetboxModule):
    def __init__(self, module, endpoint):
        if not HAS_PACKAGING:
            module.fail_json(
                msg=missing_required_lib("packaging"), exception=PACKAGING_IMPORT_ERROR
            )
        super().__init__(module, endpoint)

    def run(self):
        """
        This function should have all necessary code for endpoints within the application
        to create/update/delete the endpoint objects
        Supported endpoints:
        - cables
        - console_ports
        - console_port_templates
        - console_server_ports
        - console_server_port_templates
        - device_bays
        - device_bay_templates
        - devices
        - device_roles
        - device_types
        - front_ports
        - front_port_templates
        - interfaces
        - interface_templates
        - inventory_items
        - inventory_item_roles
        - locations
        - manufacturers
        - modules
        - module_bays
        - module_types
        - platforms
        - power_feeds
        - power_outlets
        - power_outlet_templates
        - power_panels
        - power_ports
        - power_port_templates
        - sites
        - site_groups
        - racks
        - rack_roles
        - rack_groups
        - rear_ports
        - rear_port_templates
        - regions
        - virtual_chassis
        """
        # Used to dynamically set key when returning results
        endpoint_name = ENDPOINT_NAME_MAPPING[self.endpoint]

        self.result = {"changed": False}

        application = self._find_app(self.endpoint)
        nb_app = getattr(self.nb, application)
        nb_endpoint = getattr(nb_app, self.endpoint)
        user_query_params = self.module.params.get("query_params")

        data = self.data

        # Handle rack and form_factor
        if endpoint_name == "rack":
            if Version(self.full_version) >= Version("4.1.0"):
                if "type" in data:
                    data["form_factor"] = self._to_slug(data["type"])
                    del data["type"]

        # Used for msg output
        if data.get("name"):
            name = data["name"]
        elif data.get("model") and not data.get("slug"):
            name = data["model"]
        elif data.get("master"):
            name = self.module.params["data"]["master"]
        elif data.get("slug"):
            name = data["slug"]
        elif data.get("mac_address"):
            name = data["mac_address"]
        elif endpoint_name == "cable":
            if self.module.params["data"]["termination_a"].get("name"):
                termination_a_name = self.module.params["data"]["termination_a"]["name"]
            elif self.module.params["data"]["termination_a"].get("slug"):
                termination_a_name = self.module.params["data"]["termination_a"]["slug"]
            else:
                termination_a_name = data.get("termination_a_id")

            if self.module.params["data"]["termination_b"].get("name"):
                termination_b_name = self.module.params["data"]["termination_b"]["name"]
            elif self.module.params["data"]["termination_b"].get("slug"):
                termination_b_name = self.module.params["data"]["termination_b"]["slug"]
            else:
                termination_b_name = data.get("termination_b_id")

            name = "%s %s <> %s %s" % (
                data.get("termination_a_type"),
                termination_a_name,
                data.get("termination_b_type"),
                termination_b_name,
            )
        elif endpoint_name == "module":
            if isinstance(
                self.module.params["data"]["device"], dict
            ) and self.module.params["data"]["device"].get("name"):
                device_name = self.module.params["data"]["device"]["name"]
            elif isinstance(
                self.module.params["data"]["device"], dict
            ) and self.module.params["data"]["device"].get("slug"):
                device_name = self.module.params["data"]["device"]["slug"]
            else:
                device_name = self.module.params["data"]["device"]
            if isinstance(
                self.module.params["data"]["module_bay"], dict
            ) and self.module.params["data"]["module_bay"].get("name"):
                module_bay = self.module.params["data"]["module_bay"]["name"]
            elif isinstance(
                self.module.params["data"]["module_bay"], dict
            ) and self.module.params["data"]["module_bay"].get("slug"):
                module_bay = self.module.params["data"]["module_bay"]["slug"]
            else:
                module_bay = self.module.params["data"]["module_bay"]
            if isinstance(
                self.module.params["data"]["module_type"], dict
            ) and self.module.params["data"]["module_bay"].get("model"):
                module_type = self.module.params["data"]["module_type"]["model"]
            elif isinstance(
                self.module.params["data"]["module_type"], dict
            ) and self.module.params["data"]["module_bay"].get("part_number"):
                module_type = self.module.params["data"]["module_type"]["part_number"]
            else:
                module_type = self.module.params["data"]["module_type"]
            name = "%s: %s (%s)" % (device_name, module_bay, module_type)

        if self.endpoint in SLUG_REQUIRED:
            if not data.get("slug"):
                data["slug"] = self._to_slug(name)

        # Make color params lowercase
        if data.get("color"):
            data["color"] = data["color"].lower()

        if self.endpoint == "cables":
            if Version(self.full_version) >= Version("3.0.6"):
                cables = [
                    nb_endpoint.get(
                        termination_a_type=data["termination_a_type"],
                        termination_a_id=data["termination_a_id"],
                        termination_b_type=data["termination_b_type"],
                        termination_b_id=data["termination_b_id"],
                    )
                ]
            else:
                # Attempt to find the exact cable via the interface
                # relationship
                interface_a = self.nb.dcim.interfaces.get(data["termination_a_id"])
                interface_b = self.nb.dcim.interfaces.get(data["termination_b_id"])
                if (
                    interface_a.cable
                    and interface_b.cable
                    and interface_a.cable.id == interface_b.cable.id
                ):
                    cables = [self.nb.dcim.cables.get(interface_a.cable.id)]
                else:
                    cables = []
            if len(cables) == 0:
                self.nb_object = None
            elif len(cables) == 1:
                self.nb_object = cables[0]
            else:
                self._handle_errors(msg="More than one result returned for %s" % (name))

            if Version(self.full_version) >= Version("3.3.0"):
                data["a_terminations"] = [
                    {
                        "object_id": data.pop("termination_a_id"),
                        "object_type": data.pop("termination_a_type"),
                    }
                ]
                data["b_terminations"] = [
                    {
                        "object_id": data.pop("termination_b_id"),
                        "object_type": data.pop("termination_b_type"),
                    }
                ]
        else:
            object_query_params = self._build_query_params(
                endpoint_name, data, user_query_params
            )
            self.nb_object = self._nb_endpoint_get(
                nb_endpoint, object_query_params, name
            )

        # This is logic to handle interfaces on a VC
        if self.endpoint == "interfaces" and self.nb_object:
            child = self.nb.dcim.devices.get(self.nb_object.device.id)
            if child["virtual_chassis"] and child.id != data["device"]:
                if self.module.params.get("update_vc_child"):
                    data["device"] = child.id
                else:
                    self._handle_errors(
                        msg="Must set update_vc_child to True to allow child device interface modification"
                    )

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

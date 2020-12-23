# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Mikhail Yohman (@fragmentedpacket) <mikhail.yohman@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

# Import necessary packages
import traceback
from ansible_collections.ansible.netcommon.plugins.module_utils.compat import ipaddress
from ansible.module_utils._text import to_text
from ansible.module_utils.basic import missing_required_lib

from ansible_collections.netbox.netbox.plugins.module_utils.netbox_utils import (
    NetboxModule,
    ENDPOINT_NAME_MAPPING,
    SLUG_REQUIRED,
)


NB_AGGREGATES = "aggregates"
NB_IP_ADDRESSES = "ip_addresses"
NB_PREFIXES = "prefixes"
NB_IPAM_ROLES = "roles"
NB_RIRS = "rirs"
NB_VLANS = "vlans"
NB_VLAN_GROUPS = "vlan_groups"
NB_VRFS = "vrfs"
NB_SERVICES = "services"


class NetboxIpamModule(NetboxModule):
    def __init__(self, module, endpoint):
        super().__init__(module, endpoint)

    def _handle_state_new_present(self, nb_app, nb_endpoint, endpoint_name, name, data):
        if data.get("address"):
            if self.state == "present":
                self._ensure_object_exists(nb_endpoint, endpoint_name, name, data)
            elif self.state == "new":
                self.nb_object, diff = self._create_netbox_object(nb_endpoint, data)
                self.result["msg"] = "%s %s created" % (endpoint_name, name)
                self.result["changed"] = True
                self.result["diff"] = diff
        else:
            if self.state == "present":
                self._ensure_ip_in_prefix_present_on_netif(
                    nb_app, nb_endpoint, data, endpoint_name
                )
            elif self.state == "new":
                self._get_new_available_ip_address(nb_app, data, endpoint_name)

    def _ensure_ip_in_prefix_present_on_netif(
        self, nb_app, nb_endpoint, data, endpoint_name
    ):
        query_params = {
            "parent": data["prefix"],
        }

        if not self._version_check_greater(self.version, "2.9", greater_or_equal=True):
            if not data.get("interface") or not data.get("prefix"):
                self._handle_errors("A prefix and interface is required")
            data_intf_key = "interface"

        else:
            if not data.get("assigned_object_id") or not data.get("prefix"):
                self._handle_errors("A prefix and assigned_object is required")
            data_intf_key = "assigned_object_id"

        intf_obj_type = data.get("assigned_object_type", "dcim.interface")
        if intf_obj_type == "virtualization.vminterface":
            intf_type = "vminterface_id"
        else:
            intf_type = "interface_id"

        query_params.update({intf_type: data[data_intf_key]})

        if data.get("vrf"):
            query_params["vrf_id"] = data["vrf"]

        attached_ips = nb_endpoint.filter(**query_params)
        if attached_ips:
            self.nb_object = attached_ips[-1].serialize()
            self.result["changed"] = False
            self.result["msg"] = "%s %s already attached" % (
                endpoint_name,
                self.nb_object["address"],
            )
        else:
            self._get_new_available_ip_address(nb_app, data, endpoint_name)

    def _get_new_available_ip_address(self, nb_app, data, endpoint_name):
        prefix_query = self._build_query_params("prefix", data)
        prefix = self._nb_endpoint_get(nb_app.prefixes, prefix_query, data["prefix"])
        if not prefix:
            self.result["changed"] = False
            self.result["msg"] = "%s does not exist - please create first" % (
                data["prefix"]
            )
        elif prefix.available_ips.list():
            self.nb_object, diff = self._create_netbox_object(
                prefix.available_ips, data
            )
            self.nb_object = self.nb_object.serialize()
            self.result["changed"] = True
            self.result["msg"] = "%s %s created" % (
                endpoint_name,
                self.nb_object["address"],
            )
            self.result["diff"] = diff
        else:
            self.result["changed"] = False
            self.result["msg"] = "No available IPs available within %s" % (
                data["prefix"]
            )

    def _get_new_available_prefix(self, data, endpoint_name):
        if not self.nb_object:
            self.result["changed"] = False
            self.result["msg"] = "Parent prefix does not exist - %s" % (data["parent"])
        elif self.nb_object.available_prefixes.list():
            if self.check_mode:
                self.result["changed"] = True
                self.result["msg"] = "New prefix created within %s" % (data["parent"])
                self.module.exit_json(**self.result)

            self.nb_object, diff = self._create_netbox_object(
                self.nb_object.available_prefixes, data
            )
            self.nb_object = self.nb_object.serialize()
            self.result["changed"] = True
            self.result["msg"] = "%s %s created" % (
                endpoint_name,
                self.nb_object["prefix"],
            )
            self.result["diff"] = diff
        else:
            self.result["changed"] = False
            self.result["msg"] = "No available prefixes within %s" % (data["parent"])

    def run(self):
        """
        This function should have all necessary code for endpoints within the application
        to create/update/delete the endpoint objects
        Supported endpoints:
        - aggregates
        - ipam_roles
        - ip_addresses
        - prefixes
        - rirs
        - vlans
        - vlan_groups
        - vrfs
        """
        # Used to dynamically set key when returning results
        endpoint_name = ENDPOINT_NAME_MAPPING[self.endpoint]

        self.result = {"changed": False}

        application = self._find_app(self.endpoint)
        nb_app = getattr(self.nb, application)
        nb_endpoint = getattr(nb_app, self.endpoint)
        user_query_params = self.module.params.get("query_params")

        data = self.data

        if self.endpoint == "ip_addresses":
            if data.get("address"):
                try:
                    data["address"] = to_text(ipaddress.ip_network(data["address"]))
                except ValueError:
                    pass
            name = data.get("address")
        elif self.endpoint in ["aggregates", "prefixes"]:
            name = data.get("prefix")
        else:
            name = data.get("name")

        if self.endpoint in SLUG_REQUIRED:
            if not data.get("slug"):
                data["slug"] = self._to_slug(name)

        if self.module.params.get("first_available"):
            first_available = True
        else:
            first_available = False

        object_query_params = self._build_query_params(
            endpoint_name, data, user_query_params
        )
        if data.get("prefix") and self.endpoint == "ip_addresses":
            object_query_params = self._build_query_params("prefix", data)
            self.nb_object = self._nb_endpoint_get(
                nb_app.prefixes, object_query_params, name
            )
        else:
            self.nb_object = self._nb_endpoint_get(
                nb_endpoint, object_query_params, name
            )

        if self.state in ("new", "present") and endpoint_name == "ip_address":
            self._handle_state_new_present(
                nb_app, nb_endpoint, endpoint_name, name, data
            )
        elif self.state == "present" and first_available and data.get("parent"):
            self._get_new_available_prefix(data, endpoint_name)
        elif self.state == "present":
            self._ensure_object_exists(nb_endpoint, endpoint_name, name, data)
        elif self.state == "absent":
            self._ensure_object_absent(endpoint_name, name)

        try:
            serialized_object = self.nb_object.serialize()
        except AttributeError:
            serialized_object = self.nb_object

        self.result.update({endpoint_name: serialized_object})

        self.module.exit_json(**self.result)

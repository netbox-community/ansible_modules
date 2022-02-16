# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Martin Rødvand (@rodvand) <martin@rodvand.net>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.netbox.netbox.plugins.module_utils.netbox_utils import (
    NetboxModule,
    ENDPOINT_NAME_MAPPING,
    SLUG_REQUIRED,
)


NB_WIRELESS_LANS = "wireless_lans"
NB_WIRELESS_LAN_GROUPS = "wireless_lan_groups"
NB_WIRELESS_LINKS = "wireless_links"


class NetboxWirelessModule(NetboxModule):
    def __init__(self, module, endpoint):
        super().__init__(module, endpoint)

    def run(self):
        """
        This function should have all necessary code for endpoints within the application
        to create/update/delete the endpoint objects
        Supported endpoints:
        - wireless LAN
        - wireless LAN Group
        - wireless link
        """
        # Used to dynamically set key when returning results
        endpoint_name = ENDPOINT_NAME_MAPPING[self.endpoint]

        self.result = {"changed": False}

        application = self._find_app(self.endpoint)
        nb_app = getattr(self.nb, application)
        nb_endpoint = getattr(nb_app, self.endpoint)
        user_query_params = self.module.params.get("query_params")

        data = self.data

        # Used for msg output
        if data.get("name"):
            name = data["name"]
        elif data.get("slug"):
            name = data["slug"]
        elif data.get("ssid"):
            name = data["ssid"]

        if data.get("interface_a") and data.get("interface_b"):
            interface_a_name = self.module.params["data"]["interface_a"].get("name")
            interface_a_device = self.module.params["data"]["interface_a"].get("device")
            interface_b_name = self.module.params["data"]["interface_b"].get("name")
            interface_b_device = self.module.params["data"]["interface_b"].get("device")
            name = f"{interface_a_device} {interface_a_name} <> {interface_b_device} {interface_b_name}"

        if self.endpoint in SLUG_REQUIRED:
            if not data.get("slug"):
                data["slug"] = self._to_slug(name)

        object_query_params = self._build_query_params(
            endpoint_name, data, user_query_params
        )
        self.nb_object = self._nb_endpoint_get(nb_endpoint, object_query_params, name)

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

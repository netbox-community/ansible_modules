# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Mikhail Yohman (@fragmentedpacket) <mikhail.yohman@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.netbox.netbox.plugins.module_utils.netbox_utils import (
    NetboxModule,
    ENDPOINT_NAME_MAPPING,
    SLUG_REQUIRED,
)


NB_PROVIDERS = "providers"
NB_PROVIDER_NETWORKS = "provider_networks"
NB_CIRCUIT_TYPES = "circuit_types"
NB_CIRCUIT_TERMINATIONS = "circuit_terminations"
NB_CIRCUITS = "circuits"


class NetboxCircuitsModule(NetboxModule):
    def __init__(self, module, endpoint):
        super().__init__(module, endpoint)

    def run(self):
        """
        This function should have all necessary code for endpoints within the application
        to create/update/delete the endpoint objects
        Supported endpoints:
        - circuit_types
        - circuit_terminations
        - circuits
        - providers
        - provider_networks
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
        elif data.get("cid"):
            name = data["cid"]
        elif data.get("circuit") and data.get("term_side"):
            circuit = self.nb.circuits.circuits.get(data["circuit"]).serialize()
            name = "{0}_{1}".format(
                circuit["cid"].replace(" ", "_"), data["term_side"]
            ).lower()

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

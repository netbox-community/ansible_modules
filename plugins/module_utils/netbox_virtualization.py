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

NB_VIRTUAL_MACHINES = "virtual_machines"
NB_CLUSTERS = "clusters"
NB_CLUSTER_GROUP = "cluster_groups"
NB_CLUSTER_TYPE = "cluster_types"
NB_VM_INTERFACES = "interfaces"
NB_VIRTUAL_DISKS = "virtual_disks"


class NetboxVirtualizationModule(NetboxModule):
    def __init__(self, module, endpoint):
        super().__init__(module, endpoint)

    def run(self):
        """
        This function should have all necessary code for endpoints within the application
        to create/update/delete the endpoint objects
        Supported endpoints:
          - clusters
          - cluster_groups
          - cluster_types
          - interfaces
          - virtual_machines
          - netbox_cluster
        """
        # Used to dynamically set key when returning results
        endpoint_name = ENDPOINT_NAME_MAPPING[self.endpoint]

        self.result = {"changed": False}

        if self.endpoint == "interfaces":
            application = "virtualization"
        else:
            application = self._find_app(self.endpoint)
        nb_app = getattr(self.nb, application)
        nb_endpoint = getattr(nb_app, self.endpoint)
        user_query_params = self.module.params.get("query_params")

        data = self.data

        # NetBox v4.2+ made the VM interface serializer's legacy `mac_address` field
        # read-only, so it is silently dropped on write. Always pull it out of the
        # payload here; translate it into the interface's primary MAC (after the
        # interface is ensured below) only when an explicit `primary_mac_address` was
        # not provided, so an explicit primary always wins.
        legacy_mac_address = None
        if self.endpoint == "interfaces" and self._version_check_greater(
            self.api_version, "4.2", greater_or_equal=True
        ):
            popped_mac_address = data.pop("mac_address", None)
            if popped_mac_address and not data.get("primary_mac_address"):
                legacy_mac_address = popped_mac_address

        # Used for msg output
        if data.get("name"):
            name = data["name"]
        elif data.get("slug"):
            name = data["slug"]

        if self.endpoint in SLUG_REQUIRED:
            if not data.get("slug"):
                data["slug"] = self._to_slug(name)

        object_query_params = self._build_query_params(
            endpoint_name, data, user_query_params
        )
        self.nb_object = self._nb_endpoint_get(nb_endpoint, object_query_params, name)

        if self.state == "present":
            self._ensure_object_exists(nb_endpoint, endpoint_name, name, data)
            if legacy_mac_address:
                self._set_primary_mac_address(
                    endpoint_name,
                    name,
                    legacy_mac_address,
                    "virtualization.vminterface",
                )
        elif self.state == "absent":
            self._ensure_object_absent(endpoint_name, name)

        try:
            serialized_object = self.nb_object.serialize()
        except AttributeError:
            serialized_object = self.nb_object

        self.result.update({endpoint_name: serialized_object})

        self.module.exit_json(**self.result)

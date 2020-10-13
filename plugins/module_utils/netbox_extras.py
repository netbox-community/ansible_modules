# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Mikhail Yohman (@fragmentedpacket) <mikhail.yohman@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

# Import necessary packages
import traceback
from ansible.module_utils.basic import missing_required_lib

from ansible_collections.netbox.netbox.plugins.module_utils.netbox_utils import (
    NetboxModule,
    ENDPOINT_NAME_MAPPING,
)

NB_CONFIG_CONTEXTS = "config_contexts"

class NetboxExtrasModule(NetboxModule):
    def __init__(self, module, endpoint):
        super().__init__(module, endpoint)

    def run(self):
        """
        This function should have all necessary code for endpoints within the application
        to create/update/delete the endpoint objects
        Supported endpoints:
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

        if data.get("regions"):
            regions = data["regions"]
            nb_app = getattr(self.nb, "dcim")
            nb_region = getattr(nb_app, "regions")
            regionids = []
            for region in regions:
                regionids.append(nb_region.get(slug=(region)).id)
                data["regions"] = regionids

        if data.get("sites"):
            sites = data["sites"]
            nb_app = getattr(self.nb, "dcim")
            nb_site = getattr(nb_app, "sites")
            siteids = []
            for site in sites:
                siteids.append(nb_site.get(slug=(site)).id)
                data["sites"] = siteids

        if data.get("roles"):
            roles = data["roles"]
            nb_app = getattr(self.nb, "dcim")
            nb_device_role = getattr(nb_app, "device_roles")
            roleids = []
            for role in roles:
                roleids.append(nb_device_role.get(slug=(device_role)).id)
                data["roles"] = roleids

        if data.get("platforms"):
            platforms = data["platforms"]
            nb_app = getattr(self.nb, "dcim")
            nb_platform = getattr(nb_app, "platforms")
            platformids = []
            for platform in platforms:
                platformids.append(nb_platform.get(slug=(platform)).id)
                data["platforms"] = platformids

        if data.get("cluster_groups"):
            cluster_groups = data["cluster_groups"]
            nb_app = getattr(self.nb, "virtualization")
            nb_cluster_group = getattr(nb_app, "cluster_groups")
            cluster_groupids = []
            for cluster_group in cluster_groups:
                cluster_groupids.append(nb_cluster_group.get(slug=(cluster_group)).id)
                data["cluster_groups"] = cluster_groupids

        if data.get("clusters"):
            clusters = data["clusters"]
            nb_app = getattr(self.nb, "virtualization")
            nb_cluster = getattr(nb_app, "clusters")
            clusterids = []
            for cluster in clusters:
                clusterids.append(nb_cluster.get(name=(cluster)).id)
                data["regions"] = regionids

        if data.get("tenant_groups"):
            tenant_groups = data["tenant_groups"]
            nb_app = getattr(self.nb, "tenancy")
            nb_tenant_group = getattr(nb_app, "tenant_groups")
            tenant_groupids = []
            for tenant_group in tenant_groups:
                tenant_groupids.append(nb_tenant_group.get(slug=(tenant_group)).id)
                data["tenant_groups"] = tenant_groupids

        if data.get("tenants"):
            tenants = data["tenants"]
            nb_app = getattr(self.nb, "tenancy")
            nb_tenant = getattr(nb_app, "tenants")
            tenantids = []
            for tenant in tenants:
                tenantids.append(nb_tenant.get(slug=(tenant)).id)
                data["tenants"] = tenantids

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

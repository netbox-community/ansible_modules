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


NB_TENANTS = "tenants"
NB_TENANT_GROUPS = "tenant_groups"
NB_CONTACTS = "contacts"
NB_CONTACT_ASSIGNMENTS = "contact_assignments"
NB_CONTACT_GROUPS = "contact_groups"
NB_CONTACT_ROLES = "contact_roles"


OBJECT_ENDPOINTS = {
    "circuit": "circuits",
    "cluster": "clusters",
    "cluster_group": "cluster_groups",
    "contact": "contacts",
    "contact_role": "contact_roles",
    "device": "devices",
    "location": "locations",
    "manufacturer": "manufacturers",
    "power_panel": "power_panels",
    "provider": "providers",
    "rack": "racks",
    "region": "regions",
    "site": "sites",
    "site_group": "site_groups",
    "tenant": "tenants",
    "virtual_machine": "virtual_machines",
}
# See https://netboxlabs.com/docs/netbox/features/contacts/#contacts-1
OBJECT_TYPES = {
    "circuit": "circuits.circuit",
    "cluster": "virtualization.cluster",
    "cluster_group": "virtualization.clustergroup",
    "device": "dcim.device",
    "location": "dcim.location",
    "manufacturer": "dcim.manufacturer",
    "power_panel": "dcim.powerpanel",
    "provider": "circuits.provider",
    "rack": "dcim.rack",
    "region": "dcim.region",
    "site": "dcim.site",
    "site_group": "dcim.sitegroup",
    "tenant": "tenancy.tenant",
    "virtual_machine": "virtualization.virtualmachine",
}
OBJECT_NAME_FIELD = {
    "circuit": "cid",
    # If unspecified, the default is "name"
}


class NetboxTenancyModule(NetboxModule):
    def __init__(self, module, endpoint):
        super().__init__(module, endpoint)

    def get_object_by_name(self, object_type: str, object_name: str):
        endpoint = OBJECT_ENDPOINTS[object_type]
        app = self._find_app(endpoint)
        nb_app = getattr(self.nb, app)
        nb_endpoint = getattr(nb_app, endpoint)

        name_field = OBJECT_NAME_FIELD.get(object_type)
        if name_field is None:
            name_field = "name"

        query_params = {name_field: object_name}
        result = self._nb_endpoint_get(nb_endpoint, query_params, object_name)
        if not result:
            self._handle_errors(
                msg="Could not resolve id of %s: %s" % (object_type, object_name)
            )
        return result

    def run(self):
        """
        This function should have all necessary code for endpoints within the application
        to create/update/delete the endpoint objects
        Supported endpoints:
        - tenants
        - tenant groups
        - contacts
        - contact assignments
        - contact groups
        - contact roles
        """
        # Used to dynamically set key when returning results
        endpoint_name = ENDPOINT_NAME_MAPPING[self.endpoint]

        self.result = {"changed": False}

        application = self._find_app(self.endpoint)
        nb_app = getattr(self.nb, application)
        nb_endpoint = getattr(nb_app, self.endpoint)
        user_query_params = self.module.params.get("query_params")

        data = self.data

        # For ease and consistency of use, the contact assignment module takes the name of the contact, role, and target object rather than an ID or slug.
        # We must massage the data a bit by looking up the ID corresponding to the given name so that we can pass the ID to the API.
        if self.endpoint == "contact_assignments":
            # Not an identifier, just to populate the message field
            name = f"{data['contact']} -> {data['object_name']}"

            object_type = data["object_type"]
            obj = self.get_object_by_name(object_type, data["object_name"])
            contact = self.get_object_by_name("contact", data["contact"])
            role = self.get_object_by_name("contact_role", data["role"])

            data["object_type"] = OBJECT_TYPES[object_type]
            data["object_id"] = obj.id
            del data["object_name"]  # object_id replaces object_name
            data["contact"] = contact.id
            data["role"] = role.id

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

        # For some reason, when creating a new contact assignment, role must be an ID
        # But when querying contact assignments, the role must be a slug
        if self.endpoint == "contact_assignments":
            object_query_params["role"] = role.slug

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

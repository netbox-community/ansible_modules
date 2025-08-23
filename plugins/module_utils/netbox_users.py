# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Daniel Chiquito (@dchiquito) <daniel.chiquito@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.netbox.netbox.plugins.module_utils.netbox_utils import (
    NetboxModule,
    ENDPOINT_NAME_MAPPING,
)

NB_GROUPS = "groups"
NB_PERMISSIONS = "permissions"
NB_TOKENS = "tokens"
NB_USERS = "users"

# These suboptions are lists, but need to be modeled as sets for comparison purposes.
LIST_AS_SET_KEYS = set(["permissions", "groups", "actions", "object_types"])


class NetboxUsersModule(NetboxModule):
    def __init__(self, module, endpoint):
        super().__init__(module, endpoint)

    def run(self):
        """
        This function should have all necessary code for endpoints within the
        application to create/update/delete the endpoint objects
        Supported endpoints:
        - groups
        - permissions
        - tokens
        - users
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
        if data.get("username"):
            name = data["username"]
        elif data.get("name"):
            name = data["name"]
        elif data.get("key"):
            name = data["key"]

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

    def _update_netbox_object(self, data):
        if self.endpoint == NB_TOKENS:
            return self._update_netbox_token(data)
        else:
            return self.__update_netbox_object__(data)

    def _update_netbox_token(self, data):
        if "key" in data:
            del data["key"]
        return self.__update_netbox_object__(data)

    def __update_netbox_object__(self, data):
        serialized_nb_obj = self.nb_object.serialize()
        updated_obj = serialized_nb_obj.copy()
        updated_obj.update(data)

        if serialized_nb_obj:
            for key in LIST_AS_SET_KEYS:
                if serialized_nb_obj.get(key) and data.get(key):
                    serialized_nb_obj[key] = set(serialized_nb_obj[key])
                    updated_obj[key] = set(data[key])

        if serialized_nb_obj == updated_obj:
            return serialized_nb_obj, None
        else:
            data_before, data_after = {}, {}
            for key in data:
                # Do not diff the password field
                if key == "password":
                    continue
                try:
                    if serialized_nb_obj[key] != updated_obj[key]:
                        data_before[key] = serialized_nb_obj[key]
                        data_after[key] = updated_obj[key]
                except KeyError:
                    msg = (
                        "%s does not exist on existing object. Check to make sure"
                        " valid field." % (key)
                    )
                    self._handle_errors(msg=msg)

            if not self.check_mode:
                if "password" in data:
                    # The initial response from Netbox obviously doesn't have a password field, so the nb_object also doesn't have a password field.
                    # Any fields that weren't on the initial response are ignored, so to update the password we must add the password field to the cache.
                    self.nb_object._add_cache(("password", ""))
                self.nb_object.update(data)
                updated_obj = self.nb_object.serialize()

            diff = self._build_diff(before=data_before, after=data_after)
            return updated_obj, diff

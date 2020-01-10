# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Mikhail Yohman (@fragmentedpacket) <mikhail.yohman@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

# This should just be temporary once 2.9 is relased and tested we can remove this
try:
    from ansible_collections.netbox_community.ansible_modules.plugins.module_utils.netbox_utils import (
        NetboxModule,
        ENDPOINT_NAME_MAPPING,
    )
except ImportError:
    import sys

    sys.path.append(".")
    from netbox_utils import NetboxModule, ENDPOINT_NAME_MAPPING


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

        data = self.data

        # Used for msg output
        name = data.get("name")

        data["slug"] = self._to_slug(name)

        object_query_params = self._build_query_params(endpoint_name, data)
        try:
            self.nb_object = nb_endpoint.get(**object_query_params)
        except ValueError:
            self._handle_errors(msg="More than one result returned for %s" % (name))

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

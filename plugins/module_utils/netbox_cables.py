# -*- coding: utf-8 -*-
# Copyright: (c) 2020, Kulakov Ilya (@TawR1024) <ilya@kulakov.ru.com>
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


NB_CABLES = "cables"


class NetboxCablesModule(NetboxModule):
    def __init__(self, module, endpoint):
        super().__init__(module, endpoint)

    def run(self):
        """
        This function should have all necessary code for endpoints within the application
        to create/update/delete the endpoint objects
        Supported endpoints:
        - cables
        """
        # Used to dynamically set key when returning results
        endpoint_name = ENDPOINT_NAME_MAPPING[self.endpoint]

        self.result = {"changed": False}

        application = self._find_app(self.endpoint)
        nb_app = getattr(self.nb, application)
        nb_endpoint = getattr(nb_app, self.endpoint)

        data = self.data #todo: replace user data with netbox data with ids

        sida_a_id = NetboxModule._temination_id(data['side_a_name'], data["side_a_port"])
        sida_b_id = NetboxModule._temination_id(data['side_b_name'], data["side_b_port"]) #todo fix termination id method

        del data["side_a_name"]
        del data["side_a_port"]
        del data["side_b_name"]
        del data["side_b_port"]
        data.apend({"termination_a_id":sida_a_id})
        data.apend({"termination_b_id":sida_b_id})
        '''side_a_name + side_a_port -- convert to termination_a_id'''
        '''side_b_name + side_b_port -- convert to termination_b_id'''

        object_query_params = self._build_query_params(endpoint_name, data)
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

# -*- coding: utf-8 -*-
# Copyright: (c) 2020, Hillsong, Douglas Heriot (@DouglasHeriot) <douglas.heriot@hillsong.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import pytest
import os
from functools import partial
from unittest.mock import patch, MagicMock, Mock

try:
    from ansible_collections.netbox.netbox.plugins.inventory.nb_inventory import (
        InventoryModule,
    )
    from ansible_collections.netbox.netbox.tests.test_data import load_test_data

except ImportError:
    import sys

    # Not installed as a collection
    # Try importing relative to root directory of this ansible_modules project

    sys.path.append("plugins/inventory")
    sys.path.append("tests")
    from nb_inventory import InventoryModule
    from test_data import load_test_data

load_relative_test_data = partial(load_test_data, os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture
def inventory_fixture():
    # TODO: Mock _fetch_information() to return static HTTP responses
    inventory = InventoryModule()
    inventory.api_endpoint = "https://netbox.test.endpoint:1234"
    return inventory


@pytest.fixture
def allowed_query_parameters_fixture():
    return ["a", "b", "c"]


@pytest.mark.parametrize("parameter, expected", load_relative_test_data("validate_query_parameter"))
def test_validate_query_parameter(
    inventory_fixture,
    allowed_query_parameters_fixture,
    parameter, expected):

    value = "some value, doesn't matter"
    result = inventory_fixture.validate_query_parameter({parameter: value}, allowed_query_parameters_fixture)
    assert (result == (parameter, value)) == expected


@pytest.mark.parametrize("parameters, expected", load_relative_test_data("filter_query_parameters"))
def test_filter_query_parameters(
    inventory_fixture,
    allowed_query_parameters_fixture,
    parameters, expected):

    result = inventory_fixture.filter_query_parameters(parameters, allowed_query_parameters_fixture)

    # Result is iterators of tuples
    # expected from json file is an array of dicts

    # Convert result iterator to list so we can get the length, and iterate over with an index
    result_list = list(result)

    assert len(result_list) == len(expected)

    for i, parameter in enumerate(result_list):
        assert parameter[0] == list(expected[i].keys())[0]
        assert parameter[1] == list(expected[i].values())[0]


@pytest.mark.parametrize("options, expected", load_relative_test_data("refresh_url"))
def test_refresh_url(inventory_fixture, options, expected):

    inventory_fixture.query_filters = options["query_filters"]
    inventory_fixture.device_query_filters = options["device_query_filters"]
    inventory_fixture.vm_query_filters = options["vm_query_filters"]
    inventory_fixture.config_context = options["config_context"]

    result = inventory_fixture.refresh_url()

    assert result == tuple(expected)

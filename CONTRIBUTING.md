# Contributing

The structure of the Netbox modules attempts to follow the layout of the Netbox API by having a module_util for each application (`dcim, ipam, tenancy, etc`) that inherits from a base module (`NetboxModule - netbox_utils.py`) and then implements the specific endpoints within the correct application module.

e.g. Add logic for adding devices under netbox_dcim.py or ip addresses under netbox_ipam.py

In turn when creating the actual modules, we're just calling a single function and passing in the Ansible Module and the endpoint. This means all the logic is within the specific application's module_util module and a lot of the logic should be the same for most endpoints since it is a basic operation of using the desired state of the endpoint and then either making sure it exists, updating it if it does exist, or removing it. There may be some special logic for other endpoints, but it should be minimal.

(Ansible Module) netbox_{{ endpoint }} -> (Module Util) netbox_{{ application }} -> (Module Util) netbox_utils

These modules are built using the pynetbox Python library which allows you to interact with Netbox using objects. Most of this is abstracted away when creating more modules, but something to be aware of. The reasoning for using underscores within the endpoint names is so the endpoints work with pynetbox.

An example of connecting to a Netbox instance and then choosing the application, endpoint, and operation:

```python
import pynetbox

nb = pynetbox.api("http://localhost:32768", "0123456789abcdef0123456789abcdef01234567")

# applications
nb.circuits
nb.dcim
nb.extras
nb.ipam
nb.secrets
nb.tenancy
nb.virtualization

# endpoints (small sample)
nb.circuits.providers
nb.dcim.devices
nb.dcim.device_types
nb.ipam.vrfs
nb.ipam.ip_addresses
nb.tenancy.tenant_groups

# operations
## Grabs a list of all endpoints
nb.dcim.devices.**all**
## Can pass a list of dicts to create multiple of the endpoints or just a dict to create a single endpoint
nb.dcim.devices.**create**
## Can filter to grab a name of the endpoint being filtered, not an object (Uses the same search criteria as the API)
nb.dcim.devices.**filter**
e.g. nb.dcim.devices.filter(name="test")
## Will retrieve the actual object that can be manipulated (updated, etc.) (Uses the same search criteria as the API)
nb.dcim.devices.**get**
e.g. nb.dcim.devices.get(name="test")

# Manipulate object after using .get
## Now you can manipulate the object the same as a Python object
device = nb.dcim.devices.get(name="test")
device.description = "Test Description"
## Patch operation (patches the data to the API)
device.save()

## If you were to just update the data in a fell swoop
serial = {"serial": "FXS10001", "description": "Test Description"}
## this operation will update the device and use the .save() method behind the scenes
device.update(serial)
```

## Adding an Endpoint

### Updating Variables within Module Utils

First thing is to setup several variables within **netbox_utils** and **netbox_application** module utils:

Check the following variable to make sure the endpoint is within the correct application within **netbox_utils**:

```python
API_APPS_ENDPOINTS = dict(
    circuits=[],
    dcim=[
        "devices",
        "device_roles",
        "device_types",
        "interfaces",
        "manufacturers",
        "platforms",
        "racks",
        "rack_groups",
        "rack_roles",
        "regions",
        "sites",
    ],
    extras=[],
    ipam=["ip_addresses", "prefixes", "roles", "vlans", "vlan_groups", "vrfs"],
    secrets=[],
    tenancy=["tenants", "tenant_groups"],
    virtualization=["clusters"],
)
```

Create a new variable in the **netbox_application** module until that matches the endpoint with any spaces being converted to underscores and all lowercase:

```python
NB_DEVICE_TYPES = "device_types"
```

Add the endpoint to the **run** method of supported endpoints:

```python
class NetboxDcimModule(NetboxModule):
    def __init__(self, module, endpoint):
        super().__init__(module, endpoint)

    def run(self):
        """
        This function should have all necessary code for endpoints within the application
        to create/update/delete the endpoint objects
        Supported endpoints:
        - device_types
```

Add the endpoint to the **ENDPOINT_NAME_MAPPING** variable within the **netbox_utils** module util.

```python
ENDPOINT_NAME_MAPPING = {
    "device_types": "device_type",
}
```

Log into your Netbox instance and navigate to `/api/docs` and searching for the **POST** documents for the given endpoint you're looking to create.
![POST Results](docs/media/postresults.PNG)
The module should implement all available fields that are not the **id** or **readOnly** such as the **created, last_updated, device_count** in the example above.

Add the endpoint to the **ALLOWED_QUERY_PARAMS** variable within the **netbox_utils** module util. This should be something unique for the endpoint and will be used within the **_build_query_params** method to dynamically build query params.

```python
ALLOWED_QUERY_PARAMS = {
    "device_type": set(["slug"]),
}
```

If the endpoint has a key that uses an **Array**, you will need to check the **_choices** of the application the endpoint is in and build those into **netbox_utils** module util.

```python
SUBDEVICE_ROLES = dict(parent=True, child=False)

REQUIRED_ID_FIND = {
    "device_types": [{"subdevice_role": SUBDEVICE_ROLES}],
}
# This is the method that uses the REQUIRED_ID_FIND variable (no change should be required within the method)
def _change_choices_id(self, endpoint, data):
    """Used to change data that is static and under _choices for the application.
    e.g. DEVICE_STATUS
    :returns data (dict): Returns the user defined data back with updated fields for _choices
    :params endpoint (str): The endpoint that will be used for mapping to required _choices
    :params data (dict): User defined data passed into the module
    """
    if REQUIRED_ID_FIND.get(endpoint):
        required_choices = REQUIRED_ID_FIND[endpoint]
        for choice in required_choices:
            for key, value in choice.items():
                if data.get(key):
                    try:
                        data[key] = value[data[key].lower()]
                    except KeyError:
                        self._handle_errors(
                            msg="%s may not be a valid choice. If it is valid, please submit bug report."
                            % (key)
                        )

    return data
```

If the key is something that pertains to a different endpoint such as **manufacturer** it will need to be added to a few variables within **netbox_utils**.

```python
CONVERT_TO_ID = dict(
    manufacturer="manufacturers",
)
QUERY_TYPES = dict(
    manufacturer="slug",
)
```

If **slug** and **name** is required, we should leave **slug** out as an option within the module docs and generate it dynamically. Add the endpoint to **SLUG_REQUIRED** within **netbox_utils** module util.

```python
SLUG_REQUIRED = {
    "device_roles",
    "ipam_roles",
    "rack_groups",
    "rack_roles",
    "roles",
    "manufacturers",
    "platforms",
    "vlan_groups",
}
```

Add code to the **netbox_application** module util to convert name to **slug**"

```python
if self.endpoint in SLUG_REQUIRED:
    if not data.get("slug"):
        data["slug"] = self._to_slug(name)
```

If either **role** or **group** are within the acceptable keys to POST to the endpoint, we should prefix it with the endpoint name. This is to prevent the code from trying to fetch an ID from the wrong endpoint.
Add the new key to **CONVERT_KEYS** within **netbox_utils** module util.

```python
CONVERT_KEYS = {
    "prefix_role": "role",
    "rack_group": "group",
    "rack_role": "role",
    "tenant_group": "group",
    "vlan_role": "role",
    "vlan_group": "group",
}

# Adding the method that uses this code (no change should be required within the method)
def _convert_identical_keys(self, data):
    """
    Used to change non-clashing keys for each module into identical keys that are required
    to be passed to pynetbox
    ex. rack_role back into role to pass to Netbox
    Returns data
    :params data (dict): Data dictionary after _find_ids method ran
    """
    for key in data:
        if key in CONVERT_KEYS:
            new_key = CONVERT_KEYS[key]
            value = data.pop(key)
            data[new_key] = value

    return data
```

#### Creating **netbox_endpoint** Module

Copying an existing module that has close to the same options is typically the path to least resistence and then updating portions of it to fit the new module.

- Change the author: `Copyright: (c) 2018, Mikhail Yohman (@FragmentedPacket) <mikhail.yohman@gmail.com>`
- Update the **DOCUMENTATION**/**EXAMPLES**/**RETURN** string with the necessary information
  - Main things are module, descriptions, author, version and the sub options under data
  - The **RETURN** should return the singluar of the endpoint name (done dynamically, but needs to be documented correctly)
- Update the module_util, module, and endpoint variable for the endpoint

  ```python
  from ansible_collections.netbox_community.ansible_modules.plugins.module_utils.netbox_dcim import (
      NetboxDcimModule,
      NB_DEVICE_ROLES,
  )
  ```

- Update the **main()** as necessary:

  ```python
  # Add if name is required or change to match required fields
  if not module.params["data"].get("name"):
      module.fail_json(msg="missing name")
  # Make sure the objects are endpoint name and the correct class and variable are being called for the endpoint
  netbox_device_role = NetboxDcimModule(module, NB_DEVICE_ROLES)
  netbox_device_role.run()
  ```

#### Testing

- Please update `tests/unit/module_utils/test_netbox_base_class.py` if editing anything within the base class that needs to be tested. This will most likely be needed as there are a few unit tests that test the data of **ALLOWED_QUERY_PARAMS**, etc.

  ```python
  def test_normalize_data_returns_correct_data()
  def test_find_app_returns_valid_app()
  def test_change_choices_id()
  def test_build_query_params_no_child()
  def test_build_query_params_child()
  ```

- Please add or update an existing play to test the new Netbox module for integration testing within `tests/integration/integration-tests.yml`. Make sure to test creation, duplicate, update (if possible), and deletion along with any other conditions that may want to be tested.
- Run `black .` within the base directory for black formatting as it's required for tests to pass
- Check necessary dependencies defined within `.travis.yml` for now if you're wanting to test locally

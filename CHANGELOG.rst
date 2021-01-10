===========================
Netbox.Netbox Release Notes
===========================

.. contents:: Topics


v1.2.1
======

Bugfixes
--------

- Allow IDs to be passed into objects that accept a list (https://github.com/netbox-community/ansible_modules/issues/407)

v1.2.0
======

Major Changes
-------------

- nb_inventory - Add ``dns_name`` option that adds ``dns_name`` to the host when ``True`` and device has a primary IP address. (#394)
- nb_inventory - Add ``status`` as a ``group_by`` option. (398)
- nb_inventory - Move around ``extracted_primary_ip`` to allow for ``config_context`` or ``custom_field`` to overwite. (#377)
- nb_inventory - Services are now a list of integers due to NetBox 2.10 changes. (#396)
- nb_lookup - Allow ID to be passed in and use ``.get`` instead of ``.filter``. (#376)
- nb_lookup - Allow ``api_endpoint`` and ``token`` to be found via env. (#391)

Minor Changes
-------------

- nb_inventory - Added ``status`` as host_var. (359)
- nb_inventory - Added documentation for using ``keyed_groups``. (#361)
- nb_inventory - Allow to use virtual chassis name instead of device name. (#383)
- nb_lookup - Allow lookup of plugin endpoints. (#360)
- nb_lookup - Documentation update to show Fully Qualified Collection Name (FQCN). (#355)
- netbox_service - Add ``ports`` option for NetBox 2.10+ and convert ``port`` to ``ports`` if NetBox 2.9 or lower. (#396)
- netbox_virtual_machine - Added ``comments`` option. (#380)
- netbox_virtual_machine - Added ``local_context_data`` option. (#357)

Bugfixes
--------

- Version checks were failing due to converting "2.10" to a float made it an integer of 2.1 which broke version related logic. (#396)
- netbox_device_interface - Fixed copy pasta in documentation. (#371)
- netbox_ip_address - Updated documentation to show that ``family`` option has been deprecated. (#388)
- netbox_utils - Fixed typo for ``circuits.circuittermination`` searches. (#367)
- netbox_utils - Skip all modifications to ``query_params`` when ``user_query_params`` is defined. (#389)
- netbox_vlan - Fixed uniqueness for vlan searches to add ``group``. (#386)

New Modules
-----------

- netbox.netbox.netbox_tag - Creates or removes tags from Netbox

v1.1.0
======

Minor Changes
-------------

- Add ``follow_redirects`` option to inventory plugin (https://github.com/netbox-community/ansible_modules/pull/323)

Bugfixes
--------

- Prevent inventory plugin from failing on 403 and print warning message (https://github.com/netbox-community/ansible_modules/pull/354)
- Update ``netbox_ip_address`` module to accept ``assigned_object`` to work with NetBox 2.9 (https://github.com/netbox-community/ansible_modules/pull/345)
- Update inventory plugin to properly associate IP address to interfaces with NetBox 2.9 (https://github.com/netbox-community/ansible_modules/pull/334)
- Update inventory plugin to work with tags with NetBox 2.9 (https://github.com/netbox-community/ansible_modules/pull/340)
- Update modules to be able to properly update tags to work with NetBox 2.9 (https://github.com/netbox-community/ansible_modules/pull/345)

v1.0.2
======

Bugfixes
--------

- Add ``virtual_machine_role=slug`` to ``QUERY_TYPES`` to properly search for Virtual Machine roles and not use the default ``q`` search (https://github.com/netbox-community/ansible_modules/pull/327)
- Remove ``device`` being ``required`` and implemented ``required_one_of`` to allow either ``device`` or ``virtual_machine`` to be specified for ``netbox_service`` (https://github.com/netbox-community/ansible_modules/pull/326)
- When tags specified, it prevents other data from being updated on the object. (https://github.com/netbox-community/ansible_modules/pull/325)

v1.0.1
======

Minor Changes
-------------

- Inventory - Add group_by option ``rack_role`` and ``rack_group``
- Inventory - Add group_by option ``services`` (https://github.com/netbox-community/ansible_modules/pull/286)

Bugfixes
--------

- Fix ``nb_inventory`` cache for ip addresses (https://github.com/netbox-community/ansible_modules/issues/276)
- Return HTTPError body output when encountering HTTP errors (https://github.com/netbox-community/ansible_modules/issues/294)

v1.0.0
======

Bugfixes
--------

- Fix query_dict for device_bay/interface_template to use ``devicetype_id`` (https://github.com/netbox-community/ansible_modules/issues/282)
- This expands the fix to all `_template` modules to use `devicetype_id` for the query_dict when attempting to resolve the search (https://github.com/netbox-community/ansible_modules/pull/300)

v0.3.1
======

Bugfixes
--------

- Default ``validate_certs`` to ``True`` (https://github.com/netbox-community/ansible_modules/issues/273)

v0.3.0
======

Minor Changes
-------------

- Add ``local_context_data`` and ``flatten_local_context_data`` option to ``nb_inventory`` (https://github.com/netbox-community/ansible_modules/pull/258)
- Add ``local_context_data`` option to ``netbox_device`` (https://github.com/netbox-community/ansible_modules/pull/258)
- Add ``virtual_chassis``, ``vc_position``, ``vc_priority`` to ``netbox_device`` options (https://github.com/netbox-community/ansible_modules/pull/251)

Breaking Changes / Porting Guide
--------------------------------

- To pass in integers via Ansible Jinja filters for a key in ``data`` that
  requires querying an endpoint is now done by making it a dictionary with
  an ``id`` key. The previous behavior was to just pass in an integer and
  it was converted when normalizing the data, but some people may have names
  that are all integers and those were being converted erroneously so we made
  the decision to change the method to convert to an integer for the NetBox
  API.

  ::

    tasks:
      - name: Create device within NetBox with only required information
        netbox_device:
          netbox_url: http://netbox-demo.org:32768
          netbox_token: 0123456789abcdef0123456789abcdef01234567
          data:
            name: Test66
            device_type:
              id: "{{ some_jinja_variable }}"
            device_role: Core Switch
            site: Test Site
            status: Staged
          state: present
- ``pynetbox`` changed to using ``requests.Session()`` to manage the HTTP session
  which broke passing in ``ssl_verify`` when building the NetBox API client.
  This PR makes ``pynetbox 5.0.4+`` the new required version of `pynetbox` for
  the Ansible modules and lookup plugin. (https://github.com/netbox-community/ansible_modules/pull/269)

Bugfixes
--------

- Allows OR operations in API fitlers for ``nb_lookup`` plugin (https://github.com/netbox-community/ansible_modules/issues/246)
- Build the ``rear_port`` and ``rear_port_template`` query_params to properly find rear port (https://github.com/netbox-community/ansible_modules/issues/262)
- Compares tags as a set to prevent issues with order difference between user supplied tags and NetBox API (https://github.com/netbox-community/ansible_modules/issues/242)
- Fixes typo for ``CONVERT_TO_ID`` mapping in ``netbox_utils`` for ``dcim.powerport`` and ``dcim.poweroutlet`` (https://github.com/netbox-community/ansible_modules/pull/265)
- Fixes typo for ``CONVERT_TO_ID`` mapping in ``netbox_utils`` for ``dcim.rearport`` (https://github.com/netbox-community/ansible_modules/pull/261)
- Normalize ``mac_address`` to upper case (https://github.com/netbox-community/ansible_modules/issues/254)
- Normalize descriptions to remove any extra whitespace (https://github.com/netbox-community/ansible_modules/issues/243)

New Modules
-----------

- netbox.netbox.netbox_cable - Create, update or delete cables within Netbox
- netbox.netbox.netbox_device_bay_template - Create, update or delete device bay templates within Netbox
- netbox.netbox.netbox_device_interface_template - Creates or removes interfaces on devices from Netbox
- netbox.netbox.netbox_virtual_chassis - Create, update or delete virtual chassis within Netbox

v0.2.3
======

Minor Changes
-------------

- Adds ``discovered`` field to ``netbox_inventory_item`` (https://github.com/netbox-community/ansible_modules/issues/187)
- Adds ``query_params`` to all modules to allow users to define the ``query_params`` (https://github.com/netbox-community/ansible_modules/issues/215)
- Adds ``tenant`` field to ``netbox_cluster`` (https://github.com/netbox-community/ansible_modules/pull/219)
- Allows private key to be passed in to ``validate_certs`` within modules (https://github.com/netbox-community/ansible_modules/issues/216)
- Better error handling if read-only token is provided for modules. Updated README as well to say that a ``write-enabled`` token is required (https://github.com/netbox-community/ansible_modules/pull/238)

Bugfixes
--------

- Fixes bug in ``netbox_prefix`` failing when using ``check_mode`` (https://github.com/netbox-community/ansible_modules/issues/228)
- Fixes bug in inventory plugin that fails if there are either no virtual machines, but devices defined in NetBox or vice versa from failing when ``fetch_all`` is set to ``False`` (https://github.com/netbox-community/ansible_modules/issues/214)
- Normalize any string values that are passed in via Jinja into an integer within the `_normalize_data` method (https://github.com/netbox-community/ansible_modules/issues/231)

New Modules
-----------

- netbox.netbox.netbox_console_port - Create, update or delete console ports within Netbox
- netbox.netbox.netbox_console_port_template - Create, update or delete console port templates within Netbox
- netbox.netbox.netbox_console_server_port - Create, update or delete console server ports within Netbox
- netbox.netbox.netbox_console_server_port_template - Create, update or delete console server port templates within Netbox
- netbox.netbox.netbox_front_port - Create, update or delete front ports within Netbox
- netbox.netbox.netbox_front_port_template - Create, update or delete front port templates within Netbox
- netbox.netbox.netbox_power_feed - Create, update or delete power feeds within Netbox
- netbox.netbox.netbox_power_outlet - Create, update or delete power outlets within Netbox
- netbox.netbox.netbox_power_outlet_template - Create, update or delete power outlet templates within Netbox
- netbox.netbox.netbox_power_panel - Create, update or delete power panels within Netbox
- netbox.netbox.netbox_power_port - Create, update or delete power ports within Netbox
- netbox.netbox.netbox_power_port_template - Create, update or delete power port templates within Netbox
- netbox.netbox.netbox_rear_port - Create, update or delete rear ports within Netbox
- netbox.netbox.netbox_rear_port_template - Create, update or delete rear port templates within Netbox

v0.2.2
======

Minor Changes
-------------

- Changed ``validate_certs`` to ``raw`` to allow private keys to be passed in (https://github.com/netbox-community/ansible_modules/issues/211)

Bugfixes
--------

- Added ``interfaces`` to ``ALLOWED_QUERY_PARAMS`` for ip addresses searches (https://github.com/netbox-community/ansible_modules/issues/201)
- Added ``type`` to ``ALLOWED_QUERY_PARAMS`` for interface searches (https://github.com/netbox-community/ansible_modules/issues/208)
- Remove ``rack`` as a choice when creating virtual machines (https://github.com/netbox-community/ansible_modules/pull/221)

v0.2.1
======

Minor Changes
-------------

- Added 21" width to netbox_rack (https://github.com/netbox-community/ansible_modules/pull/190)
- Added cluster, cluster_type, and cluster_group to group_by option in inventory plugin (https://github.com/netbox-community/ansible_modules/issues/188)
- Added option to change host_vars to singular rather than having single element lists (https://github.com/netbox-community/ansible_modules/issues/141)
- Added option to flatten ``config_context`` and ``custom_fields`` (https://github.com/netbox-community/ansible_modules/issues/193)

Bugfixes
--------

- Added ``type`` to ``netbox_device_interface`` and deprecation notice for ``form_factor`` (https://github.com/netbox-community/ansible_modules/issues/193)
- Fixes inventory performance issues, properly shows virtual chassis masters. (https://github.com/netbox-community/ansible_modules/pull/202)

v0.2.0
======

Minor Changes
-------------

- Add ``custom_fields`` to ``netbox_virtual_machine`` (https://github.com/netbox-community/ansible_modules/issues/170)
- Add ``device_query_filters`` and ``vm_query_filters`` to allow users to specify query filters for the specific type (https://github.com/netbox-community/ansible_modules/issues/140)
- Added ``group_names_raw`` option to the netbox inventory to allow users have the group names be the slug rather than prepending the group name with the type (https://github.com/netbox-community/ansible_modules/issues/138)
- Added ``raw_output`` option to netbox lookup plugin to return the exact output from the API with no doctoring (https://github.com/netbox-community/ansible_modules/pull/136)
- Added ``services`` option to the netbox inventory to allow users to toggle whether services are included or not (https://github.com/netbox-community/ansible_modules/pull/143)
- Added ``update_vc_child`` option to netbox_device_interface to allow child interfaces to be updated if device specified is the master device within the virtual chassis (https://github.com/netbox-community/ansible_modules/issues/105)
- Remove token from being required for nb_inventory as some NetBox setups don't require authorization for GET functions (https://github.com/netbox-community/ansible_modules/issues/177)
- Remove token from being required for nb_lookup as some NetBox setups don't require authorization for GET functions (https://github.com/netbox-community/ansible_modules/issues/183)

Breaking Changes / Porting Guide
--------------------------------

- Change ``ip-addresses`` key in netbox inventory plugin to ``ip_addresses`` (https://github.com/netbox-community/ansible_modules/issues/139)

Bugfixes
--------

- Allow integers to be passed in via Jinja string to properly convert back to integer (https://github.com/netbox-community/ansible_modules/issues/45)
- Allow services to be created with a different protocol (https://github.com/netbox-community/ansible_modules/issues/174)
- Properly find LAG if defined just as a string rather than dictionary with the relevant data (https://github.com/netbox-community/ansible_modules/issues/166)
- Removed choices within argument_spec for ``mode`` in ``netbox_device_interface`` and ``netbox_vm_interface``. This allows the API to return any error if an invalid choice is selected for ``mode`` (https://github.com/netbox-community/ansible_modules/issues/151)
- Updated rack width choices for latest NetBox version (https://github.com/netbox-community/ansible_modules/issues/167)

v0.1.10
=======

Bugfixes
--------

- Updated inventory plugin name from netbox.netbox.netbox to netbox.netbox.nb_inventory (https://github.com/netbox-community/ansible_modules/pull/129)

v0.1.9
======

Breaking Changes / Porting Guide
--------------------------------

- This version has a few breaking changes due to new namespace and collection name. I felt it necessary to change the name of the lookup plugin and inventory plugin just not to have a non descriptive namespace call to use them. Below is an example:
  ``netbox.netbox.netbox`` would be used for both inventory plugin and lookup plugin, but in different contexts so no collision will arise, but confusion will.
  I renamed the lookup plugin to ``nb_lookup`` so it will be used with the FQCN ``netbox.netbox.nb_lookup``.
  The inventory plugin will now be called within an inventory file by ``netbox.netbox.nb_inventory``

Bugfixes
--------

- Update ``netbox_tenant`` and ``netbox_tenant_group`` to use slugs for searching (available since NetBox 2.6). Added slug options to netbox_site, netbox_tenant, netbox_tenant_group (https://github.com/netbox-community/ansible_modules/pull/120)

v0.1.8
======

Bugfixes
--------

- If interface existed already, caused traceback and crashed playbook (https://github.com/netbox-community/ansible_modules/issues/114)

v0.1.7
======

Minor Changes
-------------

- Added fetching services for devices in Netbox Inventory Plugin (https://github.com/netbox-community/ansible_modules/issues/58)
- Added option for interfaces and IP addresses of interfaces to be fetched via inventory plugin (https://github.com/netbox-community/ansible_modules/issues/60)
- Change lookups to property for subclassing of inventory plugin (https://github.com/netbox-community/ansible_modules/issues/62)

Bugfixes
--------

- Assigning to parent log now finds LAG interface type dynamically rather than set statically in code (https://github.com/netbox-community/ansible_modules/issues/106)
- Create device with empty string to assign the device a UUID (https://github.com/netbox-community/ansible_modules/issues/107)
- If query_filters supplied are not allowed for either device or VM lookups, or no valid query filters, it will not attempt to fetch from devices or VMs. This should prevent devices or VMs from being fetched that do not meet the query_filters specified. (https://github.com/netbox-community/ansible_modules/issues/63)
- Properly create interface on correct device when in a VC (https://github.com/netbox-community/ansible_modules/issues/105)
- Updated _to_slug to follow same constructs NetBox uses (https://github.com/netbox-community/ansible_modules/issues/95)

v0.1.6
======

Minor Changes
-------------

- Add dns_name to netbox_ip_address (https://github.com/netbox-community/ansible_modules/issues/84)
- Add region and region_id to query_filter for Netbox Inventory plugin (https://github.com/netbox-community/ansible_modules/issues/83)

Bugfixes
--------

- Fixed vlan searching with vlan_group for netbox_prefix (https://github.com/netbox-community/ansible_modules/issues/85)
- Removed static choices from netbox_utils and now pulls the choices for each endpoint from the Netbox API at call time (https://github.com/netbox-community/ansible_modules/issues/67)

v0.1.5
======

Bugfixes
--------

- Add argument specs for every module to validate data passed in. Fixes some idempotency issues. POSSIBLE BREAKING CHANGE (https://github.com/netbox-community/ansible_modules/issues/68)
- Allow name updates to manufacturers (https://github.com/netbox-community/ansible_modules/issues/76)
- Builds slug for netbox_device_type from model which is now required and slug is optional. Model will be slugified if slug is not provided BREAKING CHANGE (https://github.com/netbox-community/ansible_modules/issues/77)
- Fail module with proper exception when connection to Netbox API cannot be established (https://github.com/netbox-community/ansible_modules/issues/80)
- netbox_device_interface Lag no longer has to be a dictionary and the value of the key can be the name of the LAG (https://github.com/netbox-community/ansible_modules/issues/81)
- netbox_ip_address If no address has no CIDR notation, it will convert it into a /32 and pass to Netbox. Fixes idempotency cidr notation is not provided (https://github.com/netbox-community/ansible_modules/issues/78)

New Modules
-----------

- netbox.netbox.netbox_service - Creates or removes service from Netbox

v0.1.3
======

Bugfixes
--------

- Add error handling for invalid key_file for lookup plugin (https://github.com/netbox-community/ansible_modules/issues/52)

v0.1.2
======

Bugfixes
--------

- Allow endpoint choices to be an integer of the choice rather than attempting to dynamically determine the choice ID (https://github.com/netbox-community/ansible_modules/issues/47)

v0.1.1
======

Bugfixes
--------

- Fixed issue with netbox_vm_interface where it would fail if different virtual machine had the same interface name (https://github.com/netbox-community/ansible_modules/issues/40)
- Updated netbox_ip_address to find interfaces on virtual machines correctly (https://github.com/netbox-community/ansible_modules/issues/40)

v0.1.0
======

Minor Changes
-------------

- Add ``primary_ip4/6`` to ``netbox_ip_address`` (https://github.com/netbox-community/ansible_modules/issues/10)

Breaking Changes / Porting Guide
--------------------------------

- Changed ``group`` to ``tenant_group`` in ``netbox_tenant.py`` (https://github.com/netbox-community/ansible_modules/issues/9)
- Changed ``role`` to ``prefix_role`` in ``netbox_prefix.py`` (https://github.com/netbox-community/ansible_modules/issues/9)
- Module failures when required fields arent provided (https://github.com/netbox-community/ansible_modules/issues/24)
- Renamed ``netbox_interface`` to ``netbox_device_interface`` (https://github.com/netbox-community/ansible_modules/issues/9)

New Modules
-----------

- netbox.netbox.netbox_aggregate - Creates or removes aggregates from Netbox
- netbox.netbox.netbox_circuit - Create, update or delete circuits within Netbox
- netbox.netbox.netbox_circuit_termination - Create, update or delete circuit terminations within Netbox
- netbox.netbox.netbox_circuit_type - Create, update or delete circuit types within Netbox
- netbox.netbox.netbox_cluster - Create, update or delete clusters within Netbox
- netbox.netbox.netbox_cluster_group - Create, update or delete cluster groups within Netbox
- netbox.netbox.netbox_cluster_type - Create, update or delete cluster types within Netbox
- netbox.netbox.netbox_device_bay - Create, update or delete device bays within Netbox
- netbox.netbox.netbox_device_role - Create, update or delete devices roles within Netbox
- netbox.netbox.netbox_device_type - Create, update or delete device types within Netbox
- netbox.netbox.netbox_inventory_item - Creates or removes inventory items from Netbox
- netbox.netbox.netbox_ipam_role - Creates or removes ipam roles from Netbox
- netbox.netbox.netbox_manufacturer - Create or delete manufacturers within Netbox
- netbox.netbox.netbox_platform - Create or delete platforms within Netbox
- netbox.netbox.netbox_provider - Create, update or delete providers within Netbox
- netbox.netbox.netbox_rack - Create, update or delete racks within Netbox
- netbox.netbox.netbox_rack_group - Create, update or delete racks groups within Netbox
- netbox.netbox.netbox_rack_role - Create, update or delete racks roles within Netbox
- netbox.netbox.netbox_region - Creates or removes regions from Netbox
- netbox.netbox.netbox_rir - Create, update or delete RIRs within Netbox
- netbox.netbox.netbox_tenant - Creates or removes tenants from Netbox
- netbox.netbox.netbox_tenant_group - Creates or removes tenant groups from Netbox
- netbox.netbox.netbox_virtual_machine - Create, update or delete virtual_machines within Netbox
- netbox.netbox.netbox_vlan - Create, update or delete vlans within Netbox
- netbox.netbox.netbox_vlan_group - Create, update or delete vlans groups within Netbox
- netbox.netbox.netbox_vm_interface - Creates or removes interfaces from virtual machines in Netbox
- netbox.netbox.netbox_vrf - Create, update or delete vrfs within Netbox

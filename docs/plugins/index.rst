.. meta::
  :antsibull-docs: 2.13.1


.. _plugins_in_netbox.netbox:

Netbox.Netbox
=============

Collection version 3.21.0

.. contents::
   :local:
   :depth: 1

Description
-----------

This is a collection of NetBox Ansible modules

**Authors:**

* Mikhail Yohman <mikhail.yohman@gmail.com>
* Martin Rødvand <martin@rodvand.net>

**Supported ansible-core versions:**

* 2.15.0 or newer

.. ansible-links::

  - title: "Issue Tracker"
    url: "https://github.com/netbox-community/ansible_modules/issues"
    external: true
  - title: "Repository (Sources)"
    url: "https://github.com/netbox-community/ansible_modules"
    external: true




.. toctree::
    :maxdepth: 1

Plugin Index
------------

These are the plugins in the netbox.netbox collection:


Modules
~~~~~~~

* :ansplugin:`netbox_aggregate module <netbox.netbox.netbox_aggregate#module>` -- Creates or removes aggregates from NetBox
* :ansplugin:`netbox_asn module <netbox.netbox.netbox_asn#module>` -- Create, update or delete ASNs within NetBox
* :ansplugin:`netbox_cable module <netbox.netbox.netbox_cable#module>` -- Create, update or delete cables within NetBox
* :ansplugin:`netbox_circuit module <netbox.netbox.netbox_circuit#module>` -- Create, update or delete circuits within NetBox
* :ansplugin:`netbox_circuit_termination module <netbox.netbox.netbox_circuit_termination#module>` -- Create, update or delete circuit terminations within NetBox
* :ansplugin:`netbox_circuit_type module <netbox.netbox.netbox_circuit_type#module>` -- Create, update or delete circuit types within NetBox
* :ansplugin:`netbox_cluster module <netbox.netbox.netbox_cluster#module>` -- Create, update or delete clusters within NetBox
* :ansplugin:`netbox_cluster_group module <netbox.netbox.netbox_cluster_group#module>` -- Create, update or delete cluster groups within NetBox
* :ansplugin:`netbox_cluster_type module <netbox.netbox.netbox_cluster_type#module>` -- Create, update or delete cluster types within NetBox
* :ansplugin:`netbox_config_context module <netbox.netbox.netbox_config_context#module>` -- Creates, updates or deletes configuration contexts within NetBox
* :ansplugin:`netbox_config_template module <netbox.netbox.netbox_config_template#module>` -- Creates or removes config templates from NetBox
* :ansplugin:`netbox_console_port module <netbox.netbox.netbox_console_port#module>` -- Create, update or delete console ports within NetBox
* :ansplugin:`netbox_console_port_template module <netbox.netbox.netbox_console_port_template#module>` -- Create, update or delete console port templates within NetBox
* :ansplugin:`netbox_console_server_port module <netbox.netbox.netbox_console_server_port#module>` -- Create, update or delete console server ports within NetBox
* :ansplugin:`netbox_console_server_port_template module <netbox.netbox.netbox_console_server_port_template#module>` -- Create, update or delete console server port templates within NetBox
* :ansplugin:`netbox_contact module <netbox.netbox.netbox_contact#module>` -- Creates or removes contacts from NetBox
* :ansplugin:`netbox_contact_group module <netbox.netbox.netbox_contact_group#module>` -- Creates or removes contact groups from NetBox
* :ansplugin:`netbox_contact_role module <netbox.netbox.netbox_contact_role#module>` -- Creates or removes contact roles from NetBox
* :ansplugin:`netbox_custom_field module <netbox.netbox.netbox_custom_field#module>` -- Creates, updates or deletes custom fields within NetBox
* :ansplugin:`netbox_custom_field_choice_set module <netbox.netbox.netbox_custom_field_choice_set#module>` -- Creates, updates or deletes custom field choice sets within Netbox
* :ansplugin:`netbox_custom_link module <netbox.netbox.netbox_custom_link#module>` -- Creates, updates or deletes custom links within NetBox
* :ansplugin:`netbox_device module <netbox.netbox.netbox_device#module>` -- Create, update or delete devices within NetBox
* :ansplugin:`netbox_device_bay module <netbox.netbox.netbox_device_bay#module>` -- Create, update or delete device bays within NetBox
* :ansplugin:`netbox_device_bay_template module <netbox.netbox.netbox_device_bay_template#module>` -- Create, update or delete device bay templates within NetBox
* :ansplugin:`netbox_device_interface module <netbox.netbox.netbox_device_interface#module>` -- Creates or removes interfaces on devices from NetBox
* :ansplugin:`netbox_device_interface_template module <netbox.netbox.netbox_device_interface_template#module>` -- Creates or removes interfaces on devices from NetBox
* :ansplugin:`netbox_device_role module <netbox.netbox.netbox_device_role#module>` -- Create, update or delete devices roles within NetBox
* :ansplugin:`netbox_device_type module <netbox.netbox.netbox_device_type#module>` -- Create, update or delete device types within NetBox
* :ansplugin:`netbox_export_template module <netbox.netbox.netbox_export_template#module>` -- Creates, updates or deletes export templates within NetBox
* :ansplugin:`netbox_fhrp_group module <netbox.netbox.netbox_fhrp_group#module>` -- Create, update or delete FHRP groups within NetBox
* :ansplugin:`netbox_fhrp_group_assignment module <netbox.netbox.netbox_fhrp_group_assignment#module>` -- Create, update or delete FHRP group assignments within NetBox
* :ansplugin:`netbox_front_port module <netbox.netbox.netbox_front_port#module>` -- Create, update or delete front ports within NetBox
* :ansplugin:`netbox_front_port_template module <netbox.netbox.netbox_front_port_template#module>` -- Create, update or delete front port templates within NetBox
* :ansplugin:`netbox_inventory_item module <netbox.netbox.netbox_inventory_item#module>` -- Creates or removes inventory items from NetBox
* :ansplugin:`netbox_inventory_item_role module <netbox.netbox.netbox_inventory_item_role#module>` -- Create, update or delete devices roles within NetBox
* :ansplugin:`netbox_ip_address module <netbox.netbox.netbox_ip_address#module>` -- Creates or removes IP addresses from NetBox
* :ansplugin:`netbox_ipam_role module <netbox.netbox.netbox_ipam_role#module>` -- Creates or removes ipam roles from NetBox
* :ansplugin:`netbox_journal_entry module <netbox.netbox.netbox_journal_entry#module>` -- Creates a journal entry
* :ansplugin:`netbox_l2vpn module <netbox.netbox.netbox_l2vpn#module>` -- Create, update or delete L2VPNs within NetBox
* :ansplugin:`netbox_l2vpn_termination module <netbox.netbox.netbox_l2vpn_termination#module>` -- Create, update or delete L2VPNs terminations within NetBox
* :ansplugin:`netbox_location module <netbox.netbox.netbox_location#module>` -- Create, update or delete locations within NetBox
* :ansplugin:`netbox_mac_address module <netbox.netbox.netbox_mac_address#module>` -- Create, update or delete MAC addresses within NetBox
* :ansplugin:`netbox_manufacturer module <netbox.netbox.netbox_manufacturer#module>` -- Create or delete manufacturers within NetBox
* :ansplugin:`netbox_module module <netbox.netbox.netbox_module#module>` -- Create, update or delete module within NetBox
* :ansplugin:`netbox_module_bay module <netbox.netbox.netbox_module_bay#module>` -- Create, update or delete module bay within NetBox
* :ansplugin:`netbox_module_type module <netbox.netbox.netbox_module_type#module>` -- Create, update or delete module types within NetBox
* :ansplugin:`netbox_permission module <netbox.netbox.netbox_permission#module>` -- Creates or removes permissions from NetBox
* :ansplugin:`netbox_platform module <netbox.netbox.netbox_platform#module>` -- Create or delete platforms within NetBox
* :ansplugin:`netbox_power_feed module <netbox.netbox.netbox_power_feed#module>` -- Create, update or delete power feeds within NetBox
* :ansplugin:`netbox_power_outlet module <netbox.netbox.netbox_power_outlet#module>` -- Create, update or delete power outlets within NetBox
* :ansplugin:`netbox_power_outlet_template module <netbox.netbox.netbox_power_outlet_template#module>` -- Create, update or delete power outlet templates within NetBox
* :ansplugin:`netbox_power_panel module <netbox.netbox.netbox_power_panel#module>` -- Create, update or delete power panels within NetBox
* :ansplugin:`netbox_power_port module <netbox.netbox.netbox_power_port#module>` -- Create, update or delete power ports within NetBox
* :ansplugin:`netbox_power_port_template module <netbox.netbox.netbox_power_port_template#module>` -- Create, update or delete power port templates within NetBox
* :ansplugin:`netbox_prefix module <netbox.netbox.netbox_prefix#module>` -- Creates or removes prefixes from NetBox
* :ansplugin:`netbox_provider module <netbox.netbox.netbox_provider#module>` -- Create, update or delete providers within NetBox
* :ansplugin:`netbox_provider_network module <netbox.netbox.netbox_provider_network#module>` -- Create, update or delete provider networks within NetBox
* :ansplugin:`netbox_rack module <netbox.netbox.netbox_rack#module>` -- Create, update or delete racks within NetBox
* :ansplugin:`netbox_rack_group module <netbox.netbox.netbox_rack_group#module>` -- Create, update or delete racks groups within NetBox
* :ansplugin:`netbox_rack_role module <netbox.netbox.netbox_rack_role#module>` -- Create, update or delete racks roles within NetBox
* :ansplugin:`netbox_rear_port module <netbox.netbox.netbox_rear_port#module>` -- Create, update or delete rear ports within NetBox
* :ansplugin:`netbox_rear_port_template module <netbox.netbox.netbox_rear_port_template#module>` -- Create, update or delete rear port templates within NetBox
* :ansplugin:`netbox_region module <netbox.netbox.netbox_region#module>` -- Creates or removes regions from NetBox
* :ansplugin:`netbox_rir module <netbox.netbox.netbox_rir#module>` -- Create, update or delete RIRs within NetBox
* :ansplugin:`netbox_route_target module <netbox.netbox.netbox_route_target#module>` -- Creates or removes route targets from NetBox
* :ansplugin:`netbox_service module <netbox.netbox.netbox_service#module>` -- Creates or removes service from NetBox
* :ansplugin:`netbox_service_template module <netbox.netbox.netbox_service_template#module>` -- Create, update or delete service templates within NetBox
* :ansplugin:`netbox_site module <netbox.netbox.netbox_site#module>` -- Creates or removes sites from NetBox
* :ansplugin:`netbox_site_group module <netbox.netbox.netbox_site_group#module>` -- Create, update, or delete site groups within NetBox
* :ansplugin:`netbox_tag module <netbox.netbox.netbox_tag#module>` -- Creates or removes tags from NetBox
* :ansplugin:`netbox_tenant module <netbox.netbox.netbox_tenant#module>` -- Creates or removes tenants from NetBox
* :ansplugin:`netbox_tenant_group module <netbox.netbox.netbox_tenant_group#module>` -- Creates or removes tenant groups from NetBox
* :ansplugin:`netbox_token module <netbox.netbox.netbox_token#module>` -- Creates or removes tokens from NetBox
* :ansplugin:`netbox_tunnel module <netbox.netbox.netbox_tunnel#module>` -- Create, update or delete tunnels within NetBox
* :ansplugin:`netbox_tunnel_group module <netbox.netbox.netbox_tunnel_group#module>` -- Create, update or delete tunnel groups within NetBox
* :ansplugin:`netbox_user module <netbox.netbox.netbox_user#module>` -- Creates or removes users from NetBox
* :ansplugin:`netbox_user_group module <netbox.netbox.netbox_user_group#module>` -- Creates or removes user groups from NetBox
* :ansplugin:`netbox_virtual_chassis module <netbox.netbox.netbox_virtual_chassis#module>` -- Create, update or delete virtual chassis within NetBox
* :ansplugin:`netbox_virtual_disk module <netbox.netbox.netbox_virtual_disk#module>` -- Creates or removes disks from virtual machines in NetBox
* :ansplugin:`netbox_virtual_machine module <netbox.netbox.netbox_virtual_machine#module>` -- Create, update or delete virtual\_machines within NetBox
* :ansplugin:`netbox_vlan module <netbox.netbox.netbox_vlan#module>` -- Create, update or delete vlans within NetBox
* :ansplugin:`netbox_vlan_group module <netbox.netbox.netbox_vlan_group#module>` -- Create, update or delete vlans groups within NetBox
* :ansplugin:`netbox_vm_interface module <netbox.netbox.netbox_vm_interface#module>` -- Creates or removes interfaces from virtual machines in NetBox
* :ansplugin:`netbox_vrf module <netbox.netbox.netbox_vrf#module>` -- Create, update or delete vrfs within NetBox
* :ansplugin:`netbox_webhook module <netbox.netbox.netbox_webhook#module>` -- Creates, updates or deletes webhook configuration within NetBox
* :ansplugin:`netbox_wireless_lan module <netbox.netbox.netbox_wireless_lan#module>` -- Creates or removes Wireless LANs from NetBox
* :ansplugin:`netbox_wireless_lan_group module <netbox.netbox.netbox_wireless_lan_group#module>` -- Creates or removes Wireless LAN Groups from NetBox
* :ansplugin:`netbox_wireless_link module <netbox.netbox.netbox_wireless_link#module>` -- Creates or removes Wireless links from NetBox

.. toctree::
    :maxdepth: 1
    :hidden:

    netbox_aggregate_module
    netbox_asn_module
    netbox_cable_module
    netbox_circuit_module
    netbox_circuit_termination_module
    netbox_circuit_type_module
    netbox_cluster_module
    netbox_cluster_group_module
    netbox_cluster_type_module
    netbox_config_context_module
    netbox_config_template_module
    netbox_console_port_module
    netbox_console_port_template_module
    netbox_console_server_port_module
    netbox_console_server_port_template_module
    netbox_contact_module
    netbox_contact_group_module
    netbox_contact_role_module
    netbox_custom_field_module
    netbox_custom_field_choice_set_module
    netbox_custom_link_module
    netbox_device_module
    netbox_device_bay_module
    netbox_device_bay_template_module
    netbox_device_interface_module
    netbox_device_interface_template_module
    netbox_device_role_module
    netbox_device_type_module
    netbox_export_template_module
    netbox_fhrp_group_module
    netbox_fhrp_group_assignment_module
    netbox_front_port_module
    netbox_front_port_template_module
    netbox_inventory_item_module
    netbox_inventory_item_role_module
    netbox_ip_address_module
    netbox_ipam_role_module
    netbox_journal_entry_module
    netbox_l2vpn_module
    netbox_l2vpn_termination_module
    netbox_location_module
    netbox_mac_address_module
    netbox_manufacturer_module
    netbox_module_module
    netbox_module_bay_module
    netbox_module_type_module
    netbox_permission_module
    netbox_platform_module
    netbox_power_feed_module
    netbox_power_outlet_module
    netbox_power_outlet_template_module
    netbox_power_panel_module
    netbox_power_port_module
    netbox_power_port_template_module
    netbox_prefix_module
    netbox_provider_module
    netbox_provider_network_module
    netbox_rack_module
    netbox_rack_group_module
    netbox_rack_role_module
    netbox_rear_port_module
    netbox_rear_port_template_module
    netbox_region_module
    netbox_rir_module
    netbox_route_target_module
    netbox_service_module
    netbox_service_template_module
    netbox_site_module
    netbox_site_group_module
    netbox_tag_module
    netbox_tenant_module
    netbox_tenant_group_module
    netbox_token_module
    netbox_tunnel_module
    netbox_tunnel_group_module
    netbox_user_module
    netbox_user_group_module
    netbox_virtual_chassis_module
    netbox_virtual_disk_module
    netbox_virtual_machine_module
    netbox_vlan_module
    netbox_vlan_group_module
    netbox_vm_interface_module
    netbox_vrf_module
    netbox_webhook_module
    netbox_wireless_lan_module
    netbox_wireless_lan_group_module
    netbox_wireless_link_module


Inventory Plugins
~~~~~~~~~~~~~~~~~

* :ansplugin:`nb_inventory inventory <netbox.netbox.nb_inventory#inventory>` -- NetBox inventory source

.. toctree::
    :maxdepth: 1
    :hidden:

    nb_inventory_inventory


Lookup Plugins
~~~~~~~~~~~~~~

* :ansplugin:`nb_lookup lookup <netbox.netbox.nb_lookup#lookup>` -- Queries and returns elements from NetBox

.. toctree::
    :maxdepth: 1
    :hidden:

    nb_lookup_lookup

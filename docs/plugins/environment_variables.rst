
:orphan:

.. _list_of_collection_env_vars:

Index of all Collection Environment Variables
=============================================

The following index documents all environment variables declared by plugins in collections.
Environment variables used by the ansible-core configuration are documented in :ref:`ansible_configuration_settings`.

.. envvar:: ANSIBLE_INVENTORY_USE_EXTRA_VARS

    Merge extra vars into the available variables for composition (highest precedence).

    *Used by:*
    :ref:`netbox.netbox.nb\_inventory inventory plugin <ansible_collections.netbox.netbox.nb_inventory_inventory>`
.. envvar:: NETBOX_API

    See the documentations for the options where this environment variable is used.

    *Used by:*
    :ref:`netbox.netbox.nb\_inventory inventory plugin <ansible_collections.netbox.netbox.nb_inventory_inventory>`,
    :ref:`netbox.netbox.nb\_lookup lookup plugin <ansible_collections.netbox.netbox.nb_lookup_lookup>`
.. envvar:: NETBOX_API_KEY

    NetBox API token to be able to read against NetBox.

    This may not be required depending on the NetBox setup.

    *Used by:*
    :ref:`netbox.netbox.nb\_inventory inventory plugin <ansible_collections.netbox.netbox.nb_inventory_inventory>`
.. envvar:: NETBOX_API_TOKEN

    The API token created through NetBox

    This may not be required depending on the NetBox setup.

    *Used by:*
    :ref:`netbox.netbox.nb\_lookup lookup plugin <ansible_collections.netbox.netbox.nb_lookup_lookup>`
.. envvar:: NETBOX_TOKEN

    See the documentations for the options where this environment variable is used.

    *Used by:*
    :ref:`netbox.netbox.nb\_inventory inventory plugin <ansible_collections.netbox.netbox.nb_inventory_inventory>`,
    :ref:`netbox.netbox.nb\_lookup lookup plugin <ansible_collections.netbox.netbox.nb_lookup_lookup>`
.. envvar:: NETBOX_URL

    The URL to the NetBox instance to query

    *Used by:*
    :ref:`netbox.netbox.nb\_lookup lookup plugin <ansible_collections.netbox.netbox.nb_lookup_lookup>`

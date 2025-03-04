:orphan:

.. meta::
  :antsibull-docs: 2.13.1

.. _list_of_collection_env_vars:

Index of all Collection Environment Variables
=============================================

The following index documents all environment variables declared by plugins in collections.
Environment variables used by the ansible-core configuration are documented in :ref:`ansible_configuration_settings`.

.. envvar:: ANSIBLE_INVENTORY_USE_EXTRA_VARS

    Merge extra vars into the available variables for composition (highest precedence).

    *Used by:*
    :ansplugin:`netbox.netbox.nb\_inventory inventory plugin <netbox.netbox.nb_inventory#inventory>`
.. envvar:: NETBOX_API

    See the documentations for the options where this environment variable is used.

    *Used by:*
    :ansplugin:`netbox.netbox.nb\_inventory inventory plugin <netbox.netbox.nb_inventory#inventory>`,
    :ansplugin:`netbox.netbox.nb\_lookup lookup plugin <netbox.netbox.nb_lookup#lookup>`
.. envvar:: NETBOX_API_KEY

    NetBox API token to be able to read against NetBox.

    This may not be required depending on the NetBox setup.

    You can provide a "type" and "value" for a token if your NetBox deployment is using a more advanced authentication like OAUTH.

    If you do not provide a "type" and "value" parameter, the HTTP authorization header will be set to "Token", which is the NetBox default

    *Used by:*
    :ansplugin:`netbox.netbox.nb\_inventory inventory plugin <netbox.netbox.nb_inventory#inventory>`
.. envvar:: NETBOX_API_TOKEN

    The API token created through NetBox

    This may not be required depending on the NetBox setup.

    *Used by:*
    :ansplugin:`netbox.netbox.nb\_lookup lookup plugin <netbox.netbox.nb_lookup#lookup>`
.. envvar:: NETBOX_HEADERS

    Dictionary of headers to be passed to the NetBox API.

    *Used by:*
    :ansplugin:`netbox.netbox.nb\_inventory inventory plugin <netbox.netbox.nb_inventory#inventory>`,
    :ansplugin:`netbox.netbox.nb\_lookup lookup plugin <netbox.netbox.nb_lookup#lookup>`
.. envvar:: NETBOX_TOKEN

    See the documentations for the options where this environment variable is used.

    *Used by:*
    :ansplugin:`netbox.netbox.nb\_inventory inventory plugin <netbox.netbox.nb_inventory#inventory>`,
    :ansplugin:`netbox.netbox.nb\_lookup lookup plugin <netbox.netbox.nb_lookup#lookup>`
.. envvar:: NETBOX_URL

    The URL to the NetBox instance to query

    *Used by:*
    :ansplugin:`netbox.netbox.nb\_lookup lookup plugin <netbox.netbox.nb_lookup#lookup>`

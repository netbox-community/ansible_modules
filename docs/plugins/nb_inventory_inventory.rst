.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.13.1

.. Anchors

.. _ansible_collections.netbox.netbox.nb_inventory_inventory:

.. Anchors: short name for ansible.builtin

.. Title

netbox.netbox.nb_inventory inventory -- NetBox inventory source
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This inventory plugin is part of the `netbox.netbox collection <https://galaxy.ansible.com/ui/repo/published/netbox/netbox/>`_ (version 3.21.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install netbox.netbox`.

    To use it in a playbook, specify: :code:`netbox.netbox.nb_inventory`.

.. version_added


.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Get inventory hosts from NetBox


.. Aliases


.. Requirements






.. Options

Parameters
----------

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ansible_host_dns_name"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-ansible_host_dns_name:

      .. rst-class:: ansible-option-title

      **ansible_host_dns_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ansible_host_dns_name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If True, sets DNS Name (fetched from primary\_ip) to be used in ansible\_host variable, instead of IP Address.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-api_endpoint"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-api_endpoint:

      .. rst-class:: ansible-option-title

      **api_endpoint**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-api_endpoint" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Endpoint of the NetBox API


      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - Environment variable: :envvar:`NETBOX\_API`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ca_path"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-ca_path:

      .. rst-class:: ansible-option-title

      **ca_path**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ca_path" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      CA path


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`false`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cache"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-cache:

      .. rst-class:: ansible-option-title

      **cache**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cache" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Toggle to enable/disable the caching of the inventory's source data, requires a cache plugin setup to work.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - INI entry:

        .. code-block::

          [inventory]
          cache = false


      - Environment variable: :envvar:`ANSIBLE\_INVENTORY\_CACHE`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cache_connection"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-cache_connection:

      .. rst-class:: ansible-option-title

      **cache_connection**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cache_connection" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Cache connection data or path, read cache plugin documentation for specifics.


      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - INI entries:

        .. code-block::

          [defaults]
          fact_caching_connection = VALUE



        .. code-block::

          [inventory]
          cache_connection = VALUE


      - Environment variable: :envvar:`ANSIBLE\_CACHE\_PLUGIN\_CONNECTION`

      - Environment variable: :envvar:`ANSIBLE\_INVENTORY\_CACHE\_CONNECTION`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cache_plugin"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-cache_plugin:

      .. rst-class:: ansible-option-title

      **cache_plugin**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cache_plugin" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Cache plugin to use for the inventory's source data.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"memory"`

      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - INI entries:

        .. code-block::

          [defaults]
          fact_caching = memory



        .. code-block::

          [inventory]
          cache_plugin = memory


      - Environment variable: :envvar:`ANSIBLE\_CACHE\_PLUGIN`

      - Environment variable: :envvar:`ANSIBLE\_INVENTORY\_CACHE\_PLUGIN`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cache_prefix"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-cache_prefix:

      .. rst-class:: ansible-option-title

      **cache_prefix**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cache_prefix" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Prefix to use for cache plugin files/tables.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"ansible\_inventory\_"`

      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - INI entries:

        .. code-block::

          [defaults]
          fact_caching_prefix = ansible_inventory_



        .. code-block::

          [inventory]
          cache_prefix = ansible_inventory_


      - Environment variable: :envvar:`ANSIBLE\_CACHE\_PLUGIN\_PREFIX`

      - Environment variable: :envvar:`ANSIBLE\_INVENTORY\_CACHE\_PLUGIN\_PREFIX`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cache_timeout"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-cache_timeout:

      .. rst-class:: ansible-option-title

      **cache_timeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cache_timeout" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Cache duration in seconds.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`3600`

      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - INI entries:

        .. code-block::

          [defaults]
          fact_caching_timeout = 3600



        .. code-block::

          [inventory]
          cache_timeout = 3600


      - Environment variable: :envvar:`ANSIBLE\_CACHE\_PLUGIN\_TIMEOUT`

      - Environment variable: :envvar:`ANSIBLE\_INVENTORY\_CACHE\_TIMEOUT`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cert"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-cert:

      .. rst-class:: ansible-option-title

      **cert**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cert" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Certificate path


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`false`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-compose"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-compose:

      .. rst-class:: ansible-option-title

      **compose**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-compose" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of custom ansible host vars to create from the device object fetched from NetBox


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`{}`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-config_context"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-config_context:

      .. rst-class:: ansible-option-title

      **config_context**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-config_context" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If True, it adds config\_context in host vars.

      Config-context enables the association of arbitrary data to devices and virtual machines grouped by region, site, role, platform, and/or tenant. Please check official netbox docs for more info.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-device_query_filters"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-device_query_filters:

      .. rst-class:: ansible-option-title

      **device_query_filters**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-device_query_filters" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of parameters passed to the query string for devices (Multiple values may be separated by commas).

      You can also use Jinja2 templates.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dns_name"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-dns_name:

      .. rst-class:: ansible-option-title

      **dns_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dns_name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Force IP Addresses to be fetched so that the dns\_name for the primary\_ip of each device or VM is set as a host\_var.

      Setting interfaces will also fetch IP addresses and the dns\_name host\_var will be set.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-fetch_all"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-fetch_all:

      .. rst-class:: ansible-option-title

      **fetch_all**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-fetch_all" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      :ansible-option-versionadded:`added in netbox.netbox 0.2.1`





      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      By default, fetching interfaces and services will get all of the contents of NetBox regardless of query\_filters applied to devices and VMs.

      When set to False, separate requests will be made fetching interfaces, services, and IP addresses for each device\_id and virtual\_machine\_id.

      If you are using the various query\_filters options to reduce the number of devices, you may find querying NetBox faster with fetch\_all set to False.

      For efficiency, when False, these requests will be batched, for example /api/dcim/interfaces?limit=0&device\_id=1&device\_id=2&device\_id=3

      These GET request URIs can become quite large for a large number of devices. If you run into HTTP 414 errors, you can adjust the max\_uri\_length option to suit your web server.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-flatten_config_context"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-flatten_config_context:

      .. rst-class:: ansible-option-title

      **flatten_config_context**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-flatten_config_context" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      :ansible-option-versionadded:`added in netbox.netbox 0.2.1`





      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If :emphasis:`config\_context` is enabled, by default it's added as a host var named config\_context.

      If flatten\_config\_context is set to True, the config context variables will be added directly to the host instead.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-flatten_custom_fields"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-flatten_custom_fields:

      .. rst-class:: ansible-option-title

      **flatten_custom_fields**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-flatten_custom_fields" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      :ansible-option-versionadded:`added in netbox.netbox 0.2.1`





      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      By default, host custom fields are added as a dictionary host var named custom\_fields.

      If flatten\_custom\_fields is set to True, the fields will be added directly to the host instead.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-flatten_local_context_data"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-flatten_local_context_data:

      .. rst-class:: ansible-option-title

      **flatten_local_context_data**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-flatten_local_context_data" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      :ansible-option-versionadded:`added in netbox.netbox 0.3.0`





      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If :emphasis:`local\_context\_data` is enabled, by default it's added as a host var named local\_context\_data.

      If flatten\_local\_context\_data is set to True, the config context variables will be added directly to the host instead.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-follow_redirects"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-follow_redirects:

      .. rst-class:: ansible-option-title

      **follow_redirects**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-follow_redirects" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Determine how redirects are followed.

      By default, :emphasis:`follow\_redirects` is set to uses urllib2 default behavior.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"urllib2"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"all"`
      - :ansible-option-choices-entry:`"yes"`
      - :ansible-option-choices-entry:`"safe"`
      - :ansible-option-choices-entry:`"none"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-group_by"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-group_by:

      .. rst-class:: ansible-option-title

      **group_by**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-group_by" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Keys used to create groups. The :emphasis:`plurals` and :emphasis:`racks` options control which of these are valid.

      :emphasis:`rack\_group` is supported on NetBox versions 2.10 or lower only

      :emphasis:`location` is supported on NetBox versions 2.11 or higher only


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"sites"`
      - :ansible-option-choices-entry:`"site"`
      - :ansible-option-choices-entry:`"location"`
      - :ansible-option-choices-entry:`"tenants"`
      - :ansible-option-choices-entry:`"tenant"`
      - :ansible-option-choices-entry:`"racks"`
      - :ansible-option-choices-entry:`"rack"`
      - :ansible-option-choices-entry:`"rack\_group"`
      - :ansible-option-choices-entry:`"rack\_role"`
      - :ansible-option-choices-entry:`"tags"`
      - :ansible-option-choices-entry:`"tag"`
      - :ansible-option-choices-entry:`"device\_roles"`
      - :ansible-option-choices-entry:`"role"`
      - :ansible-option-choices-entry:`"device\_types"`
      - :ansible-option-choices-entry:`"device\_type"`
      - :ansible-option-choices-entry:`"manufacturers"`
      - :ansible-option-choices-entry:`"manufacturer"`
      - :ansible-option-choices-entry:`"platforms"`
      - :ansible-option-choices-entry:`"platform"`
      - :ansible-option-choices-entry:`"region"`
      - :ansible-option-choices-entry:`"site\_group"`
      - :ansible-option-choices-entry:`"cluster"`
      - :ansible-option-choices-entry:`"cluster\_type"`
      - :ansible-option-choices-entry:`"cluster\_group"`
      - :ansible-option-choices-entry:`"is\_virtual"`
      - :ansible-option-choices-entry:`"services"`
      - :ansible-option-choices-entry:`"status"`
      - :ansible-option-choices-entry:`"time\_zone"`
      - :ansible-option-choices-entry:`"utc\_offset"`
      - :ansible-option-choices-entry:`"facility"`


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-group_names_raw"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-group_names_raw:

      .. rst-class:: ansible-option-title

      **group_names_raw**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-group_names_raw" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      :ansible-option-versionadded:`added in netbox.netbox 0.2.0`





      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Will not add the group\_by choice name to the group names


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-groups"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-groups:

      .. rst-class:: ansible-option-title

      **groups**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-groups" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Add hosts to group based on Jinja2 conditionals.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`{}`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-headers"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-headers:

      .. rst-class:: ansible-option-title

      **headers**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-headers" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Dictionary of headers to be passed to the NetBox API.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`{}`

      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - Environment variable: :envvar:`NETBOX\_HEADERS`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-hostname_field"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-hostname_field:

      .. rst-class:: ansible-option-title

      **hostname_field**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-hostname_field" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      By default, the inventory hostname is the netbox device name

      If set, sets the inventory hostname from this field in custom\_fields instead


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`false`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-interfaces"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-interfaces:

      .. rst-class:: ansible-option-title

      **interfaces**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-interfaces" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      :ansible-option-versionadded:`added in netbox.netbox 0.1.7`





      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If True, it adds the device or virtual machine interface information in host vars.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-key"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-key:

      .. rst-class:: ansible-option-title

      **key**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-key" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Certificate key path


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`false`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-keyed_groups"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-keyed_groups:

      .. rst-class:: ansible-option-title

      **keyed_groups**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-keyed_groups" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Add hosts to group based on the values of a variable.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-keyed_groups/default_value"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-keyed_groups/default_value:

      .. rst-class:: ansible-option-title

      **default_value**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-keyed_groups/default_value" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      :ansible-option-versionadded:`added in ansible-core 2.12`





      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The default value when the host variable's value is an empty string.

      This option is mutually exclusive with :ansopt:`netbox.netbox.nb\_inventory#inventory:keyed\_groups[].trailing\_separator`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-keyed_groups/key"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-keyed_groups/key:

      .. rst-class:: ansible-option-title

      **key**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-keyed_groups/key" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The key from input dictionary used to generate groups.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-keyed_groups/parent_group"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-keyed_groups/parent_group:

      .. rst-class:: ansible-option-title

      **parent_group**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-keyed_groups/parent_group" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      parent group for keyed group.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-keyed_groups/prefix"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-keyed_groups/prefix:

      .. rst-class:: ansible-option-title

      **prefix**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-keyed_groups/prefix" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      A keyed group name will start with this prefix.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-keyed_groups/separator"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-keyed_groups/separator:

      .. rst-class:: ansible-option-title

      **separator**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-keyed_groups/separator" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      separator used to build the keyed group name.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"\_"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-keyed_groups/trailing_separator"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-keyed_groups/trailing_separator:

      .. rst-class:: ansible-option-title

      **trailing_separator**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-keyed_groups/trailing_separator" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      :ansible-option-versionadded:`added in ansible-core 2.12`





      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Set this option to :ansval:`false` to omit the :ansopt:`netbox.netbox.nb\_inventory#inventory:keyed\_groups[].separator` after the host variable when the value is an empty string.

      This option is mutually exclusive with :ansopt:`netbox.netbox.nb\_inventory#inventory:keyed\_groups[].default\_value`.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-leading_separator"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-leading_separator:

      .. rst-class:: ansible-option-title

      **leading_separator**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-leading_separator" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      :ansible-option-versionadded:`added in ansible-core 2.11`





      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Use in conjunction with :ansopt:`netbox.netbox.nb\_inventory#inventory:keyed\_groups`.

      By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.

      This is because the default prefix is :ansval:`""` and the default separator is :ansval:`"\_"`.

      Set this option to :ansval:`false` to omit the leading underscore (or other separator) if no prefix is given.

      If the group name is derived from a mapping the separator is still used to concatenate the items.

      To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-max_uri_length"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-max_uri_length:

      .. rst-class:: ansible-option-title

      **max_uri_length**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-max_uri_length" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      :ansible-option-versionadded:`added in netbox.netbox 0.2.1`





      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      When fetch\_all is False, GET requests to NetBox may become quite long and return a HTTP 414 (URI Too Long).

      You can adjust this option to be smaller to avoid 414 errors, or larger for a reduced number of requests.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`4000`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-oob_ip_as_primary_ip"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-oob_ip_as_primary_ip:

      .. rst-class:: ansible-option-title

      **oob_ip_as_primary_ip**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-oob_ip_as_primary_ip" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Use out of band IP as \`ansible host\`


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-plugin"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-plugin:

      .. rst-class:: ansible-option-title

      **plugin**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-plugin" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      token that ensures this is a source file for the 'netbox' plugin.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"netbox.netbox.nb\_inventory"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-plurals"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-plurals:

      .. rst-class:: ansible-option-title

      **plurals**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-plurals" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      :ansible-option-versionadded:`added in netbox.netbox 0.2.1`





      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If True, all host vars are contained inside single-element arrays for legacy compatibility with old versions of this plugin.

      Group names will be plural (ie. "sites\_mysite" instead of "site\_mysite")

      The choices of :emphasis:`group\_by` will be changed by this option.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-prefixes"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-prefixes:

      .. rst-class:: ansible-option-title

      **prefixes**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-prefixes" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      :ansible-option-versionadded:`added in netbox.netbox 3.5.0`





      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If True, it adds the device or virtual machine prefixes to hostvars nested under "site".

      Must match selection for "site\_data", as this changes the structure of "site" in hostvars


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-query_filters"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-query_filters:

      .. rst-class:: ansible-option-title

      **query_filters**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-query_filters" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of parameters passed to the query string for both devices and VMs (Multiple values may be separated by commas).

      You can also use Jinja2 templates.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-racks"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-racks:

      .. rst-class:: ansible-option-title

      **racks**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-racks" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      :ansible-option-versionadded:`added in netbox.netbox 3.6.0`





      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If False, skip querying the racks for information, which can be slow with great amounts of racks.

      The choices of :emphasis:`group\_by` will be changed by this option.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-rename_variables"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-rename_variables:

      .. rst-class:: ansible-option-title

      **rename_variables**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-rename_variables" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Rename variables evaluated by nb\_inventory, before writing them.

      Each list entry contains a dict with a 'pattern' and a 'repl'.

      Both 'pattern' and 'repl' are regular expressions.

      The first matching expression is used, subsequent matches are ignored.

      Internally \`re.sub\` is used.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-services"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-services:

      .. rst-class:: ansible-option-title

      **services**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-services" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      :ansible-option-versionadded:`added in netbox.netbox 0.2.0`





      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If True, it adds the device or virtual machine services information in host vars.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-site_data"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-site_data:

      .. rst-class:: ansible-option-title

      **site_data**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-site_data" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      :ansible-option-versionadded:`added in netbox.netbox 3.5.0`





      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If True, sites' full data structures returned from Netbox API are included in host vars.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-strict"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-strict:

      .. rst-class:: ansible-option-title

      **strict**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-strict" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If :ansval:`yes` make invalid entries a fatal error, otherwise skip and continue.

      Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-timeout"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-timeout:

      .. rst-class:: ansible-option-title

      **timeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-timeout" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Timeout for NetBox requests in seconds


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`60`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-token"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-token:

      .. rst-class:: ansible-option-title

      **token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-token" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      NetBox API token to be able to read against NetBox.

      This may not be required depending on the NetBox setup.

      You can provide a "type" and "value" for a token if your NetBox deployment is using a more advanced authentication like OAUTH.

      If you do not provide a "type" and "value" parameter, the HTTP authorization header will be set to "Token", which is the NetBox default


      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - Environment variable: :envvar:`NETBOX\_TOKEN`

      - Environment variable: :envvar:`NETBOX\_API\_KEY`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-use_extra_vars"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-use_extra_vars:

      .. rst-class:: ansible-option-title

      **use_extra_vars**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-use_extra_vars" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      :ansible-option-versionadded:`added in ansible-core 2.11`





      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Merge extra vars into the available variables for composition (highest precedence).


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - INI entry:

        .. code-block::

          [inventory_plugins]
          use_extra_vars = false


      - Environment variable: :envvar:`ANSIBLE\_INVENTORY\_USE\_EXTRA\_VARS`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-validate_certs:

      .. rst-class:: ansible-option-title

      **validate_certs**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Allows connection when SSL certificates are not valid. Set to :literal:`false` when certificates are not trusted.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-virtual_chassis_name"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-virtual_chassis_name:

      .. rst-class:: ansible-option-title

      **virtual_chassis_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-virtual_chassis_name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      When a device is part of a virtual chassis, use the virtual chassis name as the Ansible inventory hostname.

      The host var values will be from the virtual chassis master.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-virtual_disks"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-virtual_disks:

      .. rst-class:: ansible-option-title

      **virtual_disks**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-virtual_disks" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      :ansible-option-versionadded:`added in netbox.netbox 3.18.0`





      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If True, it adds the virtual disks information in host vars.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-vm_query_filters"></div>

      .. _ansible_collections.netbox.netbox.nb_inventory_inventory__parameter-vm_query_filters:

      .. rst-class:: ansible-option-title

      **vm_query_filters**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-vm_query_filters" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of parameters passed to the query string for VMs (Multiple values may be separated by commas).

      You can also use Jinja2 templates.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    # netbox_inventory.yml file in YAML format
    # Example command line: ansible-inventory -v --list -i netbox_inventory.yml

    plugin: netbox.netbox.nb_inventory
    api_endpoint: http://localhost:8000
    validate_certs: true
    config_context: false
    group_by:
      - device_roles
    query_filters:
      - role: network-edge-router
    device_query_filters:
      - has_primary_ip: 'true'
      - tenant__n: internal
    headers:
      Cookie: "{{ auth_cookie }}"

    # has_primary_ip is a useful way to filter out patch panels and other passive devices
    # Adding '__n' to a field searches for the negation of the value.
    # The above searches for devices that are NOT "tenant = internal"

    # Query filters are passed directly as an argument to the fetching queries.
    # You can repeat tags in the query string.

    query_filters:
      - role: server
      - tag: web
      - tag: production

    # See the NetBox documentation at https://netbox.readthedocs.io/en/stable/rest-api/overview/
    # the query_filters work as a logical **OR**
    #
    # Prefix any custom fields with cf_ and pass the field value with the regular NetBox query string

    query_filters:
      - cf_foo: bar

    # NetBox inventory plugin also supports Constructable semantics
    # You can fill your hosts vars using the compose option:

    plugin: netbox.netbox.nb_inventory
    compose:
      foo: last_updated
      bar: display_name
      nested_variable: rack.display_name

    # You can use keyed_groups to group on properties of devices or VMs.
    # NOTE: It's only possible to key off direct items on the device/VM objects.
    plugin: netbox.netbox.nb_inventory
    keyed_groups:
      - prefix: status
        key: status.value

    # For use in Ansible Tower (AWX), please see this blog from RedHat: https://www.ansible.com/blog/using-an-inventory-plugin-from-a-collection-in-ansible-tower
    # The credential for NetBox will need to expose NETBOX_API and NETBOX_TOKEN as environment variables.
    # Example Ansible Tower credential Input Configuration:

    fields:
      - id: NETBOX_API
        type: string
        label: NetBox Host URL
      - id: NETBOX_TOKEN
        type: string
        label: NetBox API Token
        secret: true
    required:
      - NETBOX_API
      - NETBOX_TOKEN

    # Example Ansible Tower credential Injector Configuration:

    env:
      NETBOX_API: '{{ NETBOX_API }}'
      NETBOX_TOKEN: '{{ NETBOX_TOKEN }}'

    # Example of time_zone and utc_offset usage

    plugin: netbox.netbox.nb_inventory
    api_endpoint: http://localhost:8000
    token: <insert token>
    validate_certs: true
    config_context: true
    group_by:
      - site
      - role
      - time_zone
      - utc_offset
    device_query_filters:
      - has_primary_ip: 'true'
      - manufacturer_id: 1

    # using group by time_zone, utc_offset it will group devices in ansible groups depending on time zone configured on site.
    # time_zone gives grouping like:
    # - "time_zone_Europe_Bucharest"
    # - "time_zone_Europe_Copenhagen"
    # - "time_zone_America_Denver"
    # utc_offset gives grouping like:
    # - "time_zone_utc_minus_7"
    # - "time_zone_utc_plus_1"
    # - "time_zone_utc_plus_10"

    # Example of using a token type

    plugin: netbox.netbox.nb_inventory
    api_endpoint: http://localhost:8000
    token:
      type: Bearer
      value: test123456



.. Facts


.. Return values


..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Remy Leone (@sieben)
- Anthony Ruhier (@Anthony25)
- Nikhil Singh Baliyan (@nikkytub)
- Sander Steffann (@steffann)
- Douglas Heriot (@DouglasHeriot)
- Thore Knickrehm (@tkn2023)


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. ansible-links::

  - title: "Issue Tracker"
    url: "https://github.com/netbox-community/ansible_modules/issues"
    external: true
  - title: "Repository (Sources)"
    url: "https://github.com/netbox-community/ansible_modules"
    external: true


.. Parsing errors

.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.netbox.netbox.nb_inventory_inventory:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

netbox.netbox.nb_inventory -- NetBox inventory source
+++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `netbox.netbox collection <https://galaxy.ansible.com/netbox/netbox>`_ (version 3.3.0).

    To install it use: :code:`ansible-galaxy collection install netbox.netbox`.

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

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                            <th>Configuration</th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-ansible_host_dns_name"></div>
                    <b>ansible_host_dns_name</b>
                    <a class="ansibleOptionLink" href="#parameter-ansible_host_dns_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>If True, sets DNS Name (fetched from primary_ip) to be used in ansible_host variable, instead of IP Address.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-api_endpoint"></div>
                    <b>api_endpoint</b>
                    <a class="ansibleOptionLink" href="#parameter-api_endpoint" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                            <div>
                                env:NETBOX_API
                                                                                            </div>
                                                                    </td>
                                                <td>
                                            <div>Endpoint of the NetBox API</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-ca_path"></div>
                    <b>ca_path</b>
                    <a class="ansibleOptionLink" href="#parameter-ca_path" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">"no"</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>CA path</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-cache"></div>
                    <b>cache</b>
                    <a class="ansibleOptionLink" href="#parameter-cache" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [inventory]<br>cache = no
                                                                                                                    </p>
                                                            </div>
                                                                            <div>
                                env:ANSIBLE_INVENTORY_CACHE
                                                                                            </div>
                                                                    </td>
                                                <td>
                                            <div>Toggle to enable/disable the caching of the inventory&#x27;s source data, requires a cache plugin setup to work.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-cache_connection"></div>
                    <b>cache_connection</b>
                    <a class="ansibleOptionLink" href="#parameter-cache_connection" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [defaults]<br>fact_caching_connection = None
                                                                                                                    </p>
                                                                    <p>
                                        [inventory]<br>cache_connection = None
                                                                                                                    </p>
                                                            </div>
                                                                            <div>
                                env:ANSIBLE_CACHE_PLUGIN_CONNECTION
                                                                                            </div>
                                                    <div>
                                env:ANSIBLE_INVENTORY_CACHE_CONNECTION
                                                                                            </div>
                                                                    </td>
                                                <td>
                                            <div>Cache connection data or path, read cache plugin documentation for specifics.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-cache_plugin"></div>
                    <b>cache_plugin</b>
                    <a class="ansibleOptionLink" href="#parameter-cache_plugin" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"memory"</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [defaults]<br>fact_caching = memory
                                                                                                                    </p>
                                                                    <p>
                                        [inventory]<br>cache_plugin = memory
                                                                                                                    </p>
                                                            </div>
                                                                            <div>
                                env:ANSIBLE_CACHE_PLUGIN
                                                                                            </div>
                                                    <div>
                                env:ANSIBLE_INVENTORY_CACHE_PLUGIN
                                                                                            </div>
                                                                    </td>
                                                <td>
                                            <div>Cache plugin to use for the inventory&#x27;s source data.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-cache_prefix"></div>
                    <b>cache_prefix</b>
                    <a class="ansibleOptionLink" href="#parameter-cache_prefix" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"ansible_inventory_"</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [default]<br>fact_caching_prefix = ansible_inventory_
                                                                                                                    </p>
                                                                    <p>
                                        [inventory]<br>cache_prefix = ansible_inventory_
                                                                                                                    </p>
                                                            </div>
                                                                            <div>
                                env:ANSIBLE_CACHE_PLUGIN_PREFIX
                                                                                            </div>
                                                    <div>
                                env:ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX
                                                                                            </div>
                                                                    </td>
                                                <td>
                                            <div>Prefix to use for cache plugin files/tables</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-cache_timeout"></div>
                    <b>cache_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-cache_timeout" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">3600</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [defaults]<br>fact_caching_timeout = 3600
                                                                                                                    </p>
                                                                    <p>
                                        [inventory]<br>cache_timeout = 3600
                                                                                                                    </p>
                                                            </div>
                                                                            <div>
                                env:ANSIBLE_CACHE_PLUGIN_TIMEOUT
                                                                                            </div>
                                                    <div>
                                env:ANSIBLE_INVENTORY_CACHE_TIMEOUT
                                                                                            </div>
                                                                    </td>
                                                <td>
                                            <div>Cache duration in seconds</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-cert"></div>
                    <b>cert</b>
                    <a class="ansibleOptionLink" href="#parameter-cert" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">"no"</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>Certificate path</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-compose"></div>
                    <b>compose</b>
                    <a class="ansibleOptionLink" href="#parameter-compose" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{}</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>List of custom ansible host vars to create from the device object fetched from NetBox</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-config_context"></div>
                    <b>config_context</b>
                    <a class="ansibleOptionLink" href="#parameter-config_context" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>If True, it adds config_context in host vars.</div>
                                            <div>Config-context enables the association of arbitrary data to devices and virtual machines grouped by region, site, role, platform, and/or tenant. Please check official netbox docs for more info.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-device_query_filters"></div>
                    <b>device_query_filters</b>
                    <a class="ansibleOptionLink" href="#parameter-device_query_filters" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">[]</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>List of parameters passed to the query string for devices (Multiple values may be separated by commas)</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-dns_name"></div>
                    <b>dns_name</b>
                    <a class="ansibleOptionLink" href="#parameter-dns_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>Force IP Addresses to be fetched so that the dns_name for the primary_ip of each device or VM is set as a host_var.</div>
                                            <div>Setting interfaces will also fetch IP addresses and the dns_name host_var will be set.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-fetch_all"></div>
                    <b>fetch_all</b>
                    <a class="ansibleOptionLink" href="#parameter-fetch_all" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                          <div style="font-style: italic; font-size: small; color: darkgreen">
                        added in 0.2.1 of netbox.netbox
                      </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>By default, fetching interfaces and services will get all of the contents of NetBox regardless of query_filters applied to devices and VMs.</div>
                                            <div>When set to False, separate requests will be made fetching interfaces, services, and IP addresses for each device_id and virtual_machine_id.</div>
                                            <div>If you are using the various query_filters options to reduce the number of devices, you may find querying Netbox faster with fetch_all set to False.</div>
                                            <div>For efficiency, when False, these requests will be batched, for example /api/dcim/interfaces?limit=0&amp;device_id=1&amp;device_id=2&amp;device_id=3</div>
                                            <div>These GET request URIs can become quite large for a large number of devices. If you run into HTTP 414 errors, you can adjust the max_uri_length option to suit your web server.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-flatten_config_context"></div>
                    <b>flatten_config_context</b>
                    <a class="ansibleOptionLink" href="#parameter-flatten_config_context" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                          <div style="font-style: italic; font-size: small; color: darkgreen">
                        added in 0.2.1 of netbox.netbox
                      </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>If <em>config_context</em> is enabled, by default it&#x27;s added as a host var named config_context.</div>
                                            <div>If flatten_config_context is set to True, the config context variables will be added directly to the host instead.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-flatten_custom_fields"></div>
                    <b>flatten_custom_fields</b>
                    <a class="ansibleOptionLink" href="#parameter-flatten_custom_fields" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                          <div style="font-style: italic; font-size: small; color: darkgreen">
                        added in 0.2.1 of netbox.netbox
                      </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>By default, host custom fields are added as a dictionary host var named custom_fields.</div>
                                            <div>If flatten_custom_fields is set to True, the fields will be added directly to the host instead.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-flatten_local_context_data"></div>
                    <b>flatten_local_context_data</b>
                    <a class="ansibleOptionLink" href="#parameter-flatten_local_context_data" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                          <div style="font-style: italic; font-size: small; color: darkgreen">
                        added in 0.3.0 of netbox.netbox
                      </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>If <em>local_context_data</em> is enabled, by default it&#x27;s added as a host var named local_context_data.</div>
                                            <div>If flatten_local_context_data is set to True, the config context variables will be added directly to the host instead.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-follow_redirects"></div>
                    <b>follow_redirects</b>
                    <a class="ansibleOptionLink" href="#parameter-follow_redirects" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>urllib2</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>all</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                                                                                                                                <li>safe</li>
                                                                                                                                                                                                <li>none</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>Determine how redirects are followed.</div>
                                            <div>By default, <em>follow_redirects</em> is set to uses urllib2 default behavior.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-group_by"></div>
                    <b>group_by</b>
                    <a class="ansibleOptionLink" href="#parameter-group_by" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>sites</li>
                                                                                                                                                                                                <li>site</li>
                                                                                                                                                                                                <li>location</li>
                                                                                                                                                                                                <li>tenants</li>
                                                                                                                                                                                                <li>tenant</li>
                                                                                                                                                                                                <li>racks</li>
                                                                                                                                                                                                <li>rack</li>
                                                                                                                                                                                                <li>rack_group</li>
                                                                                                                                                                                                <li>rack_role</li>
                                                                                                                                                                                                <li>tags</li>
                                                                                                                                                                                                <li>tag</li>
                                                                                                                                                                                                <li>device_roles</li>
                                                                                                                                                                                                <li>role</li>
                                                                                                                                                                                                <li>device_types</li>
                                                                                                                                                                                                <li>device_type</li>
                                                                                                                                                                                                <li>manufacturers</li>
                                                                                                                                                                                                <li>manufacturer</li>
                                                                                                                                                                                                <li>platforms</li>
                                                                                                                                                                                                <li>platform</li>
                                                                                                                                                                                                <li>region</li>
                                                                                                                                                                                                <li>cluster</li>
                                                                                                                                                                                                <li>cluster_type</li>
                                                                                                                                                                                                <li>cluster_group</li>
                                                                                                                                                                                                <li>is_virtual</li>
                                                                                                                                                                                                <li>services</li>
                                                                                                                                                                                                <li>status</li>
                                                                                    </ul>
                                                                                    <b>Default:</b><br/><div style="color: blue">[]</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>Keys used to create groups. The <em>plurals</em> option controls which of these are valid.</div>
                                            <div><em>rack_group</em> is supported on NetBox versions 2.10 or lower only</div>
                                            <div><em>location</em> is supported on NetBox versions 2.11 or higher only</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-group_names_raw"></div>
                    <b>group_names_raw</b>
                    <a class="ansibleOptionLink" href="#parameter-group_names_raw" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                          <div style="font-style: italic; font-size: small; color: darkgreen">
                        added in 0.2.0 of netbox.netbox
                      </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>Will not add the group_by choice name to the group names</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-groups"></div>
                    <b>groups</b>
                    <a class="ansibleOptionLink" href="#parameter-groups" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{}</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>Add hosts to group based on Jinja2 conditionals.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-interfaces"></div>
                    <b>interfaces</b>
                    <a class="ansibleOptionLink" href="#parameter-interfaces" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                          <div style="font-style: italic; font-size: small; color: darkgreen">
                        added in 0.1.7 of netbox.netbox
                      </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>If True, it adds the device or virtual machine interface information in host vars.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">"no"</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>Certificate key path</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-keyed_groups"></div>
                    <b>keyed_groups</b>
                    <a class="ansibleOptionLink" href="#parameter-keyed_groups" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">[]</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>Add hosts to group based on the values of a variable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-leading_separator"></div>
                    <b>leading_separator</b>
                    <a class="ansibleOptionLink" href="#parameter-leading_separator" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                          <div style="font-style: italic; font-size: small; color: darkgreen">
                        added in 2.11 of ansible.builtin
                      </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>Use in conjunction with keyed_groups.</div>
                                            <div>By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.</div>
                                            <div>This is because the default prefix is &quot;&quot; and the default separator is &quot;_&quot;.</div>
                                            <div>Set this option to False to omit the leading underscore (or other separator) if no prefix is given.</div>
                                            <div>If the group name is derived from a mapping the separator is still used to concatenate the items.</div>
                                            <div>To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-max_uri_length"></div>
                    <b>max_uri_length</b>
                    <a class="ansibleOptionLink" href="#parameter-max_uri_length" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                          <div style="font-style: italic; font-size: small; color: darkgreen">
                        added in 0.2.1 of netbox.netbox
                      </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">4000</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>When fetch_all is False, GET requests to NetBox may become quite long and return a HTTP 414 (URI Too Long).</div>
                                            <div>You can adjust this option to be smaller to avoid 414 errors, or larger for a reduced number of requests.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-plugin"></div>
                    <b>plugin</b>
                    <a class="ansibleOptionLink" href="#parameter-plugin" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>netbox.netbox.nb_inventory</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>token that ensures this is a source file for the &#x27;netbox&#x27; plugin.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-plurals"></div>
                    <b>plurals</b>
                    <a class="ansibleOptionLink" href="#parameter-plurals" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                          <div style="font-style: italic; font-size: small; color: darkgreen">
                        added in 0.2.1 of netbox.netbox
                      </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>If True, all host vars are contained inside single-element arrays for legacy compatibility with old versions of this plugin.</div>
                                            <div>Group names will be plural (ie. &quot;sites_mysite&quot; instead of &quot;site_mysite&quot;)</div>
                                            <div>The choices of <em>group_by</em> will be changed by this option.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-query_filters"></div>
                    <b>query_filters</b>
                    <a class="ansibleOptionLink" href="#parameter-query_filters" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">[]</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>List of parameters passed to the query string for both devices and VMs (Multiple values may be separated by commas)</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-services"></div>
                    <b>services</b>
                    <a class="ansibleOptionLink" href="#parameter-services" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                          <div style="font-style: italic; font-size: small; color: darkgreen">
                        added in 0.2.0 of netbox.netbox
                      </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>If True, it adds the device or virtual machine services information in host vars.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-strict"></div>
                    <b>strict</b>
                    <a class="ansibleOptionLink" href="#parameter-strict" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>If <code>yes</code> make invalid entries a fatal error, otherwise skip and continue.</div>
                                            <div>Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-timeout"></div>
                    <b>timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-timeout" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">60</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>Timeout for Netbox requests in seconds</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-token"></div>
                    <b>token</b>
                    <a class="ansibleOptionLink" href="#parameter-token" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                            <div>
                                env:NETBOX_TOKEN
                                                                                            </div>
                                                    <div>
                                env:NETBOX_API_KEY
                                                                                            </div>
                                                                    </td>
                                                <td>
                                            <div>NetBox API token to be able to read against NetBox.</div>
                                            <div>This may not be required depending on the NetBox setup.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-use_extra_vars"></div>
                    <b>use_extra_vars</b>
                    <a class="ansibleOptionLink" href="#parameter-use_extra_vars" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                          <div style="font-style: italic; font-size: small; color: darkgreen">
                        added in 2.11 of ansible.builtin
                      </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [inventory_plugins]<br>use_extra_vars = no
                                                                                                                    </p>
                                                            </div>
                                                                            <div>
                                env:ANSIBLE_INVENTORY_USE_EXTRA_VARS
                                                                                            </div>
                                                                    </td>
                                                <td>
                                            <div>Merge extra vars into the available variables for composition (highest precedence).</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
                    <b>validate_certs</b>
                    <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>Allows connection when SSL certificates are not valid. Set to <code>false</code> when certificates are not trusted.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-virtual_chassis_name"></div>
                    <b>virtual_chassis_name</b>
                    <a class="ansibleOptionLink" href="#parameter-virtual_chassis_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>When a device is part of a virtual chassis, use the virtual chassis name as the Ansible inventory hostname.</div>
                                            <div>The host var values will be from the virtual chassis master.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-vm_query_filters"></div>
                    <b>vm_query_filters</b>
                    <a class="ansibleOptionLink" href="#parameter-vm_query_filters" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">[]</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>List of parameters passed to the query string for VMs (Multiple values may be separated by commas)</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

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
    validate_certs: True
    config_context: False
    group_by:
      - device_roles
    query_filters:
      - role: network-edge-router
    device_query_filters:
      - has_primary_ip: 'true'

    # has_primary_ip is a useful way to filter out patch panels and other passive devices

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



.. Parsing errors


.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.netbox.netbox.netbox_power_outlet_template_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

netbox.netbox.netbox_power_outlet_template -- Create, update or delete power outlet templates within Netbox
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `netbox.netbox collection <https://galaxy.ansible.com/netbox/netbox>`_ (version 3.3.0).

    To install it use: :code:`ansible-galaxy collection install netbox.netbox`.

    To use it in a playbook, specify: :code:`netbox.netbox.netbox_power_outlet_template`.

.. version_added

.. versionadded:: 0.2.3 of netbox.netbox

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Creates, updates or removes power outlet templates from Netbox


.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- pynetbox


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-cert"></div>
                    <b>cert</b>
                    <a class="ansibleOptionLink" href="#parameter-cert" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Certificate path</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-data"></div>
                    <b>data</b>
                    <a class="ansibleOptionLink" href="#parameter-data" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Defines the power outlet configuration</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/device_type"></div>
                    <b>device_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data/device_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The device type the power outlet is attached to</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/feed_leg"></div>
                    <b>feed_leg</b>
                    <a class="ansibleOptionLink" href="#parameter-data/feed_leg" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>A</li>
                                                                                                                                                                                                <li>B</li>
                                                                                                                                                                                                <li>C</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The phase, in case of three-phase feed</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the power outlet</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/power_port_template"></div>
                    <b>power_port_template</b>
                    <a class="ansibleOptionLink" href="#parameter-data/power_port_template" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The attached power port template</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-data/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>iec-60320-c5</li>
                                                                                                                                                                                                <li>iec-60320-c7</li>
                                                                                                                                                                                                <li>iec-60320-c13</li>
                                                                                                                                                                                                <li>iec-60320-c15</li>
                                                                                                                                                                                                <li>iec-60320-c19</li>
                                                                                                                                                                                                <li>iec-60309-p-n-e-4h</li>
                                                                                                                                                                                                <li>iec-60309-p-n-e-6h</li>
                                                                                                                                                                                                <li>iec-60309-p-n-e-9h</li>
                                                                                                                                                                                                <li>iec-60309-2p-e-4h</li>
                                                                                                                                                                                                <li>iec-60309-2p-e-6h</li>
                                                                                                                                                                                                <li>iec-60309-2p-e-9h</li>
                                                                                                                                                                                                <li>iec-60309-3p-e-4h</li>
                                                                                                                                                                                                <li>iec-60309-3p-e-6h</li>
                                                                                                                                                                                                <li>iec-60309-3p-e-9h</li>
                                                                                                                                                                                                <li>iec-60309-3p-n-e-4h</li>
                                                                                                                                                                                                <li>iec-60309-3p-n-e-6h</li>
                                                                                                                                                                                                <li>iec-60309-3p-n-e-9h</li>
                                                                                                                                                                                                <li>nema-5-15r</li>
                                                                                                                                                                                                <li>nema-5-20r</li>
                                                                                                                                                                                                <li>nema-5-30r</li>
                                                                                                                                                                                                <li>nema-5-50r</li>
                                                                                                                                                                                                <li>nema-6-15r</li>
                                                                                                                                                                                                <li>nema-6-20r</li>
                                                                                                                                                                                                <li>nema-6-30r</li>
                                                                                                                                                                                                <li>nema-6-50r</li>
                                                                                                                                                                                                <li>nema-l5-15r</li>
                                                                                                                                                                                                <li>nema-l5-20r</li>
                                                                                                                                                                                                <li>nema-l5-30r</li>
                                                                                                                                                                                                <li>nema-l5-50r</li>
                                                                                                                                                                                                <li>nema-l6-20r</li>
                                                                                                                                                                                                <li>nema-l6-30r</li>
                                                                                                                                                                                                <li>nema-l6-50r</li>
                                                                                                                                                                                                <li>nema-l14-20r</li>
                                                                                                                                                                                                <li>nema-l14-30r</li>
                                                                                                                                                                                                <li>nema-l21-20r</li>
                                                                                                                                                                                                <li>nema-l21-30r</li>
                                                                                                                                                                                                <li>CS6360C</li>
                                                                                                                                                                                                <li>CS6364C</li>
                                                                                                                                                                                                <li>CS8164C</li>
                                                                                                                                                                                                <li>CS8264C</li>
                                                                                                                                                                                                <li>CS8364C</li>
                                                                                                                                                                                                <li>CS8464C</li>
                                                                                                                                                                                                <li>ita-e</li>
                                                                                                                                                                                                <li>ita-f</li>
                                                                                                                                                                                                <li>ita-g</li>
                                                                                                                                                                                                <li>ita-h</li>
                                                                                                                                                                                                <li>ita-i</li>
                                                                                                                                                                                                <li>ita-j</li>
                                                                                                                                                                                                <li>ita-k</li>
                                                                                                                                                                                                <li>ita-l</li>
                                                                                                                                                                                                <li>ita-m</li>
                                                                                                                                                                                                <li>ita-n</li>
                                                                                                                                                                                                <li>ita-o</li>
                                                                                                                                                                                                <li>hdot-cx</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of the power outlet</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-netbox_token"></div>
                    <b>netbox_token</b>
                    <a class="ansibleOptionLink" href="#parameter-netbox_token" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The token created within Netbox to authorize API access</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-netbox_url"></div>
                    <b>netbox_url</b>
                    <a class="ansibleOptionLink" href="#parameter-netbox_url" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>URL of the Netbox instance resolvable by Ansible control host</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-query_params"></div>
                    <b>query_params</b>
                    <a class="ansibleOptionLink" href="#parameter-query_params" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>This can be used to override the specified values in ALLOWED_QUERY_PARAMS that is defined</div>
                                            <div>in plugins/module_utils/netbox_utils.py and provides control to users on what may make</div>
                                            <div>an object unique in their environment.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>absent</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Use <code>present</code> or <code>absent</code> for adding or removing.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
                    <b>validate_certs</b>
                    <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">"yes"</div>
                                    </td>
                                                                <td>
                                            <div>If <code>no</code>, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes

Notes
-----

.. note::
   - Tags should be defined as a YAML list
   - This should be ran with connection ``local`` and hosts ``localhost``

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: "Test Netbox modules"
      connection: local
      hosts: localhost
      gather_facts: False

      tasks:
        - name: Create power outlet template within Netbox with only required information
          netbox_power_outlet_template:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              name: Test Power Outlet Template
              device_type: Test Device Type
            state: present

        - name: Update power outlet template with other fields
          netbox_power_outlet_template:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              name: Test Power Outlet Template
              device_type: Test Device Type
              type: iec-60320-c6
              power_port_template: Test Power Port Template
              feed_leg: A
            state: present

        - name: Delete power outlet template within netbox
          netbox_power_outlet_template:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              name: Test Power Outlet Template
              device_type: Test Device Type
            state: absent




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-msg"></div>
                    <b>msg</b>
                    <a class="ansibleOptionLink" href="#return-msg" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Message indicating failure or info about what has been achieved</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-power_outlet_template"></div>
                    <b>power_outlet_template</b>
                    <a class="ansibleOptionLink" href="#return-power_outlet_template" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>success (when <em>state=present</em>)</td>
                <td>
                                            <div>Serialized object as created or already existent within Netbox</div>
                                        <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>

..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Tobias Groß (@toerb)



.. Parsing errors


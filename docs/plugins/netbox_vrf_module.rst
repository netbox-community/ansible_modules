.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.netbox.netbox.netbox_vrf_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

netbox.netbox.netbox_vrf -- Create, update or delete vrfs within Netbox
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `netbox.netbox collection <https://galaxy.ansible.com/netbox/netbox>`_ (version 2.0.0).

    To install it use: :code:`ansible-galaxy collection install netbox.netbox`.

    To use it in a playbook, specify: :code:`netbox.netbox.netbox_vrf`.

.. version_added

.. versionadded:: 0.1.0 of netbox.netbox

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Creates, updates or removes vrfs from Netbox


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
                                            <div>Defines the vrf configuration</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/custom_fields"></div>
                    <b>custom_fields</b>
                    <a class="ansibleOptionLink" href="#parameter-data/custom_fields" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>must exist in Netbox</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-data/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The description of the vrf</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/enforce_unique"></div>
                    <b>enforce_unique</b>
                    <a class="ansibleOptionLink" href="#parameter-data/enforce_unique" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Prevent duplicate prefixes/IP addresses within this VRF</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/export_targets"></div>
                    <b>export_targets</b>
                    <a class="ansibleOptionLink" href="#parameter-data/export_targets" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                          <div style="font-style: italic; font-size: small; color: darkgreen">
                        added in 2.0.0 of netbox.netbox
                      </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Export targets tied to VRF</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/import_targets"></div>
                    <b>import_targets</b>
                    <a class="ansibleOptionLink" href="#parameter-data/import_targets" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                          <div style="font-style: italic; font-size: small; color: darkgreen">
                        added in 2.0.0 of netbox.netbox
                      </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Import targets tied to VRF</div>
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
                                            <div>The name of the vrf</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/rd"></div>
                    <b>rd</b>
                    <a class="ansibleOptionLink" href="#parameter-data/rd" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The RD of the VRF. Must be quoted to pass as a string.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/tags"></div>
                    <b>tags</b>
                    <a class="ansibleOptionLink" href="#parameter-data/tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Any tags that the vrf may need to be associated with</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/tenant"></div>
                    <b>tenant</b>
                    <a class="ansibleOptionLink" href="#parameter-data/tenant" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The tenant that the vrf will be assigned to</div>
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
        - name: Create vrf within Netbox with only required information
          netbox_vrf:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              name: Test VRF
            state: present

        - name: Delete vrf within netbox
          netbox_vrf:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              name: Test VRF
            state: absent

        - name: Create vrf with all information
          netbox_vrf:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              name: Test VRF
              rd: "65000:1"
              tenant: Test Tenant
              enforce_unique: true
              import_targets:
                - "65000:65001"
              export_targets:
                - "65000:65001"
              description: VRF description
              tags:
                - Schnozzberry
            state: present




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
                    <div class="ansibleOptionAnchor" id="return-vrf"></div>
                    <b>vrf</b>
                    <a class="ansibleOptionLink" href="#return-vrf" title="Permalink to this return value"></a>
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

- Mikhail Yohman (@FragmentedPacket)



.. Parsing errors

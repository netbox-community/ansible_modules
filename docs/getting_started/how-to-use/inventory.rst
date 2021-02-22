============
Inventory
============

This page will just have quick examples that people may have had questions about, but the normal plugin documentation should be referenced for normal usage.

The inventory plugin documentation can be found :ref:`here<ansible_collections.netbox.netbox.nb_inventory_inventory>`.

Using Compose to Set ansible_network_os to Platform Slug
------------------------------------------------------------------

.. code-block:: yaml

  ---
  plugin: netbox.netbox.nb_inventory
  compose:
    ansible_network_os: platform.slug


Using Keyed Groups to set ansible_network_os to Platform Slug
----------------------------------------------------------------

.. code-block:: yaml

  ---
  plugin: netbox.netbox.nb_inventory
  keyed_groups:
    - key: platform
      prefix: "network_os"
      separator: "_"

.. _post: http://blog.networktocode.com/post/ansible-constructed-inventory/
.. note:: The above examples are excerpts from the following blog post_.


Using Inventory Plugin Within AWX/Tower
----------------------------------------

This will cover the basic usage of the NetBox inventory plugin within this collection.

1. Define ``collections/requirements.yml`` within a Git project.
2. AWX/Tower will download the collection on each run. This can be handled differently or excluded if storing Ansible Collections on the AWX/Tower box.
3. Define ``inventory.yml`` in Git project that adheres to inventory plugin structure.
4. Add Git project to AWX/Tower as a project.
5. Create inventory and select ``source from project``.
6. Select the AWX/Tower project from Step 2
7. Select the ``inventory.yml`` file in the project from Step 3
8. Make sure your Tower installation uses Python 3 or select the proper ``ANSIBLE ENVIRONMENT``
9. Click ``Save`` and sync source.

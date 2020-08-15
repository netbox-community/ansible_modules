Installation
=============

Ansible Galaxy
---------------

Run the following command to install the netbox.netbox collection:
``ansible-galaxy collection install netbox.netbox``

Follow the official docs_ to learn more about installation.

.. _docs: https://docs.ansible.com/ansible/latest/user_guide/collections_using.html#installing-collections

.. note:: Installing Ansible Collections using Git within a ``requirements.yml`` is not supported until Ansible 2.10.


Build From Source
------------------

Follow these steps to install from source:

1. ``git clone git@github.com:netbox-community/ansible_modules.git``
2. ``cd ansible_modules``
3. ``ansible-galaxy collection build .``
4. ``ansible-galaxy collection install netbox-netbox*.tar.gz``


Using Ansible Collections
-----------------------------------------

There are two methods when using a collection in a playbook:

1. Using the ``collections`` directive at the play level.
2. Using the Fully Qualified Collection Name (FQCN) of the module, e.g. ``netbox.netbox.netbox_device`` at the task level.

.. code-block:: yaml

  ---
  - hosts: "localhost"
    collections:
      - netbox.netbox
    
    tasks:
      - name: "Configure a device in NetBox"
        netbox_device:
        <.. omitted>


.. code-block:: yaml

  ---
  - hosts: "localhost"
  
    tasks:
      - name: "Configure a device in NetBox"
        netbox.netbox.netbox_device:
        <.. omitted>


Ansible recommends option 2 by using the FQCN when using Ansible Collections.

You can find more information at the official Ansible docs_.

.. _docs: https://docs.ansible.com/ansible/latest/user_guide/collections_using.html#installing-collections

.. note:: If you are on MacOS and are running into ``ERROR! A worker was found in a dead state errors``, try running the playbook with ``env no_proxy='*'`` tag in front of the playbook. This is a known issue with MacOS as per this reference: https://github.com/ansible/ansible/issues/32554#issuecomment-642896861

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
8. Click ``Save`` and sync source.

.. toctree::
   :maxdepth: 4
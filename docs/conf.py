# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import re
import stat
from pathlib import Path
from antsibull.cli import antsibull_docs

sys.path.insert(0, os.path.abspath("../"))


# -- Project information -----------------------------------------------------

project = "ansible_modules"
copyright = "2020, Mikhail Yohman"
author = "Mikhail Yohman <@FragmentedPacket>"

# The full version, including alpha/beta/rc tags
release = "2.0.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosectionlabel",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["ansible.css", "pygments.css"]
# html_theme_path = ["_themes"]

# Settings for extensions
autodoc_default_options = {
    "members": True,
    "private-members": True,
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
}
autodoc_mock_imports = ["ansible_collections"]


def create_antsibull_docs(files, plugin_type=None):
    """Creates the necessary docs for all files in a directory

    Args:
        files ([Path.Glob]): Glob of files from a specific directory.
        plugin_type ([str], optional): Create the proper documentation for the plugin type. Defaults to None.
    """
    for f in files:
        file_name = re.search(r"(?:.+\/)(\S+)\.py", str(f)).group(1)
        if file_name in ["netbox_interface"]:
            continue

        print(file_name)
        if plugin_type is not None:
            file_path = Path(f"plugins/{plugin_type}/{file_name}/")
        else:
            file_path = Path(f"plugins/modules/{file_name}/")

        file_path.mkdir(mode=744, exist_ok=True)

        if plugin_type is not None:
            args_string = f"junk plugin --dest-dir {file_path} --plugin-type {plugin_type} netbox.netbox.{file_name}"
        else:
            args_string = f"junk plugin --dest-dir {file_path} --plugin-type module netbox.netbox.{file_name}"
        args = args_string.split(" ")
        try:
            antsibull_docs.run(args)
        except Exception as e:
            sys.exit(1)


def remove_write_permissions(path):
    """Remove write permissions from group and others for the sake of antsibull-docs working.

    Args:
        path (Path): Path object.
    """
    for d in path.iterdir():
        d.chmod(stat.S_IRWXU | stat.S_IRGRP | stat.S_IROTH)


def build_ansible_docs(app):
    """
    This will perform all necessary actions to use antsibull-docs to generate collection docs
    """
    inventory_path = Path("../plugins/inventory/")
    lookup_path = Path("../plugins/lookup/")
    modules_path = Path("../plugins/modules/")

    # Set permissions on folders within docs/plugins to remove w from g+o
    doc_modules = Path("plugins/modules/")
    doc_lookup = Path("plugins/lookup/")
    doc_inventory = Path("plugins/inventory/")
    remove_write_permissions(doc_modules)
    remove_write_permissions(doc_lookup)
    remove_write_permissions(doc_inventory)

    inventory = inventory_path.glob("[!_]*.py")
    lookup = lookup_path.glob("[!_]*.py")
    modules = modules_path.glob("[!_]*.py")

    create_antsibull_docs(inventory, "inventory")
    create_antsibull_docs(lookup, "lookup")
    create_antsibull_docs(modules)


###########################################
# NOT IN USE AND SHOULD BE MANUALLY BUILT
################
# def setup(app):
#    app.connect("builder-inited", build_ansible_docs)


# build_ansible_docs(None)

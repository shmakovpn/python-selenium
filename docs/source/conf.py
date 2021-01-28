"""
docs/source/conf.py
+++++++++++++++++++

Configuration file for the Sphinx documentation builder.

| Author: shmakovpn <shmakovpn@yandex.ru>
| Date: 2021-01-28
"""
import os
import sys

# -- Project information -----------------------------------------------------

project = 'python_selenium'
copyright = '2021, shmakovpn@yandex.ru'
author = 'shmakovpn@yandex.ru'

SCRIPT_DIR: str = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR: str = os.path.dirname(SCRIPT_DIR)
PROJECT_DIR: str = os.path.dirname(DOCS_DIR)
PACKAGE_DIR: str = os.path.join(PROJECT_DIR, project)

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, PROJECT_DIR)  # needed to automodule

# -- imports --
from python_selenium.version import VERSION

# -- General configuration ---------------------------------------------------

# mocking C modules
# autodock_mock_imports: List[str] = []

# The short X.Y version
version: str = VERSION
# The full version, including alpha/beta/rc tags
release: str = VERSION

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
]

master_doc = 'contents'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

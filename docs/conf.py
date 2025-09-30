# Configuration file for the Sphinx documentation builder.

import importlib.metadata
import os
import sys

# -- Path setup --------------------------------------------------------------
# Add project root to sys.path so autodoc can find modules
sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------
project = "Invoco"
copyright = "2025, Christopher Bailey"
author = "Christopher Bailey"

# Get version from installed package, fallback if not installed
try:
    release = importlib.metadata.version("invoco")
except importlib.metadata.PackageNotFoundError:
    release = "0.0.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",  # Pull docstrings from code
    "sphinx.ext.napoleon",  # Support for Google/Numpy docstring styles
    "sphinx.ext.viewcode",  # Add links to source code
    "sphinx.ext.autosummary",  # Create summary tables
    "myst_parser",  # Parse Markdown files (CHANGELOG.md, etc.)
]

autosummary_generate = True  # Automatically build autosummary docs

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]

# -- MyST (Markdown) configuration -------------------------------------------
myst_enable_extensions = [
    "colon_fence",  # ::: fenced blocks
    "deflist",  # definition lists
    "linkify",  # auto-detect links
]

# -- Autodoc configuration ---------------------------------------------------
autoclass_content = "both"  # Include class docstring + __init__
autodoc_typehints = "description"
autodoc_member_order = "bysource"

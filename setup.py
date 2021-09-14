#!/usr/bin/env python
# setup
# Setup script for installing yellowbrick
#
# Author:   Banjo Obayomi
# Created:  Mon Sep 13 19:57:28 EDT 2021
#

"""
Setup script for installing fancylit.
"""

##########################################################################
## Imports
##########################################################################

import os
import codecs

from setuptools import setup
from setuptools import find_packages

##########################################################################
## Package Information
##########################################################################

## Basic information
## Basic information
NAME = "fancylit"
DESCRIPTION = "Contains pre-packaged Streamlit code to render fancy visualizations, run modeling tasks, and data exploration"
AUTHOR = "Hacktoberfest"
EMAIL = "hacktoberfest@gmail.com"
MAINTAINER = "The community"
LICENSE = "Apache 2"
REPOSITORY = "https://github.com/banjtheman/fancylit"
PACKAGE = "fancylit"
URL = "https://github.com/banjtheman/fancylit"

## Define the keywords
KEYWORDS = (
    "visualization",
    "machine learning",
    "streamlit",
    "data science",
)

## Define the classifiers
## See https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = (
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Scientific/Engineering :: Visualization",
)

## Important Paths
PROJECT = os.path.abspath(os.path.dirname(__file__))
REQUIRE_PATH = "requirements.txt"
PKG_DESCRIBE = "README.md"

## Directories to ignore in find_packages
EXCLUDES = (
    "tests",
    "tests.*",
    "bin",
    "docs",
    "docs.*",
    "fixtures",
    "register",
    "notebooks",
    "notebooks.*",
    "examples",
    "examples.*",
    "binder",
    "binder.*",
    "paper",
)

##########################################################################
## Helper Functions
##########################################################################


def read(*parts):
    """
    Assume UTF-8 encoding and return the contents of the file located at the
    absolute path from the REPOSITORY joined with *parts.
    """
    with codecs.open(os.path.join(PROJECT, *parts), "rb", "utf-8") as f:
        return f.read()


def get_version(python_version_file="./VERSION"):
    """
    Purpose:
        Get python version from a specified requirements file.
    Args:
        python_version_file (String): Path to the version file (usually
            it is VERSION in the same directory as the setup.py)
    Return:
        requirements (List of Strings): The python requirements necessary to run
            the library
    """

    version = "development"
    if os.path.isfile(python_version_file):
        with open(python_version_file) as version_file:
            version = version_file.readline().strip().strip("\n")

    return version


def get_requires(path=REQUIRE_PATH):
    """
    Yields a generator of requirements as defined by the REQUIRE_PATH which
    should point to a requirements.txt output by `pip freeze`.
    """
    for line in read(path).splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            yield line


def get_description_type(path=PKG_DESCRIBE):
    """
    Returns the long_description_content_type based on the extension of the
    package describe path (e.g. .txt, .rst, or .md).
    """
    _, ext = os.path.splitext(path)
    return {".rst": "text/x-rst", ".txt": "text/plain", ".md": "text/markdown"}[ext]


##########################################################################
## Define the configuration
##########################################################################

config = {
    "name": NAME,
    "version": get_version(),
    "description": DESCRIPTION,
    "long_description": read(PKG_DESCRIBE),
    "long_description_content_type": get_description_type(PKG_DESCRIBE),
    "classifiers": CLASSIFIERS,
    "keywords": KEYWORDS,
    "license": LICENSE,
    "author": AUTHOR,
    "author_email": EMAIL,
    "url": URL,
    "maintainer": MAINTAINER,
    "maintainer_email": EMAIL,
    "project_urls": {},
    "packages": find_packages(where=PROJECT, exclude=EXCLUDES),
    "zip_safe": False,
    "install_requires": list(get_requires()),
    "python_requires": ">=3.4, <4",
}


##########################################################################
## Run setup script
##########################################################################

if __name__ == "__main__":
    setup(**config)

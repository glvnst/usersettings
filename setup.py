#!/usr/bin/python
""" Setup the setup """
from setuptools import setup

LONG_DESCRIPTION = """
usersettings
------------
"usersettings" is a python module for easily managing persistent settings
using an editable format and stored in an OS-appropriate location
(windows/os x/linux are supported).

For more information, please refer to README.md or the `usersettings github
page <https://github.com/glvnst/usersettings>`_.
"""

setup(
    name = "usersettings",
    version = "1.0.7",
    author = "Ben Burke",
    author_email = "benburke42@gmail.com",
    url = "https://github.com/glvnst/usersettings",
    description = "Portable Local Settings Storage",
    long_description = LONG_DESCRIPTION,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    platforms = ["any"],
    license = "https://raw.github.com/glvnst/usersettings/master/LICENSE.txt",

    py_modules=['usersettings'],
    package_data = {'': ['*.md', 'docs/*.txt', 'examples/*.py']},
    install_requires = ['appdirs>=1.2'],
)

#!/usr/bin/python
""" Setup the setup """
from setuptools import setup

setup(
    name = "UserSettings",
    version = "1.0",
    description = "Portable Local Settings Storage",
    url = "https://github.com/glvnst/UserSettings",
    author = "Ben Burke",
    author_email = "benburke42@gmail.com",
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    py_modules=['usersettings'],
    install_requires = ['appdirs>=1.2'],
)
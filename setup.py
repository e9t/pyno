#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pyno",
    version = "0.0.1",
    author = "Lucy Park",
    author_email = "me@lucypark.kr",
    description = ("Python notifications for Mac OS"),
    license = "Apache v2.0",
    keywords = "python macos notification",
    url = "http://github.com/e9t/pyno",
    packages=['pyno'],
    long_description=read('README.md'),
    install_requires = ['pync>=1.6.0'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
)

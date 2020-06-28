#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from os import path
from setuptools import find_packages
from setuptools import setup

from lsif_indexer.consts import INDEXER_VERSION


def read(name):
    with open(path.join(path.dirname(__file__), name), encoding="utf8") as f:
        return f.read()


setup(
    name="lsif-py",
    version=INDEXER_VERSION,
    license="MIT",
    description="Python LSIF Indexer",
    long_description=read("README.md"),
    author="Eric Fritz",
    author_email="eric@eric-fritz.com",
    url="https://github.com/sourcegraph/lsif-py",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
    project_urls={
        "Documentation": "https://github.com/sourcegraph/lsif-py",
        "Issue Tracker": "https://github.com/sourcegraph/lsif-py/issues",
    },
    keywords=["lsif", "lsif-py", "keyword3"],
    python_requires="!=2.*, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=["jedi==0.16.0",],
    entry_points={"console_scripts": ["lsif-py = lsif_indexer.cli:main",]},
)

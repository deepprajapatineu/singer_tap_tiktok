#!/usr/bin/env python
from setuptools import setup

setup(
    name="singer_tap_tiktok",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["singer_tap_tiktok"],
    install_requires=[
        # NB: Pin these to a more specific version for tap reliability
        "singer-python",
        "requests",
    ],
    entry_points="""
    [console_scripts]
    singer_tap_tiktok=singer_tap_tiktok:main
    """,
    packages=["singer_tap_tiktok"],
    package_data = {
        "schemas": ["singer_tap_tiktok/schemas/*.json"]
    },
    include_package_data=True,
)

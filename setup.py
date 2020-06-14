# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="pyEddyTrackerSample",
    version="0.0.0",
    description="Py-Eddy-Tracker samples",
    keywords="eddy samples",
    author="Antoine Delepoulle",
    author_email="delepoulle.a@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    package_data={
        "py_eddy_tracker_sample": [
            "*/*.zarr/*/*",
            "*/*.zarr/.*",
            "*/*.zarr/*/.*",
        ],
    },
)


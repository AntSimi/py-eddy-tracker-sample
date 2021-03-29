# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

import versioneer

setup(
    name="pyEddyTrackerSample",
    description="Py-Eddy-Tracker samples",
    keywords="eddy samples",
    author="Antoine Delepoulle",
    author_email="delepoulle.a@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    package_data={
        "py_eddy_tracker_sample": [
            "*/*.zarr/*/*",
            "*/*.zarr/.*",
            "*/*.zarr/*/.*",
        ],
    },
)

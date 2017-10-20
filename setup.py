#! /usr/bin/env python

from setuptools import setup
from setuptools import find_packages

setup(
    name='obs_generator',
    version = '1.0',
    description='Combine seed image and dark ramp into simulated ramp'
    long_description=('A tool to combine a noiseless seed image with a '
                      'dark current ramp in order to produce a simulated'
                      ' NIRCam integration/exposure with realistic '
                      'detector artifacts.')
    author='Bryan Hilbert',
    author_email='hilbert@stsci.edu',
    keywords = ['astronomy'],
    classifiers = ['Programming Language :: Python'],
    packages = find_packages(exclude=["examples"]),
    install_requires = [],
    include_package_data = True
    )

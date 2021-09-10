from __future__ import print_function
import argparse
import os
import sys
import numpy
from setuptools import find_packages, setup, Extension
from setuptools.command.test import test as test_command


class PyTest(test_command):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        test_command.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name="mtpar",
    version="0.2.0",
    license='BSD2',
    description="moment tensor parameterization utilities",
    author="Ryan Modrak",
    author_email="rmodrak@uaf.edu",
    url="https://github.com/uafseismo/mtuq",
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        # complete classifier list:
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    keywords=[
        "seismology"
    ],
    python_requires='~=3.5',
    install_requires=[
        "numpy", "scipy", "obspy", "pytest", "six"
    ],
)


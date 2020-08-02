#!/usr/bin/env python3
# pylint: disable=missing-docstring
# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev
import io
import os
import sys

from pathlib import Path
from shutil import rmtree

from setuptools import Command, find_packages, setup

from typing import *

# !----------------------------------------- Package meta-data.

# Create 'Pypi-safe' project name by replaceing ['-',' '] with '_'
# NAME = NAME.lower().replace('-', '_').replace(' ', '_')

# GITHUB_USER: get_from_shell('git config user.name')
# URL: str = f'https://github.com/skeptycal/{NAME}'

class UploadCommand(Command):
    """Support setup.py upload."""

    description: str = 'Build and publish the package.'
    user_options: List[str] = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system(
            f'{sys.executable} setup.py sdist bdist_wheel --universal',
        )

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()


setup()

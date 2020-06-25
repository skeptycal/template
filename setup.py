#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" setup_utils Setup
    ---
    Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

from os import linesep as NL
from pathlib import Path
from sys import path as PYTHONPATH

from setuptools import find_packages, setup

from typing import Dict, Final, List, Optional, Sequence, Tuple

try:
    DEFAULT_ENCODING  #
except:
    from locale import getpreferredencoding
    DEFAULT_ENCODING: str = getpreferredencoding(do_setlocale=True) or "utf-8"

# put a name here to ignore the default ...
module_name: str = ""

# the default version number is '0.0.1'
__version__: str = '0.0.1'

# the default package name is the name of the parent folder ...
if not module_name:
    module_name = Path(__file__).resolve().parent.name

here = Path(__file__).resolve().parent
if here not in PYTHONPATH:
    PYTHONPATH.insert(0, here)


def table_print(data: (Dict, Sequence), **kwargs):
    tmp: List = []
    if isinstance(data, dict):
        tmp.extend(
            [f"{str(k):<15.15} :  {repr(v):<45.45}" for k, v in data.items()])
    elif isinstance(data, (list, tuple, set)):
        for x in data:
            try:
                tmp.append(f"{str(x):<15.15} :  {repr(f'{x}'):<45.45}")
            except:
                tmp.append(f"{str(x)}")
    else:
        raise TypeError('Parameter must be an iterable Mapping or Sequence.')
    print(NL.join(tmp), **kwargs)


def pip_safe_name(s: str):
    """ Return a name that is converted to pypi safe format. """
    return s.lower().replace("-", "_").replace(" ", "_")


def get_file_contents(file_name: str = "readme.md", search_list: List[str] = ["readme.md", "readme.rst", "readme", "readme.txt"]):
    """ Returns the text of the README file

        The default file is `README.md` and is *NOT* case sensitive. (e.g. `README` is the same as `readme`)
        Can load *any* text file, but the default search path is setup for readme files

        ```
        Search path = ["readme.md", "readme.rst", "readme", "readme.txt"]
        ```

        Example:

        ```
        long_description=readme()
        ```
        """

    if file_name not in search_list:
        search_list.insert(0, file_name)
    found: bool = False
    for searchfile in search_list:
        for parent in Path(__file__).resolve().parents:
            find_path = Path(parent / searchfile)
            if find_path.exists():
                found = True
                # print(find_path)
                break
        if found:
            break
    if found:
        try:
            with open(find_path, mode="r", encoding=DEFAULT_ENCODING) as f:
                return f.read()
        except IOError as e:
            raise IOError(f"Cannot read from the project file '{find_path}'")
    else:
        raise FileNotFoundError(
            f"Cannot find project file '{file_name}' in project tree. Search list = {search_list}"
        )


# ? **************************************** package metadata
#<@package_metadata>

# make the name safe for Pypi.org upload
NAME: str = pip_safe_name(module_name)

VERSION: str = __version__
VERSION_INFO: Tuple[int] = VERSION.split(".")
DESCRIPTION: str = "System utilities for Python on macOS."
REQUIRES_PYTHON: str = ">=3.8.0"
# PACKAGE_DIR: Dict = {f'{NAME}'}
PACKAGE_EXCLUDE: List[str] = ['*test*', '*bak*']
LICENSE: str = "MIT"
LONG_DESCRIPTION: str = get_file_contents('README.md')
LONG_DESCRIPTION_CONTENT_TYPE: str = "text/markdown"
# LONG_DESCRIPTION_CONTENT_TYPE="text/x-rst",
AUTHOR: str = "Michael Treanor"
AUTHOR_EMAIL: str = "skeptycal@gmail.com"
MAINTAINER: str = ""
MAINTAINER_EMAIL: str = ""
URL: str = f"https://skeptycal.github.io/{NAME}/"
DOWNLOAD_URL: str = f"https://github.com/skeptycal/{NAME}/archive/{VERSION}.tar.gz"
ZIP_SAFE: bool = False
INCLUDE_PACKAGE_DATA: bool = True
# What packages are required for this module to be executed?
REQUIRED: List[str] = [
    "aiocontextvars>=0.2.0 ; python_version<'3.7'",
    "colorama>=0.3.4 ; sys_platform=='win32'",
    "win32-setctime>=1.0.0 ; sys_platform=='win32'",
]

# What packages are optional?
EXTRAS: Dict = {}

PACKAGE_DATA: Dict = {
    # If any package contains these files, include them:
    "": [
        "*.txt",
        "*.rst",
        "*.md",
        "*.ini",
        "*.png",
        "*.jpg",
        "__init__.pyi",
        "py.typed",
    ]
}

PROJECT_URLS: Dict = {
    "Website": f"https://skeptycal.github.io/{NAME}/",
    "Documentation": f"https://skeptycal.github.io/{NAME}/docs",
    "Source Code": f"https://www.github.com/skeptycal/{NAME}/",
    "Changelog":
    f"https://github.com/skeptycal/{NAME}/blob/master/CHANGELOG.md",
}

KEYWORDS: List = [
    "application",
    "macOS",
    "dev",
    "devops",
    "cache",
    "utilities",
    "cli",
    "python",
    "cython",
    "text",
    "console",
    "log",
    "debug",
    "test",
    "testing",
    "logging",
    "logger",
]
CLASSIFIERS: List = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Environment :: Console",
    "Environment :: MacOS X",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "Operating System :: MacOS",
    "Operating System :: OS Independent",
    "Programming Language :: Cython",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3",
    # These are the Python versions tested; it may work on others
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Software Development :: Testing",
    "Topic :: Utilities",
]


def main():
    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        python_requires=REQUIRES_PYTHON,
        # package_dir=PACKAGE_DIR,
        packages=find_packages(
            f'{NAME}', exclude=PACKAGE_EXCLUDE),
        # py_modules=[f"{NAME}"],
        license=LICENSE,
        long_description=LONG_DESCRIPTION,
        long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        maintainer=MAINTAINER or AUTHOR,
        maintainer_email=MAINTAINER_EMAIL or AUTHOR_EMAIL,
        url=URL,
        download_url=DOWNLOAD_URL,
        zip_safe=ZIP_SAFE,
        include_package_data=INCLUDE_PACKAGE_DATA,
        # setup_requires=["isort"],
        install_requires=REQUIRED,
        extras_require=EXTRAS,
        package_data=PACKAGE_DATA,
        project_urls=PROJECT_URLS,
        keywords=KEYWORDS,
        classifiers=CLASSIFIERS,
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
""" setup_utils Setup

    use `poetry install` instead
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


# # ? ################################### Default Metadata
# NAME: str = 'AutoSys'
# USERNAME: str = 'skeptycal'
# DESCRIPTION: str = 'System utilities for Python on macOS.'
# PYTHON_REQUIRES: str = '>=3.6.0'
# # ? ####################################################

# if True:
#     import os
#     import re
#     import sys

#     from io import TextIOWrapper
#     from os import linesep as NL
#     from pathlib import Path
#     from sys import stderr, path as PYTHONPATH

#     from typing import (
#         Any,
#         AnyStr,
#         Dict,
#         List,
#         Match,
#         Optional,
#         Sequence,
#         Set,
#         Tuple,
#         Union,
#     )

#     from autosysloguru import logger

#     IS_WIN32 = sys.platform == 'win32' or (getattr(os, '_name', False) == 'nt')

#     PathLike = Union[Path, str, None]

#     if sys.version_info[:2] >= (3, 6):
#         from pathlib import Path, PurePath
#     else:
#         from pathlib2 import Path, PurePath

#     try:
#         from locale import getpreferredencoding

#         DEFAULT_ENCODING = getpreferredencoding(do_setlocale=True)
#         del getpreferredencoding
#     except ImportError:
#         DEFAULT_ENCODING = 'utf-8'
#     except Exception:
#         DEFAULT_ENCODING = 'utf-8'
#         del getpreferredencoding

#     from setuptools import find_namespace_packages, setup

# if True:
#     PY3: bool = sys.version_info.major > 2

#     HOME: str = Path().home().as_posix()
#     HERE: str = Path(__file__).resolve().parent.as_posix()

#     if HERE not in PYTHONPATH:
#         PYTHONPATH.insert(0, HERE)

#     LOG_FORMAT: str = '{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}'
#     # choose a common location if you consolidate logs
#     LOG_LOCATION: str = f'{HERE}/logs/'


# def table_print(data: (Dict, Sequence), **kwargs):
#     tmp: List = []
#     if isinstance(data, dict):
#         tmp.extend(
#             [f'{str(k):<15.15} :  {repr(v):<45.45}' for k, v in data.items()],
#         )
#     elif isinstance(data, (list, tuple, set)):
#         for x in data:
#             try:
#                 tmp.append(f"{str(x):<15.15} :  {repr(f'{x}'):<45.45}")
#             except:
#                 tmp.append(f'{str(x)}')
#     else:
#         raise TypeError('Parameter must be an iterable Mapping or Sequence.')
#     print(NL.join(tmp), **kwargs)


# def pip_safe_name(s: str):
#     """ Return a name that is converted to pypi safe format. """
#     return s.lower().replace('-', '_').replace(' ', '_')


# def readme(file_name: str = 'readme.md', search_list: List[str] = []) -> str:
#     """ Returns the text of the file (defaults to README files)

#         The default file is `README.md` and is *NOT* case sensitive.
#         (e.g. `README` is the same as `readme`)
#         Can load *any* text file, but the default search path is setup
#         for readme files

#         ```
#         Search path = ["readme.md", "readme.rst", "readme", "readme.txt"]
#         ```

#         Example:

#         ```
#         long_description=readme()
#         ```
#         """

#     # add default search list for README files
#     if not search_list:
#         search_list = ['readme.md', 'readme.rst', 'readme', 'readme.txt']
#     # make sure 'file_name' is in 'search_list' at index 0
#     if file_name not in search_list:
#         search_list.insert(0, file_name)
#     found: bool = False
#     # traverse up through directory tree searching for each
#     # file in 'search_list'
#     for searchfile in search_list:
#         # search in this script's path and above
#         for parent in Path(file_name).resolve().parents:
#             find_path = Path(parent / searchfile)
#             if find_path.exists():
#                 found = True
#                 break
#         if found:
#             break
#     if found:
#         try:
#             with open(find_path, mode='r', encoding=DEFAULT_ENCODING) as f:
#                 return f.read()
#         except OSError:
#             raise OSError(
#                 f"Cannot read from the \
#                 'readme' file '{find_path}'",
#             )
#     else:
#         raise FileNotFoundError(
#             f"Cannot find project 'readme' file in project \
#                 tree. Search list = {search_list}",
#         )


# # ? **************************************** package metadata

# # the default package name is the name of the parent folder ...
# if not NAME:
#     NAME = Path(HERE).name

# # the default version number is '0.0.1'
# VERSION: str = '0.0.1'

# # make the name safe for Pypi.org upload
# NAME: str = pip_safe_name(module_name)

# VERSION_INFO: Tuple[int] = VERSION.split('.')
# DESCRIPTION: str = 'System utilities for Python on macOS.'
# REQUIRES_PYTHON: str = '>=3.8.0'

# # PACKAGE_DIR: Dict = {f'{NAME}'}
# PACKAGE_EXCLUDE: List[str] = ['*test*', '*bak*']
# LICENSE: str = 'MIT'
# LONG_DESCRIPTION: str = get_file_contents('README.md')
# LONG_DESCRIPTION_CONTENT_TYPE: str = 'text/markdown'
# # LONG_DESCRIPTION_CONTENT_TYPE="text/x-rst",

# URL: str = f'https://skeptycal.github.io/{NAME}/'
# DOWNLOAD_URL: str = f'https://github.com/skeptycal/{NAME}/archive/{VERSION}.tar.gz'
# ZIP_SAFE: bool = False
# # What packages are required for this module to be executed?
# REQUIRED: List[str] = [
#     "aiocontextvars>=0.2.0 ; python_version<'3.7'",
#     "colorama>=0.3.4 ; sys_platform=='win32'",
#     "win32-setctime>=1.0.0 ; sys_platform=='win32'",
# ]

# # What packages are optional?
# EXTRAS: Dict = {}

# PACKAGE_DATA: Dict = {
#     # If any package contains these files, include them:
#     '': [
#         '*.txt',
#         '*.rst',
#         '*.md',
#         '*.ini',
#         '*.png',
#         '*.jpg',
#         '__init__.pyi',
#         'py.typed',
#     ],
# }

# PROJECT_URLS: Dict = {
#     'Website': f'https://skeptycal.github.io/{NAME}/',
#     'Documentation': f'https://skeptycal.github.io/{NAME}/docs',
#     'Source Code': f'https://www.github.com/skeptycal/{NAME}/',
#     'Changelog':
#     f'https://github.com/skeptycal/{NAME}/blob/master/CHANGELOG.md',
# }

# PACKAGE_DIR: Dict =  {'include': f'{NAME.lower()}'}

# setup(
#     name=NAME,
#     project_urls=PROJECT_URLS,
#     package_dir=PACKAGE_DIR,
#     packages=find_packages(
#         f'{NAME}', exclude=PACKAGE_EXCLUDE,
#     ),
#     py_modules=[f'{NAME}'],
#     long_description=LONG_DESCRIPTION,
#     long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,

# )

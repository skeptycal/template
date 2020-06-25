#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pytest installs:
# Installing collected packages: py, attrs, more-itertools, pluggy, wcwidth, six, pyparsing, packaging, pytest
# Successfully installed attrs-19.3.0 more-itertools-8.4.0 packaging-20.4 pluggy-0.13.1 py-1.8.2 pyparsing-2.4.7 pytest-5.4.3 six-1.15.0 wcwidth-0.2.4

# pip install -U wheel pip setuptools
# pip install -U tox pylint

# Installing collected packages: toml, filelock, distlib, appdirs, virtualenv, tox, isort, lazy-object-proxy, wrapt, astroid, mccabe, pylint
# Successfully installed appdirs-1.4.4 astroid-2.4.2 distlib-0.3.0 filelock-3.0.12 isort-4.3.21 lazy-object-proxy-1.4.3 mccabe-0.6.1 pylint-2.5.3 toml-0.10.1 tox-3.15.2 virtualenv-20.0.24 wrapt-1.12.1

import re
import package_metadata as meta
from package_metadata import *
from dataclasses import dataclass, field, Field
from typing import Dict, List

RE_TAGS_STRING: str = r'<@([^>]*)>'
RE_TAGS_PATTERN: re.Pattern = re.compile(RE_TAGS_STRING)

# dictionary of tagged replacements --> straight replacement
project_tags : Dict = {
    'docs/config.yml': [
        NAME,
        AUTHOR_EMAIL,
        DESCRIPTION,
        URL,
        twitter_username,
        github_username,
        default_jekyll_theme,
    ],
    '.env': [
        NAME,
    ],
    '.travis.yml': [
        py_version,
    ],
    'AUTHORS': [
        copyright_end,
    ],
    'CODE_OF_CONDUCT.md': [
        AUTHOR_EMAIL,
    ],
    'CHANGELOG.md': [
        NAME,
    ],
    'LICENSE': [
        copyright_start,
        copyright_end,
        AUTHOR,
    ],
    'pyvenv.cfg': [
        py_version,
    ],
    'tox.ini': [
        py_versions_tested,
    ],
    'toxcov.ini': [
        py_versions_tested,
    ],
}

# dictionary of @replacements --> replace the line below with section
#   bounded by matching tags in the package_metadata.py file
at_tags : Dict = {
    'setup.py': [           # file to put data into
        'tags_metadata',    # first section
        'package_metadata', # second section
    ],
}


@dataclass
class MetaData:
    ''' Use the package metadata file to automate the initialization and
        maintenance of a new project repo.
        '''
    file_name: str = 'package_metadata.py'
    pattern_toggle: bool = False
    tags: Field = field(init=False)
    data: Field = field(init=False)
    pattern: re.Pattern = RE_TAGS_PATTERN

    def __post_init__(self):
        self.tags = at_tags
        self.data = self._get_file_data()
        pass

    def _get_file_data(self):
        ''' Returns text file content as a list of lines. '''
        return get_file_contents(self.file_name).splitlines()

    def index(self, value, start = 0, stop = -1):
        try:
            return self.data.index(value=value,start=start, stop=stop)
        except ValueError:
            return None

    def get_match(self, pattern):
        tmp: List[str] = []
        self.pattern_toggle = False
        # list(filter(self.r.match, self.data))
        self.data.index(f'<@{pattern}')
        for line in self.data:
            if pattern in line:
                if self.pattern_toggle:
                    return tmp
                else:
                    self.pattern_toggle = True
            elif self.pattern_toggle:
                tmp.append(line)

    def _get_tag_dict(self):
        ''' Find and return lines of text from the package_metadata.py
            file. The lines are bounded by the tags listed and are placed
            in the files listed.

            ```
            at_tags : Dict = {
                'setup.py': [           # file to put data into
                    'tags_metadata',    # first section
                    'package_metadata', # second section
                ],
            }

            # tag formatting:
            <@repl_tags>
            <@package_metadata>
            ```
            '''

        return at_tags

    def matches(self):
        # m.pattern.match(self.data)
        return list(filter(self.pattern.match, self.data))


# phone number for iPad or MacBook??? 361.827.0906

RE_TAGS_STRING: str = r'<@([^>]*)>'
r: re.Pattern = re.compile(RE_TAGS_STRING)

print(r.match)

m = MetaData()
print(m.file_name)
print(m.pattern)
print(m.matches())
# print(m.matches())
# meta.table_print(m.__dict__)

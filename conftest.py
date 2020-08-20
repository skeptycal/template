#!/usr/bin/env python3
''' conftest.py - pytest configuration test

    (keep one in the root directory to aid in module loading for pytest.)

    "Pytest looks for the conftest modules on test collection to gather custom
    hooks and fixtures, and in order to import the custom objects from them,
    pytest adds the parent directory of the conftest.py to the sys.path (in
    this case the repo directory)."

    Reference: https://stackoverflow.com/a/50610630
    '''

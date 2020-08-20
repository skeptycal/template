#!/usr/bin/env python3

import sys
import unittest


def _add(a: int, b: int) -> int:
    return a + b


class TestConfigBasics(unittest.TestCase):
    def test_add(self):
        self.assertEqual(_add(2, 3), 5, '2 + 3 == 5')
        self.assertFalse(_add(3, 4) == 5, '3 + 4 != 5')


def __main__(args=sys.argv[1:]):
    t = TestConfigBasics()


if __name__ == '__main__':
    __main__()

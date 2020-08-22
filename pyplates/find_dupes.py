#!/usr/bin/env python3

from collections import OrderedDict
from dataclasses import Field, dataclass, field
from functools import wraps, lru_cache
from inspect import ismethod
from os import PathLike, linesep as NL
from pathlib import Path
from time import time_ns as time

from loguru import logger
from more_itertools import unique_everseen
from collections import Counter

from typing import List, Union


# * ********************************** Profiler


@dataclass
class ProfileCode:
    """ A code profiler for python functions.

        - preps: dictionary of setup variables
        - tests: list of functions to test
        - n: number of trials to perform for timing tests
        """

    preps: OrderedDict
    tests: List
    n: int = 100
    verify: bool = True
    results: OrderedDict = field(default_factory=OrderedDict)
    times: OrderedDict = field(default_factory=OrderedDict)
    data: List = field(default_factory=list)
    data_str: str = ''

    def __post_init__(self):
        self.prep()
        self.run_tests()
        self.show_results()

    def prep(self):
        self.data = self.read_data(Path(self.preps['file_path']).resolve())
        self.data_str = NL.join(self.data)

    def get_tests(self):
        return [x for x in self.tests]

    @staticmethod
    def read_data(filename: PathLike) -> List[str]:
        with Path(filename).open(mode='rt') as f:
            return f.readlines()

    @staticmethod
    def write_data(filename: PathLike, data: List[str]):
        p: Path = Path(filename).resolve()
        logger.info(f'Saved file set to {p.name}.')
        temp_p: Path = p.rename(f'{p.name}.bak.{p.suffix}')
        logger.info(f'Backup file set to {temp_p.name}.')
        try:
            with p.open(mode='wt') as f:
                f.writelines(data)
            logger.info(f'New file saved to {f.name}.')
        except:
            logger.error(f'File {p.name} not saved!')
        finally:
            return p.exists()

    def run_trials(self, func):
        pass

    def run_tests(self):
        len0 = len(self.data)
        code: function
        for code in self.get_tests():
            retval = code(self.data)
            # TODO - this would be better ...
            # retval = capture_output(f"{code}({self.data})")
            # logger.debug(f"capture: {retval}")
            # if not retval: # if null for some reason ??
            #     logger.debug(f"{code.__name__} <retval>: {retval}")
            t0: float = time()
            for _ in range(self.n):
                try:
                    repeat = code(self.data)
                    # logger.debug(f"<retval> type: {type(retval)}")
                except:
                    pass
            # TODO - average?
            # dt: float = (time() - t0) // self.n # average
            dt: float = (time() - t0)
            self.results[code] = len(retval)

            # logger.debug(f" -> {self.results[code]}")
            logger.debug(f'{code.__name__} is {len(retval)} lines long.')
            self.times[code] = dt
            # logger.success(f"{code.__name__} removed {len0 - self.results[code]}.")
        return retval

    def show_results(self):
        print('=' * 60)
        print(f'  Remove Duplicates (number of timing trials = {self.n})')
        print('-' * 60)
        print('  function:                     dupes removed:    time:')
        print('-' * 60)
        for code, ln in self.results.items():
            dt = self.times[code]
            print(
                f"  {code.__name__:<30.30}  {str(ln):>5}         {int(dt/1000000):>4}.{str(dt/1000000).split('.')[1]:<2.2} ms"
            )
        print('-' * 60)


# * ********************************** functions to test


@dataclass
class CLI:
    width: int = 50
    top_char: str = '='
    mid_char: str = '-'
    bottom_char: str = '='

    def make_line(self, char: str = ''):
        """ Make a repeating string of 'char' substrings that is
            self.width characters long.

            params:
                char: str      string to repeat (default self.top_char)
            """
        if not char:
            char = self.top_char

        # speedup ... assumes it is unlikely to desire a string less
        #   than length 20 or to use a substring more than length 1
        char = char * 20
        while len(s) <= self.width:
            char = f'{char}{char}'
        return s[0 : self.width]

    @property
    def top(self):
        s: str = self.top_char
        while len(s) <= self.width:
            s += self.top_char


CLI_WIDTH = 50


def with_str(str_func):
    """ Custom __str__ wrapper.

        reference: https://stackoverflow.com/a/47452562

        """

    def wrapper(f):
        class FuncType:
            def __call__(self, *args, **kwargs):
                # call the original function
                return f(self, *args, **kwargs)

            def __str__(self):
                # call the custom __str__ function

                print('fake __str__ ')
                return str_func(self)

        # decorate with functool.wraps to make the resulting function appear like f
        print(wraps(f)(FuncType()))
        return wraps(f)(FuncType())

    return wrapper


class ProfileTests:
    def __init__(self, file_path: PathLike):
        self.file_path = file_path
        self._seq = ProfileCode.read_data(filename=self.file_path)
        self.top_char: str = '='
        self.width: int = 79

    def make_line(self, char: str = ''):
        """ Make a repeating string of 'char' substrings that is
            self.width characters long.

            params:
                char: str      string to repeat (default self.top_char)
            """
        if not char:
            char = self.top_char

        # speedup ... assumes it is unlikely to desire a string less
        #   than length 20 or to use a substring more than length 1
        char = char * 20
        while len(char) <= self.width:
            char = f'{char}{char}'
        return char[0 : self.width]

    def make_line_fast(self, char: str = ''):
        """ Make a repeating string of 'char' substrings that is
            self.width characters long.

            params:
                char: str      string to repeat (default self.top_char)
            """
        if not char:
            char = self.top_char

        # speedup ... assumes it is unlikely to desire a string less
        #   than length 20 or to use a substring more than length 1
        char = char * 20
        while len(char) <= self.width:
            char = f'{char}{char}'
        return char[0 : self.width]

    def control(self, seq):
        seen = []
        for x in seq:
            if x in seen:
                continue
            seen.append(x)
        return seen

    def no_op(self, seq):
        fake = list()
        for x in seq:
            if x == x:
                pass
        return seq

    def create_list(self, seq):
        fake = list(seq)
        return fake

    def create_tuple(self, seq):
        fake = tuple(seq)
        return fake

    def create_set(self, seq):
        fake = set(seq)
        return fake

    def enumerate_seq(self, seq):
        for i, line in enumerate(seq):
            if line.startswith('#'):
                continue
            if not line.strip():
                continue
            try:
                # print(f"{i:>3} {data[i]}")
                if seq[i] == seq[i + 1]:
                    # if data[i].strip():
                    # print(f"{i:>3} {seq[i]}")
                    pass
            except IndexError:
                pass
        return seq

    def list_set_seq(self, seq):
        return list(set(seq))

    def check_list_append(self, seq):
        seen = []
        for x in seq:
            if x in seen:
                continue
            seen.append(x)
        return seen

    def try_except_set(self, seq):
        seen = set()
        for x in seq:
            try:
                seen.add(x)
            except:
                pass
        return seen

    def try_except_tuple(self, seq):
        seen = tuple()
        for x in seq:
            try:
                seen = seen + x
            except:
                pass
        return seen

    def counter_list(self, seq):
        return Counter(seq).keys()

    def unique_everseen_no_key(self, seq):
        return list(unique_everseen(seq))

    def unique_everseen_tuple_key(self, seq):
        return list(unique_everseen(seq, key=tuple))

    def ordered_dict_keys(self, seq):
        return list(OrderedDict.fromkeys(seq))

    def seen_or_seen_add(self, seq):
        seen = set()
        seen_add = seen.add
        return [x for x in seq if not (x in seen or seen_add(x))]

    @property
    def seq(self):
        return self._seq

    def _methods(self):
        from inspect import getmembers, ismethod

        gm = getmembers(self, predicate=ismethod)
        return [x for x in gm if not x[0].startswith('_')]

    @property
    def tests(self):
        for x in self._methods():
            yield x[1]

    # def __iter__(self):
    #     self.n = 0
    #     return self.tests

    # def __next__(self):
    #     try:
    #         return self.tests
    #     except:
    #         raise StopIteration

    def alt_str(self):
        s: str = f"{'='*50}{NL}"
        s += f'Profiling Tests Database{NL}'
        s += f"{'-'*50}{NL}"
        s += f'  ... fake {NL}'
        logger.debug(f'function: {__name__}  class: {__class__()}')

        # s += f" file: {Path(file_path).resolve().name}){NL}"
        s += f' tests available: {NL}'
        s += f"{'-'*50}{NL}"

        # s = NL.join([f" - {x[0]}" for x in self._methods()])
        s += f"{NL}{'='*50}{NL}"

        return s

    @with_str(alt_str)
    def __str__(self):
        print('original __str__ ')
        return ''


# * ********************************** setup and run


def main(file_path: Union[Path, str]):
    from pprint import pprint

    preps: OrderedDict = OrderedDict(
        {'file_path': file_path,}
    )

    t = ProfileTests(file_path)

    print(t)
    # pprint(t._methods())
    # for x in t.tests:
    #     print(x)

    # p = ProfileCode(preps=preps, tests=tests, n=20, verify=True)


if __name__ == '__main__':
    from sys import argv

    if len(argv) > 1:
        file_path = argv[1]
    else:
        file_path = Path(
            '/Users/michaeltreanor/Documents/coding/template/tests/find_dupes_test.txt'
        )
    main(file_path=file_path)

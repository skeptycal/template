#!/usr/bin/env python3

from pathlib import Path
from os import PathLike
from typing import List
from more_itertools import unique_everseen
from loguru import logger
from collections import OrderedDict
from dataclasses import dataclass, field, Field
from timeit import timeit


def capture_output(code: str = "print('Hello, World!')"):
    import sys
    from io import StringIO

    # create file-like string to capture output
    with StringIO() as codeOut:
        with StringIO() as codeErr:
            # codeOut = StringIO()
            # codeErr = StringIO()

            # capture output and errors
            sys.stdout = codeOut
            sys.stderr = codeErr

            exec(code)

            # restore stdout and stderr
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__

            return (codeOut.getvalue(), codeErr.getvalue())
            # c_err = codeErr.getvalue()
            # c_out = codeOut.getvalue()

    # codeOut.close()
    # codeErr.close()

    # return (c_out, c_err)


def test_capture_output():
    code = """
    def f(x):
        x = x + 1
        return x

    print 'This is my output.'
    """
    capture_output(code)
    print(f(4))


def f1(seq):
    for i, line in enumerate(seq):
        if line.startswith('#'):
            continue
        if not line.strip():
            continue
        try:
            # print(f"{i:>3} {data[i]}")
            if seq[i] == seq[i + 1]:
                # if data[i].strip():
                print(f'{i:>3} {seq[i]}')
        except IndexError:
            pass

    data = list(set(seq))


def f3(seq):
    list(unique_everseen(seq))


def f4(seq):
    list(OrderedDict.fromkeys(seq))


def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


@dataclass
class ProfileCode:
    preps: OrderedDict
    tests: List
    results: OrderedDict = field(default_factory=OrderedDict)
    times: OrderedDict = field(default_factory=OrderedDict)
    data: List = field(default_factory=list)

    def __post_init__(self):
        self.prep()

        self.results = self.run_tests()

        self.show_results()

    def prep(self):
        self.data = self.read_data(Path(self.preps['file_path']).resolve())

    def repeat(self, func, *args, count=20, **kwargs):
        retval = 0
        for i in range(count):
            result = func(*args, **kwargs)[1]
            logger.info(
                f"'{func.__name__}' completed {i} trials of fib({i}) = {result}"
            )
            retval += result
        logger.info(f"'{func.__name__}' completed {count} repeats.")
        return retval

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

    def run_tests(self):
        len0 = len(self.data)
        retval: List[str] = []
        for code in self.tests:
            try:
                retval = code(self.data)
                self.results[code] = len(retval)
                self.times[code] = timeit(f'{code}({self.data})')
                logger.success(f'{code} removed {self.results[code]-len0}.')
            except:
                logger.info(f'{code} was not available.')
                raise
        return retval

    def show_results(self):
        print('function:     dupes removed:    time:')
        for code, ln in self.results.items():
            print(f'{code:<20.20} : {ln:>5}  ->  {self.times[code]}')


def main():
    file_path = (
        '/Users/michaeltreanor/Documents/coding/template/tests/find_dupes_test.txt'
    )
    preps: OrderedDict = OrderedDict(
        {'file_path': file_path,}
    )
    try:
        tests: List = [
            f1,
            # f2,
            f3,
            f4,
            # f5,
            # f6,
            f7,
        ]
    except:
        pass

    p = ProfileCode(preps, tests)


if __name__ == '__main__':
    main()

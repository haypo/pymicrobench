#!/usr/bin/env python3
"""Microbenchmark for function call overhead.

This measures simple function calls that are not methods, do not use varargs or
kwargs, and do not use tuple unpacking.
"""

import pyperf
from six.moves import xrange


def foo(a, b, c, d):
    # 20 calls
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)


def bar(a, b, c):
    # 20 calls
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)


def baz(a, b):
    # 20 calls
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)
    quux(a)


def quux(a):
    # 20 calls
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()


def qux():
    pass


def test_calls(loops):
    range_it = xrange(loops)
    t0 = pyperf.perf_counter()

    for loops in range_it:
        # 20 calls
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)
        foo(1, 2, 3, 4)

    return pyperf.perf_counter() - t0


if __name__ == "__main__":
    runner = pyperf.Runner()
    runner.metadata['description'] = ("Test the performance of simple "
                                      "Python-to-Python function calls")
    runner.bench_time_func('call_simple', test_calls, inner_loops=20)

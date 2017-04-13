import perf
import six
from six.moves import xrange

from pybench import Test

if six.PY3:
    long = int


class CompareIntegers(Test):

    version = 2.0
    operations = 30 * 5
    inner_loops = 30

    def test(self, loops):
        range_it = xrange(loops)
        t0 = perf.perf_counter()

        for _ in range_it:

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

            2 < 3
            2 > 3
            2 == 3
            2 > 3
            2 < 3

        return perf.perf_counter() - t0


class CompareFloats(Test):

    version = 2.0
    operations = 30 * 5
    inner_loops = 30

    def test(self, loops):
        range_it = xrange(loops)
        t0 = perf.perf_counter()

        for _ in range_it:

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

            2.1 < 3.31
            2.1 > 3.31
            2.1 == 3.31
            2.1 > 3.31
            2.1 < 3.31

        return perf.perf_counter() - t0


class CompareFloatsIntegers(Test):

    version = 2.0
    operations = 30 * 5
    inner_loops = 30

    def test(self, loops):
        range_it = xrange(loops)
        t0 = perf.perf_counter()

        for _ in range_it:

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

            2.1 < 4
            2.1 > 4
            2.1 == 4
            2.1 > 4
            2.1 < 4

        return perf.perf_counter() - t0


class CompareLongs(Test):

    version = 2.0
    operations = 30 * 5
    inner_loops = 30

    def test(self, loops):
        a = long(1234567890)
        b = long(3456789012345)
        range_it = xrange(loops)
        t0 = perf.perf_counter()

        for _ in range_it:

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

            a < b
            a > b
            a == b
            a > b
            a < b

        return perf.perf_counter() - t0

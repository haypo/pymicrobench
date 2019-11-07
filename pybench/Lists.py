# Ignore flake8 E741 warning in the whole file:
# flake8: noqa

import pyperf
from six.moves import xrange

from pybench import Test


class SimpleListManipulation(Test):

    version = 2.0
    operations = 5 * (6 + 6 + 6)
    inner_loops = 5

    def test(self, loops):

        l = []
        append = l.append
        range_it = xrange(loops)
        t0 = pyperf.perf_counter()

        for _ in range_it:

            append(2)
            append(3)
            append(4)
            append(2)
            append(3)
            append(4)

            l[0] = 3
            l[1] = 4
            l[2] = 5
            l[3] = 3
            l[4] = 4
            l[5] = 5

            x = l[0]
            x = l[1]
            x = l[2]
            x = l[3]
            x = l[4]
            x = l[5]

            append(2)
            append(3)
            append(4)
            append(2)
            append(3)
            append(4)

            l[0] = 3
            l[1] = 4
            l[2] = 5
            l[3] = 3
            l[4] = 4
            l[5] = 5

            x = l[0]
            x = l[1]
            x = l[2]
            x = l[3]
            x = l[4]
            x = l[5]

            append(2)
            append(3)
            append(4)
            append(2)
            append(3)
            append(4)

            l[0] = 3
            l[1] = 4
            l[2] = 5
            l[3] = 3
            l[4] = 4
            l[5] = 5

            x = l[0]
            x = l[1]
            x = l[2]
            x = l[3]
            x = l[4]
            x = l[5]

            append(2)
            append(3)
            append(4)
            append(2)
            append(3)
            append(4)

            l[0] = 3
            l[1] = 4
            l[2] = 5
            l[3] = 3
            l[4] = 4
            l[5] = 5

            x = l[0]
            x = l[1]
            x = l[2]
            x = l[3]
            x = l[4]
            x = l[5]

            append(2)
            append(3)
            append(4)
            append(2)
            append(3)
            append(4)

            l[0] = 3
            l[1] = 4
            l[2] = 5
            l[3] = 3
            l[4] = 4
            l[5] = 5

            x = l[0]    # noqa
            x = l[1]    # noqa
            x = l[2]    # noqa
            x = l[3]    # noqa
            x = l[4]    # noqa
            x = l[5]    # noqa

            if len(l) > 10000:
                # cut down the size
                del l[:]

        return pyperf.perf_counter() - t0


class ListSlicing(Test):

    version = 2.0
    operations = 25 * (3 + 1 + 2 + 1)

    def test(self, loops):

        n = list(range(100))
        r = list(range(25))
        range_it = xrange(loops)
        t0 = pyperf.perf_counter()

        for _ in range_it:

            l = n[:]

            for j in r:

                m = l[50:]     # noqa
                m = l[:25]     # noqa
                m = l[50:55]   # noqa
                l[:3] = n      # noqa
                m = l[:-1]     # noqa
                m = l[1:]      # noqa
                l[-1:] = n     # noqa

        return pyperf.perf_counter() - t0


class SmallLists(Test):

    version = 2.0
    operations = 5 * (1 + 6 + 6 + 3 + 1)
    inner_loops = 5

    def test(self, loops):

        range_it = xrange(loops)
        t0 = pyperf.perf_counter()

        for _ in range_it:

            l = []

            append = l.append
            append(2)
            append(3)
            append(4)
            append(2)
            append(3)
            append(4)

            l[0] = 3
            l[1] = 4
            l[2] = 5
            l[3] = 3
            l[4] = 4
            l[5] = 5

            l[:3] = [1, 2, 3]
            m = l[:-1]
            m = l[1:]

            l[-1:] = [4, 5, 6]

            l = []

            append = l.append
            append(2)
            append(3)
            append(4)
            append(2)
            append(3)
            append(4)

            l[0] = 3
            l[1] = 4
            l[2] = 5
            l[3] = 3
            l[4] = 4
            l[5] = 5

            l[:3] = [1, 2, 3]
            m = l[:-1]
            m = l[1:]

            l[-1:] = [4, 5, 6]

            l = []

            append = l.append
            append(2)
            append(3)
            append(4)
            append(2)
            append(3)
            append(4)

            l[0] = 3
            l[1] = 4
            l[2] = 5
            l[3] = 3
            l[4] = 4
            l[5] = 5

            l[:3] = [1, 2, 3]
            m = l[:-1]
            m = l[1:]

            l[-1:] = [4, 5, 6]

            l = []

            append = l.append
            append(2)
            append(3)
            append(4)
            append(2)
            append(3)
            append(4)

            l[0] = 3
            l[1] = 4
            l[2] = 5
            l[3] = 3
            l[4] = 4
            l[5] = 5

            l[:3] = [1, 2, 3]
            m = l[:-1]
            m = l[1:]

            l[-1:] = [4, 5, 6]

            l = []

            append = l.append
            append(2)
            append(3)
            append(4)
            append(2)
            append(3)
            append(4)

            l[0] = 3
            l[1] = 4
            l[2] = 5
            l[3] = 3
            l[4] = 4
            l[5] = 5

            l[:3] = [1, 2, 3]
            m = l[:-1]
            m = l[1:]    # noqa

            l[-1:] = [4, 5, 6]

        return pyperf.perf_counter() - t0


class SimpleListComprehensions(Test):

    version = 2.0
    operations = 6
    inner_loops = 2

    def test(self, loops):

        n = list(range(10)) * 10

        range_it = xrange(loops)
        t0 = pyperf.perf_counter()

        for _ in range_it:
            l = [x for x in n]
            l = [x for x in n if x]
            l = [x for x in n if not x]

            l = [x for x in n]
            l = [x for x in n if x]
            l = [x for x in n if not x]    # noqa

        return pyperf.perf_counter() - t0


class NestedListComprehensions(Test):

    version = 2.0
    operations = 6

    def test(self, loops):

        m = list(range(10))
        n = list(range(10))

        range_it = xrange(loops)
        t0 = pyperf.perf_counter()

        for _ in range_it:
            l = [x for x in n for y in m]
            l = [y for x in n for y in m]

            l = [x for x in n for y in m if y]
            l = [y for x in n for y in m if x]

            l = [x for x in n for y in m if not y]
            l = [y for x in n for y in m if not x]   # noqa

        return pyperf.perf_counter() - t0

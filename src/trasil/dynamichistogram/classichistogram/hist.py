from dataclasses import dataclass

import numpy as np

from trasil.dynamichistogram.std import cerr, cout


@dataclass
class Interval:
    left: float
    right: float
    k: int = 0

    def __contains__(self, x):
        return self.left <= x <= self.right

    def add(self, k=1):
        self.k += 1

    def f(self, m=1):
        return [self.left, self.right], [self.k / m, self.k / m]


class ClassicHistogram:
    def __init__(self, a, b, n):
        self.cs = [
            Interval(a + (b - a) / n * i, a + (b - a) / n * (i + 1)) for i in range(n)
        ]
        self.x = None
        self.y = None
        self.m = 0

    def add(self, x):
        self.x = self.y = None

        cout(f"{x = }", 32)
        for i in self.cs:
            if x in i:
                cout(i, 34)
                i.add()
                cout(i, 35)
                break
        else:
            cout(self.cs[-1], 34)
            self.cs[-1].add()
            cout(self.cs[-1], 35)
        self.m += 1
        cout("=================")

    def draw_hist(self, ax=None):
        for i in self.cs:
            x, y = i.f(self.m)
            ax.plot(x, y, "r")
            ax.fill_between(x, y)  # , color='FF999955')

    def _cdf(self):
        self.x = [self.cs[0].left]
        self.y = [0]
        for i in self.cs:
            self.x.append(i.right)
            self.y.append(self.y[-1] + i.k / self.m)

    def draw_cdf(self, ax=None):
        if self.x is None:
            self._cdf()

        ax.plot(self.x, self.y, "r")

    def cdf(self, x: np.array):
        def _cdf(x):
            if x <= self.cs[0].left:
                return 0
            if x >= self.cs[-1].right:
                return 1
            for i, inv in enumerate(self.cs):
                if x in inv:
                    a = inv.left
                    b = inv.right
                    ya = self.y[i]
                    yb = self.y[i + 1]
                    return ya + (x - a) * (yb - ya) / (b - a)

        if self.x is None:
            self._cdf()

        cdf = np.vectorize(_cdf, otypes=[float])
        return cdf(x)

    def mean(self):
        return 0

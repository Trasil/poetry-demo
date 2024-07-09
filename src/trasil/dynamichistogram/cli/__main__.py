#!/usr/bin/env python

import sys
from random import randint as irandom
from random import uniform as urandom

from matplotlib import pyplot as plt

from .demoscene import DemoScene
from .parser import get_parser



from trasil.dynamichistogram.classichistogram import ClassicHistogram as Hist
from trasil.dynamichistogram.std import *
def prepare_axs(a, b):
    fig = plt.figure(figsize=(18, 10))
    axs = tuple(fig.add_subplot(int(f"13{i+1}")) for i in range(3))
    for ax in axs[:2]:
        ax.set_xlim(a - 1, b + 1)
        ax.set_ylim(0, 1)
    return axs


def get_rand_func(a, b, type="int"):
    rand_func = {"int": irandom, "real": urandom}[type]
    return lambda: rand_func(a, b)


def main(args=sys.argv[1:]) -> int:
    args = get_parser().parse_args(args)

    hist = Hist(args.a, args.b, args.n)

    demo_scene = DemoScene(
        hist,  # cdfi  #, cdf
    )
    axs = prepare_axs(args.a, args.b)
    demo_scene.axs = axs[:2]

    rand = get_rand_func(args.a, args.b, args.random)

    # plt.pause(10)
    m = 0
    ddd = dict((i, 0) for i in range(int(args.a), int(args.b) + 1))

    try:
        file = None if args.output is None else open(args.output, "w")
        dd = []
        dd2 = []
        dd3 = []

        for _ in range(2):
            x = rand()
            demo_scene.add_dot(x)

            m += 1
            ddd[x] += 1

        while True:
            x = rand()
            # for x in range(0, 11):

            demo_scene.add_dot(x)
            demo_scene.draw_scene()

            m += 1
            ddd[x] += 1
            mean = sum([x * y / m for x, y in ddd.items()])
            variance = sum([y / m * (x - mean) ** 2 for x, y in ddd.items()])
            axs[0].plot([mean, mean], [0, 0.2], "r")

            # dd.append(demo_scene.get_cdf_diff(args.a, args.b))
            def difference(a, b):
                return abs((a - b) / (a + b))

            # m_dd  = difference(mean, cdfi.mean1())
            # m_dd2 = difference(mean, cdfi.mean2())
            # m_dd3 = difference(mean, cdfi.mean3())

            # v_dd  = difference(variance, cdfi.variance1())
            # v_dd2 = difference(variance, cdfi.variance2())
            # v_dd3 = difference(variance, cdfi.variance3())
            # v_dd4 = difference(variance, cdfi.variance4())
            #
            ##print(dd[-1], file=file)
            # axs[2].plot(m, m_dd, ' *g')
            # axs[2].plot(m, m_dd2, '*b')
            # axs[2].plot(m, m_dd3, '*y')
            # axs[2].plot(m, v_dd,  '.g')
            # axs[2].plot(m, v_dd2, '.b')
            # axs[2].plot(m, v_dd3, '.y')
            # axs[2].plot(m, v_dd4, '.c')
            # axs[2].set_yscale('log')

            plt.pause(0.5)

        cdfi.show()
        plt.show()
    except KeyboardInterrupt:
        pass

    finally:
        if file is not None:
            file.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())

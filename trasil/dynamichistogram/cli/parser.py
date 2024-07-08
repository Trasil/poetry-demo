import argparse


def get_parser():
    parser = argparse.ArgumentParser(description='Dynamic histogram work demo')

    parser.add_argument(
        'a',
        nargs='?', default=0, type=float,
        help='The left boundary of the uniform distribution of a random variable'
    )
    parser.add_argument(
        'b',
        nargs='?', default=10, type=float,
        help='The right boundary of the uniform distribution of a random variable'
    )
    parser.add_argument(
        'n',
        nargs='?', default=5, type=int,
        help='Number of histogram intervals'
    )
    parser.add_argument(
        'k',
        nargs='?', default=2, type=int,
        help='The number of points per one interval of the dynamic histogram'
    )
    parser.add_argument(
        '--random', '-r',
        choices=('int', 'real'),
        default='int',
        help='Set type of random variable: integer(int) or real(real)'
    )
    parser.add_argument(
        '--output', '-o',
        type=str, default=None,
        help='The name of the file in which information about the difference between normal and dynamic histograms will be placed'
    )

    return parser

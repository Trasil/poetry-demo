import pytest

from trasil.dynamichistogram.classichistogram.hist import Interval


@pytest.mark.parametrize(
    ("left", "right", "x", "contain"),
    (
        (0, 10, 0, True),
        (0, 10, 5, True),
        (0, 10, 10, False),
        (0, 10, -1, False),
    )
)
def test_interval(left, right, x, contain):
    assert (x in Interval(left, right)) == contain

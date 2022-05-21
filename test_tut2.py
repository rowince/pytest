from fun.tut2 import evenfun
from fun.tut2 import oddfun


def test_evenfun():
    inputt = [10, 4, 3, 5, 7, 2, 12]
    res = evenfun(inputt)
    out = [10, 4, 2, 12]
    assert res == out


def test_oddfun():
    inputt = [10, 4, 3, 5, 7, 2, 12]
    res = oddfun(inputt)
    out = [3, 5, 7]
    assert res == out

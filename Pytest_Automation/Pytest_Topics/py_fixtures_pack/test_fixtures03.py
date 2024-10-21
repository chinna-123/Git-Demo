import pytest

def test_delitem(setup01):
    del setup01[-1]
    print(setup01)
    assert setup01 == pytest.weekdays1


def test_removeitem(setup02):
    setup02.remove('thur')
    print(setup02)
    assert setup02 == pytest.weekdays2
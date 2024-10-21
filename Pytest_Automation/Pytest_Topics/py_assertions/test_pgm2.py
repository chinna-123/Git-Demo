import pytest


def test_case01():
    with pytest.raises(Exception):
        assert (1/0)
        assert 1 > 3

def test_case01():
    with pytest.raises(Exception) as excinfo:
        assert (1, 2, 3) == (1, 2, 4)
    print(excinfo)
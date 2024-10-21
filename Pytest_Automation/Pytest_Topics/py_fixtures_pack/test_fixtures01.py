import pytest


@pytest.fixture()
def setup_list():
    print('\n in fixtures...\n')
    city = ['New York', 'England', 'America', 'India', 'Mumbai', 'Kolkata']
    return city

def test_getItems(setup_list):  # Test is calling the fixture and fixture is passed as argument  to test-function
    print(setup_list[1:3])      # accessing the list from our fixtures
    assert setup_list[0] == 'New York'
    assert setup_list[::2] == ['New York', 'America', 'Mumbai']

def myReverse(lst):
    lst.reverse()
    return lst

def test_reverseList(setup_list):
    assert setup_list[::-2] == ['Kolkata', 'India', 'England']
    assert setup_list[::-1] == myReverse(setup_list)

@pytest.mark.xfail(reason="known issue: usefixtures can not use the fixture's return value")
@pytest.mark.usefixtures("setup_list")
def test_useFixturesDemo():
    assert 1 == 1
    assert (setup_list[0])

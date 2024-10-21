import pytest

months = ['Jan', 'Feb', 'Mar']

# Introspecting the requesting test with 'request' in fixture
def test_checkrequest(setup04):
    assert 'April' in setup04
    assert len(setup04) == 4


# Testing Factories as Fixture Scenario
def test_fact_fixture(setup05):
    assert type(setup05('list')) == list
    assert type(setup05('tuple')) == tuple
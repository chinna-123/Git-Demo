from pytest_bdd import scenario, given, when, then, scenarios
from pathlib import Path
import pytest


featureFileDir = 'myfeatures'
featureFile = 'first101.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)


def pytest_configure():  # global variable
    pytest.amt = 0

scenarios(featureFileDir)
# @scenario('first101.feature', 'withdrawal of money')
# def test_withdrawal():
#     print("End of withdrawal test")
#     pass


@given('the account balance is 100')
def current_balance():
    pytest.amt = 100


@when('the account holder withdraws 30')
def withdraw_amount():
    pytest.AMT = pytest.amt - 30


@then('the account balance should be 70')
def final_balance():
    assert pytest.amt == 70


# @scenario('first101.feature', 'Removal of items from a set')
# def test_removal():
#     pass


@given('A set of 3 fruits', target_fixture="myset")
def current_fruit():
    myset = {"apple", "banana", "orange"}
    return myset


@when('we remove a fruit from the set')
def remove_fruit(myset):
    myset.pop()
    print(myset)


@then('the set will have 2 fruits')
def final_set(myset):
    assert len(myset) == 2
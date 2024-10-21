import sys
import pytest

pytestmark = pytest.mark.skipif(sys.platform != 'win32', reason="will run only on linux Os")

const = 9/5
def cent_to_fah(cent=0):
    fah = (cent * const) + 32
    return fah
#print(cent_to_fah())

@pytest.mark.skip(reason="skipping for no reason")
def test_case01():
    assert type(const) == float

#@pytest.mark.skipif(sys.version_info < (3, 10), reason="does'nt work on py version above 3.10")
@pytest.mark.skipif(cent_to_fah() == 32, reason="default value test, so skipping")
def test_case02():
    assert cent_to_fah() == 32

def testt_case03():
    assert cent_to_fah(38) == 100.4

def test_a1():
    print("This is my first test")
    assert 5 + 5 == 10

# this is a failed test
def test_a2():
    assert 9 / 5 == 1, "failed intensionally"

def test_a3():
    assert 9 // 5 == 1 # Integer truncating division

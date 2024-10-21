
def test_a1():
    assert 5 > 4

def test_a2():
    assert 123     # 1 or True pass  0 or False id fail

def test_a3():
    assert "abc" == 'abcd'

def test_a4():
    assert ((3-1)*4/2) == 4.0

def test_a5():
    assert 1 in divmod(9, 5)
    assert 'put' not in 'this is python'
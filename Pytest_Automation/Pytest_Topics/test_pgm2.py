
class TestMyStuff():
    def test_type(self):
        assert type(1.5) == int

    def test_strs(self):
        assert str.upper('python') == 'PYTHON'
        assert 'pytest'.capitalize() == 'Pytest'
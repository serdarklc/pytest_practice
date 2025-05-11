import pytest

@pytest.mark.parametrize("a,b,expected", [(2,3,5),(4,5,9),(10,20,30)])
def test_sum(a,b,expected):
    assert a+b == expected
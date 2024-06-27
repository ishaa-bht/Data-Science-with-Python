def add(x,y):
    return x+y
def test_add_pass():
    assert add(2,3) == 5
    assert add(-2,3) == 1
def test_add_fail():
    assert add(2,3) == 6



from mypkg.main import multiply, add

def test_multiply():
    assert multiply(2, 3) == 6

def test_add():
    assert add(2, 3) == 5
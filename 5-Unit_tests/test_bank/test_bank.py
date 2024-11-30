from bank import value

def test_hello():
    assert value("hello") == 0

def test_partial():
    assert value("hi") == 20
    assert value("how") == 20

def test_wrong():
    assert value("sup") == 100

def test_upper():
    assert value("SUP") == 100
    assert value("HELLO") == 0
    assert value("HI") == 20

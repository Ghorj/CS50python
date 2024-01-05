from bank import value

def test_hello():
    assert value("hello, bruv") == 0
    assert value("HeLlo, bruv") == 0

def test_h():
    assert value("hi man") == 20
    assert value("Hi man") == 20

def test_other():
    assert value("ciao") == 100
    assert value("CIAO") == 100
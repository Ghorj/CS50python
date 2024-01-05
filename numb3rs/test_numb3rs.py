from numb3rs import validate

def test_number():
    assert validate("cat") == False
    assert validate("cat.cat.cat.cat") == False
    assert validate("0.0.0.cat") == False

def test_dot():
    assert validate("1?1?1?1") == False
    assert validate("1234321") == False
    assert validate("1a2b3cd") == False

def test_range():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.256") == False
    assert validate("555.555.555.555") == False

def test_length():
    assert validate("0.0.0.0.0") == False

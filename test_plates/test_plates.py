from plates import is_valid

def test_length():
    assert is_valid("A") == False
    assert is_valid("AAA9999") == False
    assert is_valid("AAA999") == True

def test_start():
    assert is_valid("A999") == False
    assert is_valid("999") == False

def test_first_number():
    assert is_valid("AA099") == False
    assert is_valid("AA909") == True

def test_punct():
    assert is_valid("AA.99") == False
    assert is_valid("AA 99") == False
    assert is_valid("AA!99") == False

def test_order():
    assert is_valid("AA9A9") == False
from um import count

def test_word():
    assert count("yummy") == 0
    assert count("mum") == 0
    assert count("umami") == 0

def test_multiple():
    assert count("yummy mum um") == 1
    assert count("um yummy mum um") == 2
    assert count("yummy um yuy yum um um") == 3

def test_symbols():
    assert count("um, yummy") == 1
    assert count("yummy, um?") == 1
    assert count("yummy, um, um? um. um)") == 4

def test_caps():
    assert count("Um, yummy") == 1
    assert count("UM, yummy") == 1
    assert count("uM, yummy") == 1


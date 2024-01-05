from twttr import shorten

def test_lower():
    assert shorten("hello world") == "hll wrld"

def test_upper():
    assert shorten("HELLO WORLD") == "HLL WRLD"

def test_mix():
    assert shorten("Schalke 04") == "Schlk 04"

def test_punct():
    assert shorten("Take.it.easy") == "Tk.t.sy"
import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("4/5") == 80
    with pytest.raises(ValueError):
        convert("6/5")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"

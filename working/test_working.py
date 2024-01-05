import pytest
from working import convert

def test_format():
    with pytest.raises(ValueError):
        convert("8:00 AM - 4:00 AM")
    with pytest.raises(ValueError):
        convert("8:0 AM to 4:0 AM")
    with pytest.raises(ValueError):
        convert("8:00 am to 4:00 pm")
    with pytest.raises(ValueError):
        convert("25:00 AM to 36 AM")

def test_first():
    assert convert("9 AM to 5 AM") == "09:00 to 05:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"

def test_second():
    assert convert("9 AM to 5 AM") == "09:00 to 05:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

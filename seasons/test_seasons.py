from seasons import how_long
import pytest

def test_format():
    with pytest.raises(ValueError):
        how_long("12 January, 2020")
    with pytest.raises(ValueError):
        how_long("12012020")
    with pytest.raises(ValueError):
        how_long("12-01-2020")
    with pytest.raises(ValueError):
        how_long("01-12-2020")
    with pytest.raises(ValueError):
        how_long("2020.01.12")

def test_today():
    assert how_long("2023-11-10") == "Zero minutes"

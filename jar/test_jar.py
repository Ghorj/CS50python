from jar import Jar
import pytest


def test_init():
    jar = Jar(10)
    assert jar.size == 0
    assert jar.capacity == 10
    jar2 = Jar()
    assert jar2.size == 0
    assert jar2.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit("cat")
    with pytest.raises(ValueError):
        jar.deposit(-1)
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(9)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.withdraw("cat")
    with pytest.raises(ValueError):
        jar.withdraw(-1)
    with pytest.raises(ValueError):
        jar.withdraw(1)
    jar.deposit(10)
    jar.withdraw(1)
    assert jar.size == 9
    jar.withdraw(3)
    assert jar.size == 6
    jar.withdraw(4)
    assert jar.size == 2

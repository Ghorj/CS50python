from project import Coffee_machine
import pytest

def test_take_coin():
    coffee_machine = Coffee_machine()
    assert coffee_machine.take_coin("£1") == 1.0
    assert coffee_machine.take_coin("0.5") == 1.5

    coffee_machine = Coffee_machine()
    with pytest.raises(ValueError):
        coffee_machine.take_coin("5")


def test_validate_coin():
    coffee_machine = Coffee_machine()
    assert coffee_machine.validate_coin(0.20) == True
    assert coffee_machine.validate_coin(0.50) == True

    assert coffee_machine.validate_coin(0.30) == False
    assert coffee_machine.validate_coin(3) == False


def test_choose_coffee():
    coffee_machine = Coffee_machine()
    assert coffee_machine.choose_coffee("latte") == {"name": "latte", "price": 1.0, "grains": 1, "milk": 2}
    assert coffee_machine.choose_coffee("cortado") == {"name": "cortado", "price": 0.75, "grains": 1, "milk": 1}

    with pytest.raises(ValueError):
        coffee_machine.choose_coffee("americano")


def test_check_credit():
    coffee_machine = Coffee_machine()
    coffee = {"name": "latte", "price": 1.0, "grains": 1, "milk": 2}
    coffee_machine.credit = 2
    assert coffee_machine.check_credit(coffee) == True

    coffee_machine = Coffee_machine()
    coffee = {"name": "latte", "price": 1.0, "grains": 1, "milk": 2}
    coffee_machine.credit = 0.5
    assert coffee_machine.check_credit(coffee) == False


def test_check_ingredients():
    coffee_machine = Coffee_machine()
    coffee = {"name": "latte", "price": 1.0, "grains": 1, "milk": 2}
    coffee_machine.grains = 2
    coffee_machine.milk = 3
    assert coffee_machine.check_ingredients(coffee) == True

    coffee = {"name": "latte", "price": 1.0, "grains": 1, "milk": 2}
    coffee_machine.grains = 0
    coffee_machine.milk = 1
    assert coffee_machine.check_ingredients(coffee) == False


def test_fill_ingredients():
    coffee_machine = Coffee_machine()
    coffee_machine.fill_ingredients()

    assert coffee_machine.grains == 10
    assert coffee_machine.milk == 10


def test_give_change():
    coffee_machine = Coffee_machine()
    coffee_machine.credit = 1.0

    assert coffee_machine.give_change() == 1.0
    assert coffee_machine.credit == 0.0


def test_convert_to_coins():
    coffee_machine = Coffee_machine()
    assert coffee_machine.convert_to_coins(1.0) == {"£1.00": 1}
    assert coffee_machine.convert_to_coins(1.01) == {"£1.00": 1, "£0.01": 1}
    assert coffee_machine.convert_to_coins(3.88) == {"£2.00": 1, "£1.00": 1, "£0.50": 1, "£0.20": 1, "£0.10": 1, "£0.05": 1, "£0.02": 1, "£0.01": 1}

    with pytest.raises(TypeError):
        coffee_machine.convert_to_coins("americano")
        

def test_make_coffee():
    coffee_machine = Coffee_machine()
    coffee = {"name": "latte", "price": 1.0, "grains": 1, "milk": 2}
    coffee_machine.credit = 2
    coffee_machine.grains = 2
    coffee_machine.milk = 3
    message = coffee_machine.make_coffee(coffee)
    assert message == f"\n      )  (\n     (   ) )\n      ) ( (\n mrf_______)_\n .-\'---------|\n( C|/\\/\\/\\/\\/|\n \'-./\\/\\/\\/\\/|\n   \'_________\'\n    \'-------\'  your latte, thank you!\n"

    coffee = {"name": "latte", "price": 1.0, "grains": 1, "milk": 2}
    coffee_machine.credit = 2
    coffee_machine.grains = 0
    coffee_machine.milk = 1
    message = coffee_machine.make_coffee(coffee)
    assert message == "Not enough ingredients"

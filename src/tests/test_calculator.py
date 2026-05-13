import pytest

"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

calc = Calculator()

def test_app():
    welcome_message = calc.get_hello_message()
    assert "== Calculatrice v1.0 ==" in welcome_message

def test_addition():
    assert calc.addition(2, 2) == 4
    assert calc.addition(2, -20) == -18

def test_subtraction():
    assert calc.subtraction(6,3) == 3
    assert calc.subtraction(-2, -4) == 2

def test_multiplication():
    assert calc.multiplication(7,8) == 56
    assert calc.multiplication(-1, -1) == 1

def test_division():
    assert calc.division(40, 8) == 5
    assert calc.division(10, -4) == -2.5
    assert calc.division(10, 0).find("division par zéro")
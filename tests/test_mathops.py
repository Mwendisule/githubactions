from src.mathops import *

def test_add():
    assert add(5, 12) == 17

def test_subtract():
    assert subtract(5, 12) == -7

def test_multiply():
    assert multiply(5, 12) == 60

def test_divide():
    assert divide(6, 12) == 0.5

def test_power():
    assert power(5, 3) == 125
    
def test_modulus():
    assert modulus(7, 4) == 3

def test_sqrt():
    assert sqrt(49) == 7
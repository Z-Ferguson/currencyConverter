# from currencyConverter import currencyConverter
from currency import Currency

def test_equals_six_dollars():
    a = Currency('USD', 6)
    b = Currency('USD', 6)
    assert a == b

def test_not_equals_equals_six_dollars():
    a = Currency('USD', 6)
    b = Currency('USD', 3)
    assert a != b

def test_currency_code():
    a = Currency('USD', 6)
    b = Currency('Euro', 6)
    assert a != b

def test_adding_currency():
    a = Currency('USD', 4)
    b = Currency('USD', 5)
    assert a + b == Currency('USD', 9)

def test_subtracting_currency():
    a = Currency('USD', 8)
    b = Currency('USD', 4)
    assert a - b == Currency('USD', 4)

def test_multiplying_currency():
    a = Currency('USD', 6)
    b = 5
    assert a * b == Currency('USD', 30)

def test_currency_code_arg():
    a = Currency('$6')
    b = Currency('USD', 6)
    assert a == b

from currency import Currency, DifferentCurrencyCodeError
from currencyConverter import CurrencyConverter, UnkownCurrencyCodeError
from nose.tools import raises


# currency object tests
def test_currency_value():
    one_dollar = Currency('$120')
    assert one_dollar.value == 120


def test_currency_code():
    dollar = Currency('$1')
    assert dollar.currency_code == 'USD'


def test_add_currency():
    forty_one_dollar = Currency('USD', 41)
    five_dollar = Currency('$5')
    assert forty_one_dollar + five_dollar == Currency('USD', 46)


def test_is_currency_equal():
    d = Currency('$1')
    d1 = Currency('$1')
    assert d == d1


def test_subtract_currency():
    three_dollars = Currency('$3')
    two_dollar = Currency('$2')
    assert three_dollars - two_dollar == Currency('USD', 1)


def test_multiply_currency():
    four_dollars = Currency('$4')
    assert four_dollars * four_dollars == Currency('USD', 16)


@raises(DifferentCurrencyCodeError)
def test_code_error():
    eight_dollars = Currency('USD', 8)
    four_great_british_pounds = Currency('GBP', 4)
    assert eight_dollars * four_great_british_pounds


# # CurrencyConverter object tests
# currency_rates = CurrencyConverter({'USD': 1.0, 'EUR': .91, 'RUB': 64.42})
#
#
# def test_usd_to_eur():
#     usd_object = Currency('$15')
#     assert currency_rates.convert(usd_object, 'EUR') == Currency('EUR', 13.65)
#
#
# def test_rub_to_usd():
#     rub_object = Currency('₽20')
#     assert currency_rates.convert(rub_object, 'USD') == Currency('USD', 0.31)
#
#
# def test_rub_to_eur():
#     rub_object = Currency('₽45')
#     assert currency_rates.convert(rub_object, 'EUR') == Currency('EUR', 0.64)
#
#
# def test_eur_to_rub():
#     eur_object = Currency('€4')
#     assert currency_rates.convert(eur_object, 'RUB') == Currency('RUB', 283.16)
#
#
# def test_eur_to_usd():
#     eur_object = Currency('€23')
#     assert currency_rates.convert(eur_object, 'USD') == Currency('USD', 25.27)
#
#
# @raises(UnkownCurrencyCodeError)
# def test_unkown_code():
#     usd_object = Currency('$5')
#     assert currency_rates.convert(usd_object, 'GBP')

from currency import Currency

rates = {'USD': 1, 'GBP': 0.82, 'EUR': 0.91}
class CurrencyConverter:
    def __init__(self, rates):
        pass


class UnknownCurrencyCodeError(Exception):
    pass

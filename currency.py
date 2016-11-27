class Currency:
    def __init__(self, currency_code, value=0):
        if value == 0:
            if currency_code[0] == '$':
                self.currency_code = 'USD'
                self.value = float(currency_code[1:])
            elif currency_code[0] == '€':
                self.currency_code = 'EUR'
                self.value = float(currency_code[1:])
            elif currency_code[0] == '£':
                self.currency_code = 'GBP'
                self.value = float(currency_code[1:])
        else:
            self.value = value
            self.currency_code = currency_code

    def __eq__(self, other):
        if self.currency_code == other.currency_code and self.value == other.value:
            return True
        return False

    def __add__(self, other):
        if self.currency_code == other.currency_code:
            return Currency(self.currency_code, self.value + other.value)
        else:
            raise Exception("DifferentCurrencyCodeError")

    def __sub__(self, other):
        if self.currency_code == other.currency_code:
            return Currency(self.currency_code, self.value - other.value)
        else:
            raise Exception("DifferentCurrencyCodeError")

    def __mul__(self, m):
        return Currency(self.currency_code, (self.value) * m)


class DifferentCurrencyCodeError(Exception):
    pass

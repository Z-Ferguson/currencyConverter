from currency import Currency


class CurrencyConverter:

    def __init__(self, conversion_dict):
        self.conversion_dict = conversion_dict

    def convert(self, from_currency, to_currency_code):
        try:
            rate = (self.conversion_dict[to_currency_code] / self.conversion_dict[from_currency.code])
            raw_value = rate * from_currency.value
            rounded_value = round(raw_value, 2)
            return Currency(to_currency_code, rounded_value)
        except:
            raise Exception("UnkownCurrencyCodeError")

    def __str__(self):
        return str(self.conversion_dict)


class UnkownCurrencyCodeError(Exception):
    pass

from libs.openexchange import OpenExchangeClient
import os

APP_ID = os.environ.get('OAR_APP_ID')

client = OpenExchangeClient(APP_ID)


def test(from_amount, from_currency, to_currency):
    to_amount = client.convert(from_amount, from_currency, to_currency)
    print(f"{from_currency} {from_amount} is {to_currency} {to_amount:.2f}")


test(1000, "USD", "EUR")
test(2000, "EUR", "USD")
test(1000, "EUR", "JPY")
test(5000, "JPY", "EUR")

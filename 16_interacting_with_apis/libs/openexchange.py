import requests
from cachetools import cached, TTLCache

# The free access layer to the API returns foreign currencies relative to USD.
# When we want to convert between two other currencies, say JPY and EUR, we
# need to convert one of them to USD first. ANd then convert further.

class OpenExchangeClient:
    BASE_URL = "https://openexchangerates.org/api/"

    def __init__(self, app_id):
        self.app_id = app_id

    def __make_url(self, endpoint: str) -> str:
        return f"{self.BASE_URL}{endpoint}?app_id={self.app_id}"

    @property
    @cached(cache=TTLCache(maxsize=2, ttl=900))
    def latest(self):
        url = self.__make_url("latest.json")
        return requests.get(url).json()
    
    def convert(self, from_amount: float, from_currency: str, to_currency: str) -> float:
        rates = self.latest["rates"]
        to_rate = rates[to_currency]

        if from_currency == "USD":
            return from_amount * to_rate
        else:
            from_in_usd = from_amount / rates[from_currency]
            return from_in_usd * to_rate

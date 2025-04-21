import requests
from decouple import config


class ExchangeRateService:
    EXCHANGE_RATE_API_KEY = config("EXCHANGE_RATE_API_KEY")
    BASE_URL = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/latest/USD"
    SUPPORTED_CURRENCIES = ["USD", "BRL", "EUR", "JPY"]

    @classmethod
    def get_rates(cls):
        try:
            response = requests.get(cls.BASE_URL)
            response.raise_for_status()

            data = response.json()
            response_result = data.get("result")
            if response_result == "error" and data.get("error-type") == "invalid-key":
                raise ValueError("Invalid API key for ExchangeRate API")

            if data["result"] != "success":
                raise ValueError("Failed to fetch exchange rates")

            rates = data["conversion_rates"]
            return {currency: rates[currency] for currency in cls.SUPPORTED_CURRENCIES}

        except requests.RequestException as e:
            raise ConnectionError(f"Error fetching exchange rates: {e}")
        except KeyError as e:
            raise ValueError(f"Missing expected currency in response: {e}")
        except ValueError as e:
            raise e

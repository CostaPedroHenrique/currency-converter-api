from decimal import Decimal

from .exchangeRateService import ExchangeRateService


class ConversionService:
    """
    Service for converting currencies using exchange rates.
    """

    @staticmethod
    def convert_currency(source_currency, target_currency, amount):

        rates = ExchangeRateService.get_rates()
        if source_currency not in rates or target_currency not in rates:
            raise ValueError("Unsupported currency.")

        # Convert amount to Decimal
        amount = Decimal(amount)

        # Convert rates to Decimal
        conversion_rate = Decimal(rates[target_currency]) / Decimal(
            rates[source_currency]
        )

        # Calculate the converted amount
        converted_amount = amount * conversion_rate

        return {
            "converted_amount": converted_amount,
            "conversion_rate": conversion_rate,
            "source_currency": source_currency,
            "target_currency": target_currency,
        }

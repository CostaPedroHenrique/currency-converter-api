from decimal import Decimal


class ConversionService:
    @staticmethod
    def get_conversion_rates():
        """
        Mocked method to return the currency conversion rates.
        Returns a simulated response, mimicking the response
        from a currency conversion API.
        """
        return {
            "success": True,
            "timestamp": 1744849144,
            "base": "EUR",
            "date": "2025-04-17",
            "rates": {
                "BRL": 6.679223,
                "USD": 1.138265,
                "EUR": 1,
                "JPY": 161.8636,
            },
        }

    @staticmethod
    def convert_currency(source_currency, target_currency, amount):
        """
        Mocked method to convert an amount from one currency to another.
        Returns the converted amount, the conversion rate, and the currencies involved.
        """
        conversion_rates = ConversionService.get_conversion_rates()
        if not conversion_rates["success"]:
            raise Exception("Failed to get conversion rates.")

        rates = conversion_rates["rates"]
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

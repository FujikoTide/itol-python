from exchange_rates import RATES


# accepts USD, EUR, GBP, JPY
def convert_currency(amount: float, currency_from: str, currency_to: str) -> float:
    converted_amount = round(RATES[currency_from][currency_to] * amount, 2)
    print(
        f"Converting {currency_from} to {currency_to}: {amount} {currency_from} is {converted_amount} {currency_to}."
    )
    return converted_amount


convert_currency(100, "USD", "EUR")
convert_currency(100, "JPY", "EUR")
convert_currency(100, "USD", "GBP")
convert_currency(100, "GBP", "JPY")
convert_currency(100, "EUR", "USD")

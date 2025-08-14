from currency_converter import convert_currency


def main():
    convert_currency(100, "USD", "EUR")
    convert_currency(100, "JPY", "EUR")
    convert_currency(100, "USD", "GBP")
    convert_currency(100, "GBP", "JPY")
    convert_currency(100, "EUR", "USD")


if __name__ == "__main__":
    main()

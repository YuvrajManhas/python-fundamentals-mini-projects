from converter import convert_currency

print("\nWelcome to Currency Converter")
print("*" * 30)
from_currency = input("Enter from Currency: ").upper()
to_currency = input("Enter to Currency: ").upper()
amount = float(input("Enter Amount: "))

result = convert_currency(from_currency, to_currency, amount)


if result:
    print("Calculated amount:", result["conversion_result"])
else:
    print("Conversion failed")

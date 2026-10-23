
from decimal import Decimal, ROUND_HALF_UP

def calculate_payment(litres, rate):
    litres = Decimal(str(litres))
    rate = Decimal(str(rate))
    amount = litres * rate
    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


try:
    litres = input("Enter milk quantity in litres: ")
    rate = input("Enter rate per litre: ")

    payment = calculate_payment(litres, rate)

    if Decimal(litres) <= 0 or Decimal(rate) < 0:
        print("Quantity must be positive and rate cannot be negative.")
    else:
        print("Milk payment: ₹", payment)

except Exception:
    print("Invalid input. Please enter valid numbers.")

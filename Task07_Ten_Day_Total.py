
from decimal import Decimal, ROUND_HALF_UP

def calculate_ten_day_total(payments):
    total = sum(
        (Decimal(str(payment)) for payment in payments),
        Decimal("0.00")
    )
    return total.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )


payments = []

for day in range(1, 11):
    value = input(f"Enter payment for day {day}: ")

    try:
        payment = Decimal(value)

        if payment < 0:
            print("Payment cannot be negative. Using 0 for this day.")
            payment = Decimal("0.00")

        payments.append(payment)

    except Exception:
        print("Invalid amount. Using 0 for this day.")
        payments.append(Decimal("0.00"))


total = calculate_ten_day_total(payments)
print("Total payment for ten days: ₹", total)


from decimal import Decimal, ROUND_HALF_UP

def calculate_payment(litres, rate):
    amount = Decimal(str(litres)) * Decimal(str(rate))
    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


entries = []

number = int(input("How many milk entries? "))

for i in range(number):
    print(f"\nEntry {i + 1}")
    farmer_id = input("Farmer ID: ")
    litres = input("Milk quantity in litres: ")
    rate = input("Rate per litre: ")

    try:
        payment = calculate_payment(litres, rate)
        if Decimal(litres) <= 0 or Decimal(rate) < 0:
            print("Invalid quantity or rate. Entry skipped.")
            continue

        entries.append({
            "farmer_id": farmer_id,
            "litres": Decimal(litres),
            "rate": Decimal(rate),
            "payment": payment
        })

        print("Payment: ₹", payment)

    except Exception:
        print("Invalid number. Entry skipped.")

print("\nPayment Summary")
for entry in entries:
    print(
        entry["farmer_id"],
        "- ₹",
        entry["payment"]
    )

print("Valid entries:", len(entries))

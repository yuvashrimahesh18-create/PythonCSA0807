
from decimal import Decimal

def find_highest_payment(entries):
    if not entries:
        print("No valid entries available.")
        return

    highest = max(entries, key=lambda entry: entry["payment"])

    print("\nHighest Payment Record")
    print("Farmer ID:", highest["farmer_id"])
    print("Milk quantity:", highest["litres"], "litres")
    print("Payment: ₹", highest["payment"])


entries = []

number = int(input("How many entries? "))

for i in range(number):
    print(f"\nEntry {i + 1}")
    farmer_id = input("Farmer ID: ")

    try:
        litres = Decimal(input("Milk quantity in litres: "))
        rate = Decimal(input("Rate per litre: "))

        if litres <= 0 or rate < 0:
            print("Invalid quantity or rate. Entry skipped.")
            continue

        payment = (litres * rate).quantize(Decimal("0.01"))

        entries.append({
            "farmer_id": farmer_id,
            "litres": litres,
            "payment": payment
        })

    except Exception:
        print("Invalid input. Entry skipped.")

find_highest_payment(entries)

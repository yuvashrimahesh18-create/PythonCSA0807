
from decimal import Decimal, ROUND_HALF_UP

def farmer_report(entries, farmer_id):
    farmer_entries = [
        entry for entry in entries
        if entry["farmer_id"] == farmer_id
    ]

    total_litres = sum(
        (entry["litres"] for entry in farmer_entries),
        Decimal("0")
    )

    total_payment = sum(
        (entry["payment"] for entry in farmer_entries),
        Decimal("0.00")
    ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    print("\nFarmer Payment Report")
    print("Farmer ID:", farmer_id)
    print("Number of entries:", len(farmer_entries))
    print("Total litres:", total_litres)
    print("Total payment: ₹", total_payment)


entries = []

number = int(input("How many entries do you want to record? "))

for i in range(number):
    print(f"\nEntry {i + 1}")
    farmer_id = input("Farmer ID: ")
    litres = Decimal(input("Milk quantity in litres: "))
    rate = Decimal(input("Rate per litre: "))

    if litres <= 0 or rate < 0:
        print("Invalid quantity or rate. Entry skipped.")
        continue

    payment = (litres * rate).quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )

    entries.append({
        "farmer_id": farmer_id,
        "litres": litres,
        "payment": payment
    })

search_id = input("\nEnter farmer ID for the report: ")
farmer_report(entries, search_id)

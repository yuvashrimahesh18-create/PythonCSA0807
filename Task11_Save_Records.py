
import csv
from decimal import Decimal, ROUND_HALF_UP

FILENAME = "milk_records.csv"

def save_record(farmer_id, litres, fat, snf, shift, rate, payment):
    with open(FILENAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            farmer_id,
            litres,
            fat,
            snf,
            shift,
            rate,
            payment
        ])


try:
    farmer_id = input("Enter farmer ID: ").strip()
    litres = Decimal(input("Enter milk quantity in litres: "))
    fat = Decimal(input("Enter fat percentage: "))
    snf = Decimal(input("Enter SNF percentage: "))
    shift = input("Enter shift (Morning/Evening): ").strip().title()

    if not farmer_id:
        raise ValueError("Farmer ID cannot be empty.")
    if litres <= 0:
        raise ValueError("Quantity must be greater than zero.")
    if not Decimal("2.0") <= fat <= Decimal("7.0"):
        raise ValueError("Fat must be between 2.0 and 7.0.")
    if snf <= 0:
        raise ValueError("SNF must be greater than zero.")
    if shift not in ("Morning", "Evening"):
        raise ValueError("Shift must be Morning or Evening.")

    fat_change = (fat - Decimal("3.5")) / Decimal("0.1")
    snf_change = (snf - Decimal("8.5")) / Decimal("0.1")

    rate = (
        Decimal("30.00")
        + fat_change * Decimal("0.40")
        + snf_change * Decimal("0.30")
    ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    payment = (litres * rate).quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )

    save_record(farmer_id, litres, fat, snf, shift, rate, payment)

    print("Rate per litre: ₹", rate)
    print("Payment: ₹", payment)
    print("Record saved to", FILENAME)

except Exception as error:
    print("Error:", error)

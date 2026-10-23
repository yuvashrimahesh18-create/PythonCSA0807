
from decimal import Decimal

MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")
MIN_LITRES = Decimal("0")

def validate_entry(farmer_id, litres, fat, snf, shift):
    errors = []

    if not farmer_id.strip():
        errors.append("Farmer ID cannot be empty.")

    try:
        litres = Decimal(str(litres))
        if litres <= MIN_LITRES:
            errors.append("Milk quantity must be greater than zero.")
    except Exception:
        errors.append("Milk quantity must be a number.")

    try:
        fat = Decimal(str(fat))
        if not MIN_FAT <= fat <= MAX_FAT:
            errors.append("Fat must be between 2.0% and 7.0%.")
    except Exception:
        errors.append("Fat must be a number.")

    try:
        snf = Decimal(str(snf))
        if snf <= 0:
            errors.append("SNF must be greater than zero.")
    except Exception:
        errors.append("SNF must be a number.")

    if shift.strip().lower() not in ("morning", "evening"):
        errors.append("Shift must be Morning or Evening.")

    return errors


farmer_id = input("Enter farmer ID: ")
litres = input("Enter milk quantity: ")
fat = input("Enter fat percentage: ")
snf = input("Enter SNF percentage: ")
shift = input("Enter shift (Morning/Evening): ")

errors = validate_entry(farmer_id, litres, fat, snf, shift)

if errors:
    print("Entry is invalid:")
    for error in errors:
        print("-", error)
else:
    print("Entry is valid.")

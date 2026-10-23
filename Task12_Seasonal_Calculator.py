
from decimal import Decimal, ROUND_HALF_UP

def calculate_rate(fat, snf, month):
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))

    if month in (4, 5, 6):
        base_rate = Decimal("32.00")
        fat_step_value = Decimal("0.45")
    else:
        base_rate = Decimal("30.00")
        fat_step_value = Decimal("0.40")

    standard_fat = Decimal("3.5")
    standard_snf = Decimal("8.5")

    fat_change = (fat - standard_fat) / Decimal("0.1")
    snf_change = (snf - standard_snf) / Decimal("0.1")

    rate = (
        base_rate
        + fat_change * fat_step_value
        + snf_change * Decimal("0.30")
    )

    return rate.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )


try:
    farmer_id = input("Enter farmer ID: ")
    litres = Decimal(input("Enter milk quantity in litres: "))
    fat = Decimal(input("Enter fat percentage: "))
    snf = Decimal(input("Enter SNF percentage: "))
    month = int(input("Enter month number (1-12): "))
    ten_day_litres = Decimal(
        input("Enter total litres supplied in ten days: ")
    )

    if not farmer_id.strip():
        raise ValueError("Farmer ID cannot be empty.")
    if litres <= 0 or ten_day_litres < 0:
        raise ValueError("Milk quantities must be valid.")
    if not Decimal("2.0") <= fat <= Decimal("7.0"):
        raise ValueError("Fat must be between 2.0 and 7.0.")
    if snf <= 0:
        raise ValueError("SNF must be greater than zero.")
    if not 1 <= month <= 12:
        raise ValueError("Month must be between 1 and 12.")

    rate = calculate_rate(fat, snf, month)
    payment = litres * rate

    bonus = Decimal("0.00")
    if month in (4, 5, 6) and ten_day_litres > 500:
        bonus = litres * Decimal("0.50")

    total = (payment + bonus).quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )

    print("\n--- Milk Payment Summary ---")
    print("Farmer ID:", farmer_id)
    print("Rate per litre: ₹", rate)
    print("Milk payment: ₹", payment.quantize(Decimal("0.01")))
    print("Seasonal bonus: ₹", bonus.quantize(Decimal("0.01")))
    print("Total payment: ₹", total)

except Exception as error:
    print("Error:", error)


from decimal import Decimal

BASE_RATE = Decimal("30.00")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")


def calculate_rate(fat, snf):
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))

    fat_change = (fat - STANDARD_FAT) / Decimal("0.1")
    snf_change = (snf - STANDARD_SNF) / Decimal("0.1")

    rate = BASE_RATE + fat_change * FAT_STEP_VALUE + snf_change * SNF_STEP_VALUE
    return rate.quantize(Decimal("0.01"))


fat = input("Enter fat percentage: ")
snf = input("Enter SNF percentage: ")

try:
    rate = calculate_rate(fat, snf)
    print("Rate per litre: ₹", rate)
except Exception:
    print("Invalid input. Please enter numeric fat and SNF values.")

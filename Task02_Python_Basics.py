from decimal import Decimal

# Integer and float examples
quantity = 10
price = 12.5

print("Integer:", quantity)
print("Float:", price)

# Division operators
print("Normal division:", 7 / 2)
print("Floor division:", 7 // 2)
print("Remainder:", 7 % 2)
print("-7 // 2 =", -7 // 2)

# Floating-point precision
items = [0.1] * 100
print("float  :", sum(items))

# Decimal for accurate money
def total_decimal(items):
    return sum(items, Decimal("0.00"))

decimal_items = [Decimal("0.10")] * 100
print("Decimal:", total_decimal(decimal_items))

print(0.1 + 0.2 == 0.3)
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
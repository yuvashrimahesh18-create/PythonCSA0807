
def count_shifts(entries):
    morning = 0
    evening = 0

    for entry in entries:
        shift = entry.strip().lower()

        if shift == "morning":
            morning += 1
        elif shift == "evening":
            evening += 1

    return morning, evening


shifts = []

number = int(input("How many entries do you want to record? "))

for i in range(number):
    shift = input(f"Enter shift for entry {i + 1} (Morning/Evening): ")
    shifts.append(shift)

morning_count, evening_count = count_shifts(shifts)

print("Morning entries:", morning_count)
print("Evening entries:", evening_count)
print("Total entries:", morning_count + evening_count)

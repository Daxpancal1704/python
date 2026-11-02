

import csv

data = [
    ["name", "age", "salary"],
    ["Asha", "25", "50000"],
    ["Raj", "30", "60000"],
    ["Asha", "25", "50000"],  # Duplicate
    ["Mira", "", "45000"],    # Missing age
    ["Dev", "22", "30000"],
    ["Neha", "28", ""],       # Missing salary
]

with open("sample.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("sample.csv created successfully")

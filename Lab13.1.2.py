import csv
current_year=2025
csv_path="banks.csv"

file=open(csv_path, "r")
reader=csv.reader(file)

next(reader)

print("Вік банків у 2025 році: \n")

for row in reader:
    name=row[0]
    year=int(row[1])
    age=current_year-year
    print(name, "-", age, "років")

file.close()
import csv
banks={
    "ПриватБанк": 1992,
    "Ощадбанк": 1991,
    "Монобанк": 2017,
    "Альфа-Банк": 1993,
    "ПУМБ": 1991,
    "Укрексімбанк": 1992,
    "Райффайзен Банк": 1996,
    "Креді Агріколь": 1993,
    "Укргазбанк": 1993,
    "Ідея банк": 1989,
    "Кредобанк": 1990,
    "МТБ Банк": 1993
}
with open("banks.csv", "w", newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["Назва банку", "Рік створення"])
    for name, year in banks.items():
        writer.writerow([name, year])
print("Дані записано у файл.")

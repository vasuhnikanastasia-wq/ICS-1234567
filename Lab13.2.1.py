import json
datas=[["Вода", 1000],
       ["Олія", 920],
       ["Бензин", 710],
       ["Молоко", 1030],
       ["Ртуть", 13500],
       ["Етанол", 790]]

liquids={}
for i in datas:
    liquids[i[0]]=i[1]

with open("liquids.json", "w")as write_file:
    json.dump(liquids, write_file)

print("Файл створено.")

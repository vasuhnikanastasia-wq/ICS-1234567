import shelve
countries={}

print("Введіть 10 країн і їх площу:")

for i in range(10):
    name=input("Назва країни: ")
    area=float(input("Площа у км^2: "))
    countries[name]=area

temp=countries.copy()
top3={}
for i in range(3):
    max_country=max(temp, key=temp.get)
    top3[max_country]=temp[max_country]
    del temp[max_country]

print("Три найбльші країни:")
for k, v in top3.items():
    print(k, "-", v, "км^2")

db=shelve.open("africa.dat")
db["top3"]=top3
db.close()

print("Дані записані у файл.")
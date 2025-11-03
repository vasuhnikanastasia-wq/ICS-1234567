import shelve
db=shelve.open("africa.dat")

if "top3" in db:
    top3=db["top3"]
    print("Три країни з найбільшою площею: ")
    for country, area in top3.items():
        print(country, "-", area, "км^2")
else: 
    print("У файлі немає даних з ключем 'top3'. ")

db.close()
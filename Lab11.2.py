countries={"Алжир": 2382,
           "Єгипет": 1001,
           "Туніс": 164,
           "Чад": 1284,
           "Лівія": 1760,
           "Марокко": 446,
           "Габон": 268,
           "Гана": 239,
           "Ерітрея": 118,
           "Ефіопія": 1104
}
f=open("africa.txt", "w")
for kraina in countries:
    plosha=countries[kraina]
    line=kraina+ ":" +str(plosha) + "\n"
    f.write(line)

f.close()
print("Файл успішно створено і заповнено!")
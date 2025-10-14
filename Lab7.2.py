numbers=[]
for i in range(10, 100):
    if i % 2 == 0:
        numbers.append(i)
print("Список парних двоцифрових:", numbers)    

last_six=numbers[-6:]
print("Останні 6 чисел:", last_six)

suma=sum(last_six)
print("Сума останніх 6 чисел =", suma)
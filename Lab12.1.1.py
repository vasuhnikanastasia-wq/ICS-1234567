import pickle
List1=[]
for i in range(100, 1000):
    if i % 42 ==0:
        List1.append(i)

Result=[]
for num in List1:
    if num % 10 == 4:
        Result.append(num)

print("Всі числа кратні 42:", List1)
print("Числа, що підходять: ", Result)

f=open("numbers4.dat", "wb")
pickle.dump(Result, f)
f.close()
print("Дані записано у файл.")
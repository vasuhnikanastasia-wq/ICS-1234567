A=[]
B=[]
n=int(input("Скільки елементів у масиві A і B? "))
for i in range(n):
    A.append(2** i)

for i in range(n):
    B.append(3** i)

print("Масив A:", A)
print("Масив B: ", B)
C=A+B
C.sort()
print("Об'єднаний і відсортований масив:", C)

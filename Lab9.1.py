import array
import random

min_val=int(input("Введіть мінімальне число: "))
max_val=int(input("Введіть максимальне число: "))
mas=array.array("i", [])

for i in range(10):
    num=random.randint(min_val, max_val)
    mas.append(num)
print("Масив:", mas)

sum_first= 0
for i in range(5):
    sum_first +=mas[i]
print("Сума першої половини: ", sum_first)

sum_second=0
for i in range(5, 10):
    sum_second +=mas[i]
avg_second=sum_second /5
print("Середнє другої половини: ", avg_second)

search_num=int(input("Введіть число для пошуку:"))

found=False 
for i in range(10):
    if mas[i] ==search_num:
        print("Є. Це елемент під номером", i)
        found=True
        break

if not found:
    print("Такого числа немає у масиві.")
import math
P=lambda a, b, c: a+b+c
S=lambda a, b, c: math.sqrt(P(a, b, c)/2*(P(a, b, c)/2-a)*(P(a, b, c)/2-b)*(P(a, b, c)/2-c))

a=float(input("Введіть сторону а: "))
b=float(input("Введіть сторону b: "))
c=float(input("Ввеіть сторону с: "))

print("Периметр= ", P(a, b, c))
print("Площа=", S(a, b, c))
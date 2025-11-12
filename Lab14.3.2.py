import figures
print("1 - трикутник")
print("2 - прямокутник")
choice=int(input("Введіть фігуру: "))

if choice ==1:
    a=float(input("a= "))
    b=float(input("b= "))
    c=float(input("c= "))
    print("Площа:", figures.area(a, b, c))
    print("Периметр:", figures.perimetr(a, b, c))
else:
    a=float(input("a= "))
    b=float(input("b= "))
    print("Площа:", figures.area(a, b))
    print("Периметр: ", figures.perimetr(a, b))

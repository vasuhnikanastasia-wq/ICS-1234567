import math
a=float(input("Введіть нижню межу a: "))
b=float(input("Введіть верхню межу b: "))
h=float(input("Введіть крок h: "))
n=int((b-a)/h)+1
for i in range(n):
    x=a+i*h
    try:
        y=abs(math.log(abs(x+1)))+math.exp(2*x-4)
        print(f"x={x:.2f}, f(x)={y:.4f}")
    except ValueError:
        print(f"x={x:.2f}, f(x) не обчислюється(помилка)")
import math
a=float(input("Введіть нижню межу a: "))
b=float(input("Введіть верхню межу b: "))
h=float(input("Введіть крок h: "))
x=a
while x <= b:
    try:
        y=math.pow(x, math.e)+x/7+math.exp(x)
        print(f"x={x:.2f}, f(x)={y:.4f}")
    except ValueError:
        print(f"x={x:.2f}, f(x) не обчислюється(помилка)")
    x +=h 
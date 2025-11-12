
def divisors(x, i):
    if i > x:
        return
    if x % i == 0:
        print(i)
    divisors(x, i+1)

x=int(input("Введіть число: "))
divisors(x, 1)
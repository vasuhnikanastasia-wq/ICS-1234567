import math
def area(*args):
    if len(args)== 3:
        a, b, c= args
        p=(a+b+c)/2
        return math.sqrt(p*(p-a)*(p-b)*(p-c))
    elif len(args)==2:
        a, b= args
        return a*b

def perimetr(*args):
    if len(args)==3:
        return args[0]+args[1]+args[2]
    elif len(args)==2:
        return 2*(args[0]+args[1])

from math import sin
a=float(input("введите число: "))
def fun(x):
    if 0.2<=x<=0.9:
        return (sin(x))
    else:
        return (1)
print(fun(a))

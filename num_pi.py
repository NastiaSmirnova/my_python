from math import pi
a=int(input("введите число: "))
def fun1(x):
    return f'{pi:.{x}f}'
print(fun1(a))

from math import sqrt
s=[2,4,9,16,25]
b=[sqrt(i) for i in s]
print(b)

a=[]
for i in s:
    a.append(sqrt(i))
print(a)


def f(x):
    return sqrt(x)
print(list(map(f,s)))

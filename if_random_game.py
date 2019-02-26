from random import randint
a=int(input("введите число "))
n=randint(1,4)
while a!=n:
    if a>=n:
        print('меньше')
    else:
        print ('больше')
    a=int(input("введите число "))
print("победа")

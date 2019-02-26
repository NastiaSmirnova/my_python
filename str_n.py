n=int(input("Введите число: "))
s=str(input("Введите строку: "))
def fun3(x,y):
    if len(x) > y:
        return (x.upper())
    else:
        return(x.lower())
print(fun3(s,n))

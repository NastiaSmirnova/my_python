f=float(input("Введите первое число: "))
s=float(input("Введите второе число: "))
o=input("Введите оператор: ")
def calc(x,y,z):
    try:
        if z=="+":
            return x+y
        elif z=="-":
            return x-y
        elif z=="*":
            return x*y
        elif z=="/":
            return x/y
    except ValueError:
        print("Неверный ввод!")
    except ZeroDivisionError:
        print("на 0 делить нельзя!")

print(calc(f,s,o))

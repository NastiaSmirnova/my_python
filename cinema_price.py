film=input('Введите фильм:')
data=input('Введите дату:')
time=input('Введите время:')
col=int(input('Введите количество:'))
if film=='Пятница':
    if data=='сегодня':
        if time=='12':
            if col>=20:
                print ('Стоимость:', 250*0.8*col)
            else:
                print('Стоимость-:', 250*col)
        elif time=='16':
            if col>=20:
                print ('Стоимость:', 350*0.8*col)
            else:
                print('Стоимость-', 350*col)
        elif time=='20':
            if col>=20:
                print ('Стоимость:', 450*0.8*col)
            else:
                print('Стоимость -', 450*col)
        else:
           print('Ошибка ввода') 
    elif data=='завтра':
        if time=='12':
            if col>=20:
                print ('Стоимость:', 250*0.8*0.95*col)
            else:
                print('Стоимость:', 250*0.95*col)
        elif time=='16':
            if col>=20:
                print ('Стоимость:', 350*0.8*0.95*col)
            else:
                print('Стоимость:', 350*0.95*col)
        elif time=='20':
            if col>=20:
                print ('Стоимость:', 450*0.8*0.95*col)
            else:
                print('Стоимость:', 450*0.95*col)
        else:
            print('Ошибка ввода')
    else:
        print('Ошибка ввода')
elif film=='Чемпионы':
    if data=='сегодня':
        if time=='10':
            if col>=20:
                print ('Стоимость:', 250*0.8*col)
            else:
                print('Стоимость -', 250*col)
        elif time=='13':
            if col>=20:
                print ('Стоимость:', 350*0.8*col)
            else:
                print('Стоимость-', 350*col)
        elif time=='16':
            if col>=20:
                print ('Стоимость:', 350*0.8*col)
            else:
                print('Стоимость -',  350*col)
        else:
            print('Ошибка ввода')              
    elif data=='завтра':
        if time=='10':
            if col>=20:
                print ('Стоимость:', 250*0.8*0.95*col)
            else:
                print('Стоимость:', 250*0.95*col)
        elif time=='13':
            if col>=20:
                print ('Стоимость:', 350*0.8*0.95*col)
            else:
                print('Стоимость:', 350*0.95*col)
        elif time=='16':
            if col>=20:
                print ('Стоимость:', 350*0.8*0.95*col)
            else:
                print('Стоимость:', 350*0.95*col)
        else:
            print('Ошибка ввода')             
    else:
        print('Ошибка ввода')

elif film=='Пернатая банда':
    if data=='сегодня':
        if time=='10':
            if col>=20:
                print ('Стоимость:', 350*0.8*col)
            else:
                print('Стоимость -', 350*col)
        elif time=='14':
            if col>=20:
                print ('Стоимость:', 450*0.8*col)
            else:
                print('Стоимость-', 450*col)
        elif time=='18':
            if col>=20:
                print ('Стоимость:', 450*0.8*col)
            else:
                print('Стоимость - ', 450*col)
        else:
            print('Ошибка ввода')
    elif data=='завтра':
        if time=='10':
            if col>=20:
                print ('Стоимость:', 350*0.8*0.95*col)
            else:
                print('Стоимость:', 350*0.95*col)
        elif time=='14':
            if col>=20:
                print ('Стоимость:', 450*0.8*0.95*col)
            else:
                print('Стоимость:', 450*0.95*col)
        elif time=='18':
            if col>=20:
                print ('Стоимость:', 450*0.8*0.95*col)
            else:
                print('Стоимость:', 450*0.95*col)
        else:
            print('Ошибка ввода')
    else:
        print('Ошибка ввода')
else:
    print('Ошибка ввода')

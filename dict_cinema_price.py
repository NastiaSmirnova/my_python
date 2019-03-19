
dict_cinema = {
    'Пятница': {'time_price': {12: 250, 16: 350, 20: 450}}, 
    'Чемпионы': {'time_price': {10: 250, 13: 350, 16: 350}}, 
    'Пернатая банда': {'time_price': {10: 350, 14: 450, 18: 450} }
    }
film=input('Введите фильм:')
data=input('Введите дату:')
time=int(input('Введите время:'))
col=int(input('Введите количество:'))

if data=='сегодня':
    if col>=20:
        print(dict_cinema[film]['time_price'][time]*col*0.80)
    else:
        print(dict_cinema[film]['time_price'][time]*col)
elif data=='завтра':
    if col>=20:
        print(dict_cinema[film]['time_price'][time]*col*0.80*0.95)
    else:
        print(dict_cinema[film]['time_price'][time]*col*0.95)
    

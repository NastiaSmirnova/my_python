

def reader(filename):
    '''
    Чтение содержимого json файла 
    '''
    import json    
    try:
        with open(filename) as f_obj:
            numbers = json.load(f_obj)
        return numbers
    except Exception as e:
        return e


  
def writer(filename, numbers):    
    import json    
    try:
        with open(filename, 'w') as f_obj:
            json.dump(numbers, f_obj)
    except Exception as e:
        print(e)


    
m=[]
k=10
while k!=3:
    print( 'Простой todo:')
    print('1.Добавить задачу')
    print('2.Вывести список задач')
    print('3.Выход')
    k=int(input('Укажите число: '))
    if k==1:
       f= input('Сформулируйте задачу: ')
       s= input('Добавьте категорию к задаче: ')
       t= input('Добавьте время к задаче: ')
       l=('Задача: '+ f+ ' Катеория: '+s+' Дата: '+ t)
       m.append(l)
      
    elif k==2:
        for i in range(len(m)):
            print(m[i])
if k==3:
    print('Задачи сохранены в файл!')
writer('10.json',m)


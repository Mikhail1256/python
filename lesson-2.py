
#   Задача 1

from asyncio import start_server
from itertools import product


print('')
print('Задача 1')
print('')

data = [1,1.2,'string',2.5,3.6,'asdsdfsdf',12]
print('data:')
print(data)
for i in range(len(data)):
    print(f'data элемент {i}: {data[i]}, type - {type(data[i])}')


#   Задача 2

print('')
print('Задача 2')
print('')

list.clear(data)
end = False
while end == False:
    print('Введите end, чтобы заканчивать вводить элементы. Введите новый элемент: ')
    element = input()
    if element == 'end':
        break
    data.append(element)
for i in range(len(data)):
    if i % 2 != 0:
        one_element = data[i]
        two_element = data[i-1]
        data[i] = two_element
        data[i-1] = one_element
print('data: ', data)



#   Задача 3

print('')
print('Задача 3')
print('')

list.clear(data)
data = ['Декабрь', 'Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь']
season = 3
season_name = ['Зима','Весна','Лето','Осень']
dict_data = {}
for i in range(len(data)):
    dict_data[i] = {data[i]:season_name[i//season]}
print('Введите число месяца: ',end='')
month = int(input())
if month == 12:
    month = 0
if month < 0 or month > 12:
    print('Неверное значение!')
else:
    print(dict_data[month])



#   Задача 4

print('')
print('Задача 4')
print('')

print('Введите строку: ',end = '')
string = input()
start_str = 0
end_str = 0
print(string)
for i in range(len(string)):
    if string[i] == " " or i+1 == len(string):
        if i+1 == len(string):
            end_str = i+1
        else:
            end_str = i
        if end_str-start_str > 10:
            end_str = start_str + 10
        print(string[start_str:end_str])
        start_str = i+1


#   Задача 5

print('')
print('Задача 5')
print('')

list.clear(data)
data = [10,9,8,7,7,6,8,1,2]
data.sort()
print('Рейтинг: ', data)
print('Введите новое значение: ',end='')
new_number = int(input())
data.append(new_number)
data.sort()
print('Новый рейтинг: ', data)



#   Задача 6

print('')
print('Задача 6')
print('')
    
dict = {'название': '', 'цена': '', 'количество': '', 'ед': ''}
products = []
analitics = {'название': [], 'цена': [], 'количество': [], 'ед': []}
end = False
while end == False:
    print('Введите end, чтобы закончить, либо нажмите Enter, чтобы продолжить')
    inp = input()
    if inp == 'end':
        break
    for i in dict.keys():
        print(f"Введите {i} товара: ",end=' ')
        dict[i] = input()
        analitics[i].append(dict[i])
    products.append(dict)
    
    print('')
    print('all products')
    for i in range(len(products)):
        print(f'({i},{products[i]})')

    print('')
    print('Analitics: ')
    for i in analitics.keys():
        print(f'{i} : {analitics[i]}')



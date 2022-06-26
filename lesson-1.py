inte = 10
fl = 1.2
string = 'name'

print(inte)
print(fl)
print(string)
print('')

print('Введите время в секундах: ', end='')
second = int(input())
hour = second // 3600
second -= hour * 3600
minute = second // 60
second -= minute * 60
print(hour,':',minute,':',second)
print('')

print('Введите число: ',end='')
number1 = int(input())
number2 = int(str(number1)+str(number1))
number3 = int(str(number2)+str(number1))
print(number1, ' + ', number2, ' + ', number3, ' = ', number1+number2+number3)
print('')

print('Введите доходы фирмы: ',end='')
revenue = float(input())
print('Введите расходы фирмы: ',end='')
expenses = float(input())
profit = float(revenue-expenses)
print('Прибыль: ', profit, end='. ')
if profit > 0:
    print("Поздравляем, доходы выше расходов!")
else:
    print('Походу надо что-то делать с этим!:)')
print('Теперь введите кол-во сотрудников в вашей фирме: ',end='')
employee = int(input())
if employee == 0:
    print('Круто! Меньше сотрудников - меньше налогов!')
elif employee > 0:
    print('Прибыль на одного сотрудника: ', profit/employee)
else:
    print("Удачи!")
print('')

print("Введите число a: ",end='')
a = int(input())
print("Введите число b: ",end='')
b = int(input())
day = 1
print(day, '-й день: ', a)
while a<b:
    day += 1
    a += a/10
    print(day, '-й день: ', a)
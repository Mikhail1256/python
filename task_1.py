

number1 = int(input(f'Введите 1 число: '))
number2 = int(input(f'Введите 2 число: '))
    

def multy(a,b):
    if b == 0:
        return 0
    return int(a)*int(b)

if number2 == 0:
    print('Неверное значение!')
else:
    print(f'Число: {multy(number1,number2)}')


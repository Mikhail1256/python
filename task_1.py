
file = open('hw_5/task_1.txt','w')


while True:
    print('Введите строку: ', end='')
    str = input()
    if len(str) == 0:
        break
    file.write(str + '\n')

file.close

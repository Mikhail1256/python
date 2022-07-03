
from posixpath import split
#определить символ окончания
end = 'k'
the_end = False
str_start = 0
str_end = 0
str_End = -1
number  = []
answer = 0
while the_end == False:
    str = input()
    number.clear()
    if str.find('k') != -1:
        the_end = True
        str = str[0:str.find('k')]
    number = str.split()
    for i in number:
        answer+=int(i)
    print(f'число: {answer}')



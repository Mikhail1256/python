import sys

data = [el for el in int(sys.argv)]

try:
    print(data[0]*data[1]+data[2])
except:
    print('Ошибка!')
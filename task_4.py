import codecs
file_load = codecs.open('hw_5/task_4_load.txt','r', "utf_8_sig")
file_save = codecs.open('hw_5/task_4_save.txt','w', "utf_8_sig")

data = file_load.readlines()
data = {el.split(' — ')[0]:int(el.split()[2]) for el in data}
data_rus = {'Один': 1, 'Два': 2, 'Три': 3, 'Четыре': 4}
data_new = {key_rus:value_rus for key_rus, value_rus in data_rus.items() for value_eng in data.values() if value_rus == value_eng}
str = ''
for keys,value in data_new.items():
    str += f'{keys} - {value} \n'
file_save.write(str)
import codecs
file_load = codecs.open('hw_5/task_7_load.txt','r', "utf_8_sig")
file_save = open('hw_5/task_7_save.txt','w')

data = file_load.readlines()
data = {el.split(' ', 1)[0]:[el.split()[1],el.split()[2],el.split()[3]] for el in data}
data_end = [{key:int(value[1])-int(value[2]) for key,value in data.items()}]
average_profit = 0
for el in data_end[0].values():
    average_profit+=el
data_end = [data_end[0],{'average_profit': average_profit}]
str = str(data_end)
file_save.write(str)
print(str)
print(data)
print(data_end)
print(average_profit)

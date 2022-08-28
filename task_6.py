import codecs
file = codecs.open('hw_5/task_6.txt','r', "utf_8_sig")
data = file.readlines()
data = [el.replace('\r','') for el in data]
data = [el.replace('\n','') for el in data]
data = [el.replace(' ','') for el in data]
data = [el.replace('(л)','+') for el in data]
data = [el.replace('(пр)','+') for el in data]
data = [el.replace('(лаб)','+') for el in data]
print(data)
data = {el.split(':')[0]:el.split(':')[1] for el in data}
for key,value in data.items():
    value = value.split('+')
    new_val = 0
    for el in value:
        try:
            new_val+=int(el)
        except:
            break
    data.update({key:new_val})
print(data)
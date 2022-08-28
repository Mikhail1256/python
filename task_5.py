
str = '12 10 15'
file = open('hw_5/task_5.txt','w')
file.write(str)
file.close()
file = open('hw_5/task_5.txt','r')
data = file.read()
data = [el for el in data.split()]
sum = 0
for el in data:
    sum+=int(el)
print(sum)

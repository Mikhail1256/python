from itertools import count, cycle


for i in count(3,1):
    print(i)
    if i >= 10:
        break

data = list(range(10))

for a,b in enumerate(cycle(data)):
    print(b, end = ' ')
    if a > 30:
        break
    

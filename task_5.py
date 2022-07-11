from functools import reduce


data = reduce(lambda a,b: a+b, range(100,1001))

print(data)
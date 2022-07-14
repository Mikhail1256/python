
file = open('hw_5/task_2.txt','r')

data = file.readlines()
print(f'Строк: {len(data)}')
data = [el.replace('\n',' ') for el in data]
# words = [el for el in data]
# можно ли сгенерировать строку таким способом?
words = ''
for el in data:
    words += el
print(f'Слов: ', len(words.split(' ')))


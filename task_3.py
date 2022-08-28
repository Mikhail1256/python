import codecs
file = codecs.open('hw_5/task_3.txt','r', "utf_8_sig")

data = file.readlines()
data = {el.split()[0]:float(el.split()[2]) for el in data}
wages_min = [key for key, el in data.items() if el < 20000.0]
print(f'Сотрудники с окладом меньше 20к: {wages_min}')
average_income = float(0)
for key, el in data.items():
    average_income += el
average_income /= len(data)
print(f'Средний оклад сотрудников: {average_income}')
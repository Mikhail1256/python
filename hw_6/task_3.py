
cash = {"wage": None, "bonus": None}

class Worker():
    _income = cash
    def __init__(self, name,surname,position,wage,bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname
    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

Gregor = Position('Грегор','Белинский','Мидл',100000,100000)
print(f'Имя: {Gregor.get_full_name()}\nДоход: {Gregor.get_total_income()}')
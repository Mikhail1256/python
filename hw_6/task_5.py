from turtle import title


class Stationery ():
    def __init__(self,title):
        self.title = title
    def draw(self):
        return 'Запуск отрисовки'

class Pen (Stationery):
    def draw(self):
        print(f'{self.title} {super().draw()}')

class Pencil (Stationery):
    def draw(self):
        print(f'{self.title} {super().draw()}')

class Handle (Stationery):
    def draw(self):
        print(f'{self.title} {super().draw()}')

stationery = [Pen('Ручка'),Pencil('Карандаш'),Handle('Маркер')]
for el in stationery:
    el.draw()
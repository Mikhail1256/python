from mimetypes import init


class Cell:
    def __init__(self,cells):
        self.cells = cells
    def __add__(self,other):
        self.cells += other.cells
        del other
        return self.cells
    def __sub__(self,other):
        if self.cells - other.cells < 0:
            return print('Невозможно выпонить действие, разность меньше 0')
        self.cells -= other.cells
        del other
        return self.cells
    def __mul__(self,other):
        self.cells *= other.cells
        del other
        return self.cells
    def __truediv__(self,other):
        self.cells = self.cells // other.cells
        del other
        return self.cells
    def make_order(self,quantity):
        str = ''
        d = self.cells//quantity
        s = self.cells%quantity
        for i in range(d):
            for text in range(quantity):
                str+='*'
            str+='\n'
        if s > 0:
            for i in range(s):
                str+='*'
        return str

cell1 = Cell(5)
cell2 = Cell(8)
print(cell1.make_order(4))
print('\n')
print(cell2.make_order(3))
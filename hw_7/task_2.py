class Сlothes:
    def __init__(self,name,size,height):
        self.name = name
        self.size = size
        self.height = height
    
    @property
    def cost(self):
        return f'Материалов для изготовления {self.name}: '
    

class Coat(Сlothes):
    
    @property
    def cost(self):
        return f'{super().cost} {self.size / 6.5 + 0.5}'

class Suit(Сlothes):
    
    @property
    def cost(self):
        return f'{super().cost} {2*self.height + 0.3}'

coat = Coat('Пальто',200,200)
suit = Suit('Костюм',500,500)
print(coat.cost)
print(suit.cost)
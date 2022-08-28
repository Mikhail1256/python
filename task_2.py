
class Road():
    __length = 0
    __width = 0
    def __init__(self,length,width):
        self.__length = length
        self.__width = width
        self.weight = self.__length * self.__width * 25 * 5 / 1000
        print(f'Масса осфальта {self.weight} т')

road = Road(20,5000)

import random
import threading

class Car():
    speed = 0
    timer = None
    def __init__(self, max_speed, color, name, is_police):
        self.max_speed = max_speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.movement()

    def movement(self):
        self.timer = threading.Timer(3, self.movement)
        self.timer.start()
        if self.speed <= 0:
            self.go()
        if self.speed > self.max_speed:
            self.braking()
        rand = random.randint(0,3)
        if rand == 0:
            self.turn(random.choice(['налево','направо']))
        if rand == 1:
            self.boost()
        if rand == 2:
            self.braking()

    def go(self):
        print(f'{self.name} поехала')
        self.boost()

    def stop(self):
        while self.speed > 0:
            self.braking()
        self.speed = 0
        print(f'{self.name} остановилась')
    
    def turn(self,direction):
        print(f'{self.name} повернула {direction}')

    def boost(self):
        self.speed += random.randint(1,10)
        self.show_speed()
        if self.speed > self.max_speed:
            self.braking()
    
    def braking(self):
        self.speed -= random.randint(1,10)
        if self.speed < 0:
            self.stop()
        else:
            self.show_speed()
    
    def show_speed(self):
        print(f'{self.name} текущая скорость {self.speed} KM/Ч')
        if self.speed <= 0:
            self.braking
            self.go

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превышение скорости: {self.speed} KM/Ч')
        else:
            return super().show_speed()

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превышение скорости: {self.speed} KM/Ч')
        else:
            return super().show_speed()

class PoliceCar(Car):
    pass

cars = [WorkCar(80,'Красный','Грузовик',False),SportCar(200,'Красный','Феррари',False),PoliceCar(150,'Красный','Полиция',True),TownCar(100,'Красный','ВАЗ',False)]

#Если однин метод выводится одновременно, то соединяются в строке без \n
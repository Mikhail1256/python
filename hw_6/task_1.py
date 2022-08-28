import time

class TrafficLight:
    _color = ['Красный','Желтый','Зеленый']
    timer = [7.0,3.0,8.0]
    status = -1

    def running(self):
        if self.status == -1 or self.status >= 2:
            self.status = 0
        else:
            self.status += 1
        print(f'Загорелся {self._color[self.status]} цвет')
        time.sleep(self.timer[self.status])
        self.running()



new = TrafficLight()
new.running()


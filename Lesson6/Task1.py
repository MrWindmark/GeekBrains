import time

class TrafficLight:
    _color = "Red"
    def running(self):
        if TrafficLight._color == 'Red':
            print(f'Work in mode {TrafficLight._color} - 7 sec')
            time.sleep(7)
            TrafficLight._color = 'Yellow'
            TrafficLight.running(self)
        elif TrafficLight._color == 'Yellow':
            print(f'Work in mode {TrafficLight._color} - 2 sec')
            time.sleep(2)
            TrafficLight._color = 'Green'
            TrafficLight.running(self)
        elif TrafficLight._color == 'Green':
            print(f'Work in mode {TrafficLight._color} - 10 sec')
            time.sleep(10)
            TrafficLight._color = 'Red'

test = TrafficLight()
test.running()
class Road:
    def __init__(self, length: int, width: int):
        Road._length = length
        Road._width = width

    def road_calc(self, mass, depth):
        Road.__m_sqwr_mass = mass
        Road.__depth_in_sm = depth
        result = (Road._length * Road._width * Road.__m_sqwr_mass * Road.__depth_in_sm) / 1000
        print(f'Road mass: {result} T')


test = Road(5000, 15)
test.road_calc(25, 10)
test2 = Road(10000, 15)
test2.road_calc(25, 10)

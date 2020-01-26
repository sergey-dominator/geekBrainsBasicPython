class Road:
    default_weight_of_one_km = 25
    default_height = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def evaluate_weight_ton(self):
        return self._length * self._width * Road.default_weight_of_one_km * Road.default_height / 1000


new_road = Road(20, 5000)
print(new_road.evaluate_weight_ton())

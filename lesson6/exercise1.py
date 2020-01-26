from enum import Enum
import time


class Color(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3


class TrafficLight:
    colors = [Color.RED, Color.YELLOW, Color.GREEN]
    delays = {
        Color.RED: 7,
        Color.YELLOW: 2,
        Color.GREEN: 5
    }

    def __init__(self):
        self.__current_color_index = 0
        # positive - we go from first color to the last, negative - we go in opposite direction
        self.__direction = -1

    def running(self):
        while True:
            if self.__direction > 0:
                if self.__current_color_index < len(TrafficLight.colors) - 1:
                    self.__current_color_index += 1
                else:
                    self.__current_color_index -= 1
                    self.__direction *= -1
            else:
                if self.__current_color_index > 0:
                    self.__current_color_index -= 1
                else:
                    self.__current_color_index += 1
                    self.__direction *= -1

            current_color = TrafficLight.colors[self.__current_color_index]
            print(current_color)
            time.sleep(TrafficLight.delays.get(current_color))


city_traffic_light = TrafficLight()
city_traffic_light.running()





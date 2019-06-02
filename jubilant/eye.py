from adafruit_hcsr04 import HCSR04


class Eye:
    def __init__(self, trigger_pin, receive_pin, name='unknown'):
        self.__sonar = HCSR04(trigger_pin, receive_pin, timeout=2)
        self.__last_distance = 0
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def distance(self):
        self.__last_distance = self.__sonar.distance
        return self.__last_distance

    @property
    def last_distance(self):
        return self.__last_distance
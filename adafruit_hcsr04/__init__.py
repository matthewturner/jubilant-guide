class HCSR04:
    def __init__(self, pin_in, pin_out, timeout):
        self.__distance = 10.3

    @property
    def distance(self):
        return self.__distance

    def set_distance(self, distance):
        self.__distance = distance
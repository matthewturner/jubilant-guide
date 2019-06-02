from digitalio import DigitalInOut

class HCSR04:
    def __init__(self, pin_in, pin_out, timeout):
        self.__distance = 25
        self.__pin_in = DigitalInOut(pin_in)
        self.__pin_out = DigitalInOut(pin_out)

    @property
    def distance(self):
        self.__pin_in.value = True
        self.__pin_out.value = True
        self.__pin_in.value = False
        self.__pin_out.value = False
        return self.__distance

    def set_distance(self, distance):
        self.__distance = distance
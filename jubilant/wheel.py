import board
from digitalio import DigitalInOut, Direction, Pull

class Wheel:
    def __init__(self, forward_pin, reverse_pin):
        self.__forward_pin = DigitalInOut(forward_pin)
        self.__forward_pin.direction = Direction.OUTPUT

        self.__reverse_pin = DigitalInOut(reverse_pin)
        self.__reverse_pin.direction = Direction.OUTPUT

    def forward(self):
        self.__forward_pin.value = True
        self.__reverse_pin.value = False

    def reverse(self):
        self.__forward_pin.value = False
        self.__reverse_pin.value = True

    def stop(self):
        self.__forward_pin.value = False
        self.__reverse_pin.value = False
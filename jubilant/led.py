import board
from digitalio import DigitalInOut, Direction, Pull

class Led:
    def __init__(self):
        self.__pin = DigitalInOut(board.D13)
        self.__pin.direction = Direction.OUTPUT


    def on(self):
        self.__pin.value = True


    def off(self):
        self.__pin.value = False

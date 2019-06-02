import board
import time
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogOut
from jubilant import queue, Wheel

class WheelDriver:
    STOPPED = 0
    FORWARD = 1
    TURNING_RIGHT = 2
    TURNING_LEFT = 3
    REVERSING = 4

    def __init__(self):
        self.__status = WheelDriver.STOPPED
        self.__right_wheel = Wheel(board.D2, board.D3)
        self.__left_wheel = Wheel(board.D4, board.D5)

        self.__speed = AnalogOut(board.A0)
        self.__speed.value = 55000

    @property
    def status(self):
        return self.__status


    def is_turning(self):
        return self.status == TURNING_LEFT or self.status == TURNING_RIGHT

    @status.setter
    def status(self, status):
        self.__status = status


    def turn(self, right, degrees):
        desired = WheelDriver.TURNING_RIGHT if right else WheelDriver.TURNING_LEFT
        if self.status == desired:
            return
        self.status = desired
        message = 'Turning right...' if right else 'Turning left...'
        print(message)
        if right:
            self.__right_wheel.forward()
            self.__left_wheel.reverse()
        else:
            self.__right_wheel.reverse()
            self.__left_wheel.forward()

        time_to_turn = 360 / degrees / 8
        queue.enqueue(self.stop, time_to_turn)


    def turn_right(self, degrees):
        self.turn(True, degrees)


    def turn_left(self, degrees):
        turn(False, degrees)


    def forward(self):
        if self.status == WheelDriver.FORWARD:
            return
        self.status = WheelDriver.FORWARD
        print('Moving forward...')
        self.__right_wheel.forward()
        self.__left_wheel.forward()


    def reverse(self):
        if self.status == WheelDriver.REVERSING:
            return
        self.status = WheelDriver.REVERSING
        print('Reversing...')
        self.__right_wheel.reverse()
        self.__left_wheel.reverse()


    def stop(self):
        if self.status == WheelDriver.STOPPED:
            return
        self.status = WheelDriver.STOPPED
        print('Stopping...')
        self.__right_wheel.stop()
        self.__left_wheel.stop()

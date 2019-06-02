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
    BEARING_RIGHT = 4
    BEARING_LEFT = 5
    REVERSING = 6

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
        return self.status == WheelDriver.TURNING_LEFT \
            or self.status == WheelDriver.TURNING_RIGHT \
            or self.status == WheelDriver.BEARING_RIGHT \
            or self.status == WheelDriver.BEARING_LEFT

    @status.setter
    def status(self, status):
        self.__status = status

    def __time_to_turn(self, degrees):
        return (360 / degrees / 8)

    def turn_right(self, degrees):
        if self.status == WheelDriver.TURNING_RIGHT:
            return
        self.status = WheelDriver.TURNING_RIGHT
        message = 'Turning right...'
        print(message)
        self.__right_wheel.forward()
        self.__left_wheel.reverse()
        queue.enqueue(self.stop, self.__time_to_turn(degrees))

    def turn_left(self, degrees):
        if self.status == WheelDriver.TURNING_LEFT:
            return
        self.status = WheelDriver.TURNING_LEFT
        message = 'Turning left...'
        print(message)
        self.__right_wheel.reverse()
        self.__left_wheel.forward()
        queue.enqueue(self.stop, self.__time_to_turn(degrees))

    def bear_right(self):
        if self.status == WheelDriver.BEARING_RIGHT:
            return
        self.status = WheelDriver.BEARING_RIGHT
        print('Bearing right...')
        self.__right_wheel.forward()
        self.__left_wheel.stop()
        queue.enqueue(self.forward, 0.1)

    def bear_left(self):
        if self.status == WheelDriver.BEARING_LEFT:
            return
        self.status = WheelDriver.BEARING_LEFT
        print('Bearing left...')
        self.__right_wheel.stop()
        self.__left_wheel.forward()
        queue.enqueue(self.forward, 0.1)

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

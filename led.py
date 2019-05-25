import board
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT


def on():
    led.value = True


def off():
    led.value = False

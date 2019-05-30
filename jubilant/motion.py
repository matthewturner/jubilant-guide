import board
import time
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogOut
from jubilant.queue import queue

STOPPED = 0
FORWARD = 1
TURNING_RIGHT = 2
TURNING_LEFT = 3
REVERSING = 4

__status = STOPPED


def status():
    global __status
    return __status


def is_turning():
    return status() == TURNING_LEFT or status() == TURNING_RIGHT


def set_status(status):
    global __status
    __status = status


motor_right_forward = DigitalInOut(board.D2)
motor_right_forward.direction = Direction.OUTPUT

motor_right_reverse = DigitalInOut(board.D3)
motor_right_reverse.direction = Direction.OUTPUT

motor_left_forward = DigitalInOut(board.D4)
motor_left_forward.direction = Direction.OUTPUT

motor_left_reverse = DigitalInOut(board.D5)
motor_left_reverse.direction = Direction.OUTPUT

speed = AnalogOut(board.A0)
speed.value = 55000


def turn(right, degrees):
    desired = TURNING_RIGHT if right else TURNING_LEFT
    if status() == desired:
        return
    set_status(desired)
    message = 'Turning right...' if right else 'Turning left...'
    print(message)
    motor_right_forward.value = right
    motor_right_reverse.value = not right

    motor_left_forward.value = not right
    motor_left_reverse.value = right
    time_to_turn = 360 / degrees / 8
    queue.enqueue(stop, time_to_turn)


def turn_right(degrees):
    turn(True, degrees)


def turn_left(degrees):
    turn(False, degrees)


def forward():
    if status() == FORWARD:
        return
    set_status(FORWARD)
    print('Moving forward...')
    motor_right_forward.value = True
    motor_right_reverse.value = False

    motor_left_forward.value = True
    motor_left_reverse.value = False


def reverse():
    if status() == REVERSING:
        return
    set_status(REVERSING)
    print('Reversing...')
    motor_right_forward.value = False
    motor_right_reverse.value = True

    motor_left_forward.value = False
    motor_left_reverse.value = True


def stop():
    if status() == STOPPED:
        return
    set_status(STOPPED)
    print('Stopping...')
    motor_right_forward.value = False
    motor_right_reverse.value = False

    motor_left_forward.value = False
    motor_left_reverse.value = False


def test():
    forward()
    time.sleep(1)
    reverse()
    time.sleep(1)
    turn_right()
    time.sleep(1)
    turn_left()
    time.sleep(1)
    stop()

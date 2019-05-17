import board
import time
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogOut

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
  motor_right_forward.value = right
  motor_right_reverse.value = not right

  motor_left_forward.value = not right
  motor_left_reverse.value = right
  time_to_turn = 360 / degrees / 4
  time.sleep(time_to_turn)
  stop()

def turn_right(degrees):
  turn(True, degrees)

def turn_left(degrees):
  turn(False, degrees)

def forward():
  motor_right_forward.value = True
  motor_right_reverse.value = False

  motor_left_forward.value = True
  motor_left_reverse.value = False

def reverse():
  motor_right_forward.value = False
  motor_right_reverse.value = True

  motor_left_forward.value = False
  motor_left_reverse.value = True

def stop():
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

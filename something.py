import board
import time
from adafruit_hcsr04 import HCSR04
sonar = HCSR04(board.D9, board.D8, timeout=5)

last_distance = 0

def is_infront():
  global last_distance
  try:
    current_distance = int(sonar.distance)
    if current_distance != last_distance:
      last_distance = current_distance
      print("Distance: % 3d" %(current_distance))
    return current_distance <= 6
  except RuntimeError:
    print("Retrying!")
    pass
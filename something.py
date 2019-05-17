import board
import time
from adafruit_hcsr04 import HCSR04
sonar = HCSR04(board.D9, board.D8, timeout=5)

def is_infront():
  try:
    print(sonar.distance)
    return sonar.distance <= 11
  except RuntimeError:
    print("Retrying!")
    pass

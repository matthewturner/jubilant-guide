import neopixel
import board

dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2)

NUMPIXELS = 16
neopixels = neopixel.NeoPixel(board.D6, NUMPIXELS, brightness=0.2, auto_write=False)

def next(i):
  # spin internal LED around! autoshow is on
  dot[0] = color(i & 255)

  # also make the neopixels swirl around
  for p in range(NUMPIXELS):
    idx = int ((p * 256 / NUMPIXELS) + i)
    neopixels[p] = color(idx & 255)
  neopixels.show()

# Helper to give us a nice color swirl
def color(pos):
  # Input a value 0 to 255 to get a color value.
  # The colours are a transition r - g - b - back to r.
  if (pos < 0):
    return [0, 0, 0]
  if (pos > 255):
    return [0, 0, 0]
  if (pos < 85):
    return [int(pos * 3), int(255 - (pos*3)), 0]
  elif (pos < 170):
    pos -= 85
    return [int(255 - pos*3), 0, int(pos*3)]
  else:
    pos -= 170
    return [0, int(pos*3), int(255 - pos*3)]

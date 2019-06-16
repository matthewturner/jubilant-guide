import neopixel
import board
from .queueable import Queueable as async


class Swirl:
    NUMPIXELS = 16

    def __init__(self):
        self.__i = 0
        self.__dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2)

        self.__neopixels = neopixel.NeoPixel(
            board.D6, Swirl.NUMPIXELS, brightness=0.2, auto_write=False)

    def next(self):
        self.__dot[0] = self.__color(self.__i & 255)

        for p in range(Swirl.NUMPIXELS):
            idx = int((p * 256 / Swirl.NUMPIXELS) + self.__i)
            self.__neopixels[p] = self.__color(idx & 255)
        self.__neopixels.show()
        self.__i = (self.__i + 1) % 256

    @async(repeat=True)
    def next_async(self):
        self.next()

    def __color(self, pos):
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

def NeoPixel(pin, numPixels, brightness=0, auto_write=False):
    return Pixel(numPixels)


class Pixel(list):
    def __init__(self, numPixels):
        for _ in range(numPixels):
            self.append(0)

    def show(self):
        pass

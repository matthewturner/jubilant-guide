from jubilant import Swirl, Led, Vision, \
    queue, WheelDriver, CollisionWarning, \
    Body
from jubilant import Queueable as async


class Robot:
    def __init__(self):
        self.__motion = WheelDriver()
        self.__led = Led()
        self.__vision = Vision()
        self.__swirl = Swirl()
        self.__body = Body()
        self.__motion.listener = self.__body

    @property
    def motion(self):
        return self.__motion

    @property
    def vision(self):
        return self.__vision

    @property
    def body(self):
        return self.__body

    def update(self):
        self.__body.update(self.__motion)

    @async(delay=0.01, repeat=True)
    def __move_async(self):
        something = self.__vision
        motion = self.__motion
        led = self.__led

        try:
            if not motion.is_manoevring():
                if something.is_straight_infront():
                    led.off()
                    motion.forward()
                else:
                    led.off()
                    if something.is_closer_to_left():
                        motion.bear_right()
                    else:
                        motion.bear_left()
        except CollisionWarning:
            led.on()
            if something.is_closer_to_right():
                motion.turn_left(90)
            else:
                motion.turn_right(90)

    def start(self):
        self.__move_async()
        self.__swirl.next_async()

from jubilant import Swirl, Led, Vision, queue, WheelDriver, CollisionWarning


class Robot:
    def __init__(self):
        self.__motion = WheelDriver()
        self.__led = Led()
        self.__something = Vision()
        self.__swirl = Swirl()

    def __check_in_front(self):
        try:
            if not self.__motion.is_turning():
                if self.__something.is_straight_infront():
                    self.__led.off()
                    self.__motion.forward()
                else:
                    self.__led.off()
                    if self.__something.is_closer_to_left():
                        self.__motion.bear_right()
                    else:
                        self.__motion.bear_left()
        except CollisionWarning:
            self.__led.on()
            if self.__something.is_closer_to_left():
                self.__motion.turn_right(90)
            else:
                self.__motion.turn_left(90)

    def start(self):
        queue.enqueue(self.__check_in_front, delay=0.01, repeat=True)
        queue.enqueue(self.__swirl.next, repeat=True)

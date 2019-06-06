from jubilant import WheelDriver
import time


class Body:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__speed = 0
        self.__heading = 0
        self.__last_status = WheelDriver.STOPPED
        self.__last_status_changed = time.monotonic()
        self.__time_scale = 1

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y


    def coordinate(self, translation_vector=[0, 0]):
        return [self.x + translation_vector[0], self.y + translation_vector[0]]

    @property
    def time_scale(self):
        return self.__time_scale

    @time_scale.setter
    def time_scale(self, time_scale):
        self.__time_scale = time_scale

    @property
    def speed(self):
        return self.__speed

    @property
    def heading(self):
        return self.__heading

    def on_status_changed(self, args):
        last_status = self.__last_status
        last_status_changed = self.__last_status_changed

        current_status = args
        current_time = time.monotonic()

        self.__last_status = current_status
        self.__last_status_changed = current_time

        if current_status == WheelDriver.FORWARD:
            self.__speed = 5

        if current_status == WheelDriver.REVERSING:
            self.__speed = 5

        if last_status == WheelDriver.STOPPED:
            return
        
        duration = current_time - last_status_changed

        if last_status == WheelDriver.FORWARD:
            self.__y = self.__y + (duration / 1000 * self.__time_scale * self.__speed)
            return

        if last_status == WheelDriver.REVERSING:
            self.__y = self.__y - (duration / 1000 * self.__time_scale * self.__speed)
            return
    
    def update(self, wheel_driver):
        duration = time.monotonic() - self.__last_status_changed

        if wheel_driver.status == WheelDriver.FORWARD:
            self.__y = self.__y + (duration / 1000 * self.__time_scale * self.__speed)
            return
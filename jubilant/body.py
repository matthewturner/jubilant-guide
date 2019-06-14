from jubilant import WheelDriver, Point
import time


class Body:
    def __init__(self):
        self.__point = Point(0, 0)
        self.__speed = 0
        self.__heading = 0
        self.__last_status = WheelDriver.STOPPED
        self.__last_status_changed = time.monotonic()
        self.__time_scale = 1
        self.__turn_speed = 0

    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, point):
        self.__point = point

    def move(self, by):
        self.__point = point.translate(by)

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

    @heading.setter
    def heading(self, heading):
        self.__heading = heading

    def on_status_changed(self, args):
        last_status = self.__last_status
        last_status_changed = self.__last_status_changed

        current_status = args
        current_time = time.monotonic()

        self.__last_status = current_status
        self.__last_status_changed = current_time

        if current_status == WheelDriver.STOPPED:
            self.__speed = 0
            self.__turn_speed = 0

        if current_status == WheelDriver.FORWARD:
            self.__speed = 5

        if current_status == WheelDriver.REVERSING:
            self.__speed = 5

        if current_status == WheelDriver.TURNING_LEFT:
            self.__speed = 0
            self.__turn_speed = -0.49
        
        if current_status == WheelDriver.TURNING_RIGHT:
            self.__speed = 0
            self.__turn_speed = 0.49
        
        duration = current_time - last_status_changed
    
    def update(self, wheel_driver):
        duration = time.monotonic() - self.__last_status_changed

        if wheel_driver.status == WheelDriver.FORWARD:
            distance_travelled = duration / 1000 * self.__time_scale * self.__speed
            self.__point = self.__point.move(self.__heading, distance_travelled)
            return
        
        if wheel_driver.status == WheelDriver.TURNING_LEFT or wheel_driver.status == WheelDriver.TURNING_RIGHT:
            self.__heading = (self.__heading + (duration * self.__turn_speed)) % 360
            print('New heading: % 2d' % self.__heading)
            return
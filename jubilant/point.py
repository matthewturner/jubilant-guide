import math


class Point:
    '''Creates a point on a coordinate plane with values x and y.'''

    def __init__(self, x, y):
        '''Defines x and y variables'''
        self.__x = x
        self.__y = y

    def translate(self, by):
        '''Determines where x and y move'''
        x = self.__x + by.x
        y = self.__y + by.y
        return Point(x, y)
    
    def move(self, angle, distance):
        deltax = distance * math.sin(math.radians(angle))
        deltay = distance * math.cos(math.radians(angle))

        return Point(self.__x + deltax, self.__y + deltay)

    def __str__(self):
        return "Point(%s,%s)"%(self.X, self.Y) 

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def distance_from(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.hypot(dx, dy)

    def scale(self, by):
        return Point(self.__x * by, self.__y * by)

    def array(self):
        return [self.__x, self.__y]
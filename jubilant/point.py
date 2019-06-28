import math
import numpy as np


class Point:
    '''Creates a point on a coordinate plane with values x and y.'''

    def __init__(self, x, y):
        '''Defines x and y variables'''
        self.__x = x
        self.__y = y

    def translate(self, by):
        '''Determines where x and y move'''
        return self + by

    def __add__(self, other):
        x = self.__x + other.__x
        y = self.__y + other.__y
        return Point(x, y)

    def __sub__(self, other):
        x = self.__x - other.__x
        y = self.__y - other.__y
        return Point(x, y)

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y

    def move(self, angle, distance):
        deltax = distance * math.sin(math.radians(angle))
        deltay = distance * math.cos(math.radians(angle))

        return self + Point(deltax, deltay)

    def __repr__(self):
        return "Point(%s, %s)" % (self.__x, self.__y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def distance_from(self, other):
        d = self - other
        return math.hypot(d.__x, d.__y)

    def scale(self, by):
        return Point(self.__x * by, self.__y * by)

    def array(self):
        return [self.__x, self.__y]

    def bearing(self, to):
        north = self + Point(0, 1)
        return self.angle(north, to)

    def angle(self, p0, p2):
        p1 = self
        ''' compute angle (in degrees) for p0p1p2 corner
        Inputs:
            p0,p1,p2 - points in the form of [x,y]
        '''
        v0 = np.array(p0.array()) - np.array(p1.array())
        v1 = np.array(p2.array()) - np.array(p1.array())

        angle = np.math.atan2(np.linalg.det([v0, v1]), np.dot(v0, v1))
        angle = round(np.degrees(angle), 2)
        if angle < 0:
            angle = angle + 360
        angle = angle % 180
        return angle

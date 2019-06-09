from jubilant import Point
import numpy as np
import math


class ObstacleIdentifier:
    def __init__(self, map):
        self.__map = map

    def obstacle(self, robot):
        for square in self.__map.interesting_squares():
            if self.is_obstacle(square, robot):
                return square
        return None

    def is_obstacle(self, square, robot):
        north = robot.body.point.translate(Point(0, 1))
        for line in square.lines(self.__map.square_size, robot.body.point):
            start_point = line[0]
            end_point = line[1]
            start_angle = self.__angle(north, robot.body.point, start_point)
            end_angle = self.__angle(north, robot.body.point, end_point)
            if (start_angle <= robot.body.heading <= end_angle) or (start_angle >= robot.body.heading >= end_angle):
                return True
        return False

    def __angle(self, p0, p1, p2):
        ''' compute angle (in degrees) for p0p1p2 corner
        Inputs:
            p0,p1,p2 - points in the form of [x,y]
        '''
        v0 = np.array(p0.array()) - np.array(p1.array())
        v1 = np.array(p2.array()) - np.array(p1.array())

        angle = np.math.atan2(np.linalg.det([v0, v1]), np.dot(v0, v1))
        return np.degrees(angle)
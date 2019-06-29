from jubilant import Point
import numpy as np
import math


class ObstacleIdentifier:
    def __init__(self, map):
        self.__map = map

    def obstacle(self, robot):
        for square in self.__map.interesting_squares:
            if self.is_obstacle(square, robot):
                return square
        return None

    def is_obstacle(self, square, robot):
        north = robot.body.point.translate(Point(0, self.__map.square_size))
        for line in square.lines(self.__map.square_size, robot.body.point):
            start_point, end_point = line
            start_angle = robot.body.point.angle(north, start_point, bearing=True)
            end_angle = robot.body.point.angle(north, end_point, bearing=True)
            if (start_angle <= robot.body.heading <= end_angle) or (start_angle >= robot.body.heading >= end_angle):
                return True
        return False
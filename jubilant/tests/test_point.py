from jubilant.point import Point
import pytest


class TestPoint:
    def test_add(self):
        actual = Point(9, 11) + Point(5, 4)
        assert(actual.x == 14)
        assert(actual.y == 15)

    def test_equal(self):
        actual = Point(9, 11)
        other = Point(9, 11)
        assert(actual == other)

    def test_subtract(self):
        actual = Point(9, 11) - Point(5, 4)
        assert(actual.x == 4)
        assert(actual.y == 7)

    def test_move(self):
        actual = Point(9, 11).move(90, 25)
        assert(actual.x == 34)
        assert(round(actual.y, 2) == 11)
    
    def test_array(self):
        actual = Point(9, 11).array()
        assert(actual[0] == 9)
        assert(actual[1] == 11)
        assert(len(actual) == 2)

    def test_scale(self):
        actual = Point(9, 11).scale(10)
        assert(actual.x == 90)
        assert(actual.y == 110)
    
    def test_distance_from(self):
        actual = Point(9, 11).distance_from(Point(10, 12))
        assert(round(actual, 2) == 1.41)

    def test_angle_between_three_points(self):
        actual = Point(10, 0).angle(Point(5, 5), Point(15, 5))
        assert(round(actual, 2) == 90)

    def test_bearing(self):
        actual = Point(10, 0).bearing(Point(5, 5))
        assert(round(actual, 2) == 45)
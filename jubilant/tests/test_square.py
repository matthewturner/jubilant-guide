from jubilant.square import Square
from jubilant.point import Point
import pytest


class TestSquare:  
    def test_points(self):
        target = Square(Point(1, 1))

        actual = target.points()

        assert(actual[0] == Point(1, 1))
        assert(actual[1] == Point(2, 1))
        assert(actual[2] == Point(2, 2))
        assert(actual[3] == Point(1, 2))
    
    def test_lines(self):
        target = Square(Point(1, 1))

        actual = target.lines()

        assert(actual[0] == (Point(1, 1), Point(2, 1)))
        assert(actual[1] == (Point(2, 1), Point(2, 2)))
        assert(actual[2] == (Point(2, 2), Point(1, 2)))
        assert(actual[3] == (Point(1, 2), Point(1, 1)))

    def test_lines_closest_to_north(self):
        target = Square(Point(1, 1))
        actual = target.lines(scale=10, point=Point(15, 5))
        assert(actual == ((Point(10, 10), Point(20, 10)),))
    
    def test_center(self):
        target = Square(Point(1, 1))
        actual = target.center(scale=10)
        assert(actual == Point(15, 15))
    
    def test_center_with_large_origin(self):
        target = Square(Point(12, 12))
        actual = target.center(scale=10)
        assert(actual == Point(125, 125))

    def test_next_type_after_open(self):
        target = Square(Point(12, 12))
        actual = target.next_type()
        assert(actual == Square.SOLID)
    
    def test_next_type_after_solid(self):
        target = Square(Point(12, 12), type=Square.SOLID)
        actual = target.next_type()
        assert(actual == Square.TRANSPARENT)
    
    def test_next_type_after_transparent(self):
        target = Square(Point(12, 12), type=Square.TRANSPARENT)
        actual = target.next_type()
        assert(actual == Square.OPEN)
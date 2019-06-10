from world import ObstacleIdentifier
from jubilant import Map, Square, Point, Robot
import pytest


class TestObstacleIdentifier:
    @pytest.fixture
    def map(self):
        return Map('x', 10)

    @pytest.fixture
    def robot(self):
        robot = Robot()
        robot.body.point = Point(40, 40)
        robot.body.heading = 0
        return robot

    def square(self, x, y):
        return Square(Point(x, y), type=Square.SOLID)

    def test_due_north(self, map, robot):
        map.append(self.square(4, 6))
        target = ObstacleIdentifier(map)
        assert(target.obstacle(robot))

    def test_north_east(self, map, robot):
        map.append(self.square(2.5, 5))
        target = ObstacleIdentifier(map)
        assert(not target.obstacle(robot))

    def test_due_south(self, map, robot):
        map.append(self.square(4, 2))
        target = ObstacleIdentifier(map)
        assert(not target.obstacle(robot))
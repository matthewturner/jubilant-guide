from world import ObstacleIdentifier
from jubilant import Map, Square, Point, Robot


class TestObstacleIdentifier:
    def test_due_north(self):
        robot = Robot()
        robot.body.point = Point(10, 10)
        robot.body.heading = 0
        square = Square(Point(1, 2), type=Square.SOLID)
        map = Map('x', 10)
        map.append(square)

        target = ObstacleIdentifier(map)
        assert(target.is_obstacle(square, robot))

    def test_due_south(self):
        robot = Robot()
        robot.body.point = Point(10, 20)
        robot.body.heading = 0
        square = Square(Point(1, 1), type=Square.SOLID)
        map = Map('x', 10)
        map.append(square)

        target = ObstacleIdentifier(map)
        assert(not target.is_obstacle(square, robot))
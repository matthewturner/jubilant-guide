from jubilant import Square, Point


class Map:
    def __init__(self, id, square_size_cm=10):
        self.__id = id
        self.__square_size = square_size_cm
        self.__squares = []

    def append(self, square):
        self.__squares.append(square)

    @property
    def squares(self):
        return self.__squares

    @property
    def id(self):
        return self.__id
    
    @property
    def square_size(self):
        return self.__square_size

    def locate(self, point_cm):
        x = int(point_cm.x / self.__square_size)
        y = int(point_cm.y / self.__square_size)
        for s in self.__squares:
            if s.point.x == x and s.point.y == y:
                return s
        return None

    @property
    def width(self):
        return max(self.__squares,
                   key=lambda s: s.point.x,
                   default=Square(Point(-1, 0), Square.OPEN)).point.x + 1

    @property
    def height(self):
        return max(self.__squares,
                   key=lambda s: s.point.y,
                   default=Square(Point(0, -1), Square.OPEN)).point.y + 1

    def interesting_squares(self):
        return filter(lambda s: s.type != Square.OPEN, self.__squares)

from jubilant import Point


class Square:
    OPEN = 0
    SOLID = 1
    TRANSPARENT = 2

    TYPE_NAMES = {
        OPEN: 'open',
        SOLID: 'solid',
        TRANSPARENT: 'transparent'
    }

    def __init__(self, point, type=OPEN, type_name=None, scale=1):
        self.__point = point
        self.__scale = scale
        if type != None:
            self.__type = type
        if type_name:
            self.__type = self.type_from_name(type_name)

    def __repr__(self):
        return "Square({}, type_name='{}')".format(repr(self.__point), self.type_name)

    def points(self, scale=1):
        adjusted_scale = scale * self.__scale
        return (
            self.__point.scale(adjusted_scale),
            self.__point.translate(Point(1, 0)).scale(adjusted_scale),
            self.__point.translate(Point(1, 1)).scale(adjusted_scale),
            self.__point.translate(Point(0, 1)).scale(adjusted_scale)
        )

    def lines(self, scale=1, point=None):
        points = self.points(scale)

        if not point:
            return (
                (points[0], points[1]),
                (points[1], points[2]),
                (points[2], points[3]),
                (points[3], points[0])
            )

        lines = [
            ((points[0], points[1]), points[0].distance_from(
                point) + points[1].distance_from(point)),
            ((points[1], points[2]), points[1].distance_from(
                point) + points[2].distance_from(point)),
            ((points[2], points[3]), points[2].distance_from(
                point) + points[3].distance_from(point)),
            ((points[3], points[0]), points[3].distance_from(
                point) + points[0].distance_from(point))
        ]

        lines.sort(key=lambda x: x[1])
        line_a = lines[0][0]
        line_b = lines[1][0]
        angle_a = point.angle(line_a[0], line_a[1])
        angle_b = point.angle(line_b[0], line_b[1])
        if angle_a > angle_b:
            return tuple([line_a])
        return tuple([line_a, line_b])

    @property
    def type_name(self):
        return Square.TYPE_NAMES[self.__type]

    @property
    def point(self):
        return self.__point

    def center(self, scale=1):
        return self.__point.translate(Point(0.5, 0.5)).scale(scale * self.__scale)

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    def type_from_name(self, name):
        for id, type_name in Square.TYPE_NAMES.items():
            if name == type_name:
                return id
        return None

    def next_type(self):
        return (self.__type + 1) % len(Square.TYPE_NAMES.keys())

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

    def __init__(self, point, type=None, type_name=None):
        self.__point = point
        if type != None:
            self.__type = type
        if type_name:
            self.__type = self.type_from_name(type_name)

    def points(self, scale=1):
        return (
            self.__point.scale(scale),
            self.__point.translate(Point(1, 0)).scale(scale),
            self.__point.translate(Point(1, 1)).scale(scale),
            self.__point.translate(Point(0, 1)).scale(scale)
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
            ((points[0], points[1]), points[0].distance_from(point) + points[1].distance_from(point)),
            ((points[1], points[2]), points[1].distance_from(point) + points[2].distance_from(point)),
            ((points[2], points[3]), points[2].distance_from(point) + points[3].distance_from(point)),
            ((points[3], points[0]), points[3].distance_from(point) + points[0].distance_from(point))
        ]

        lines.sort(key=lambda x: x[1])
        return tuple([lines[0][0], lines[1][0]])


    @property
    def type_name(self):
        return Square.TYPE_NAMES[self.__type]

    @property
    def x(self):
        return self.__point.x
    
    @property
    def y(self):
        return self.__point.y
    
    def center(self, scale=1):
        return self.__point.translate(Point(0.5, 0.5)).scale(scale)

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
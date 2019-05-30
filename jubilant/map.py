from jubilant.square import Square

class Map:
    def __init__(self):
        self.__squares = []

    def append(self, square):
        self.__squares.append(square)
    
    @property
    def squares(self):
        return self.__squares

    @property
    def width(self):
        return max(self.__squares, 
            key=lambda s: s.x, 
            default=Square(-1, 0, Square.OPEN)).x + 1
    
    @property
    def height(self):
        return max(self.__squares, 
            key=lambda s: s.y, 
            default=Square(0, -1, Square.OPEN)).y + 1
    
    def interesting_squares(self):
        return filter(lambda s: s.type != Square.OPEN, self.__squares)

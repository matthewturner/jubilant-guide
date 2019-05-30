class Square:
    OPEN = 0
    SOLID = 1

    def __init__(self, x, y, type):
        self.__x = x
        self.__y = y
        self.__type = type

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, type):
        self.__type = type

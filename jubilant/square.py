class Square:
    OPEN = 0
    SOLID = 1
    TRANSPARENT = 2

    TYPE_NAMES = {
        OPEN: 'open',
        SOLID: 'solid',
        TRANSPARENT: 'transparent'
    }

    def __init__(self, x, y, type=None, type_name=None):
        self.__x = x
        self.__y = y
        if type != None:
            self.__type = type
        if type_name:
            self.__type = self.type_from_name(type_name)

    def points(self):
        return [
            [self.__x, self.__y], 
            [self.__x + 10, self.__y]#,
            #[self.__x + 10, self.__y + 10], 
            #[self.__x, self.__y + 10]
        ]

    @property
    def type_name(self):
        return Square.TYPE_NAMES[self.__type]

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

    def type_from_name(self, name):
        for id, type_name in Square.TYPE_NAMES.items():
            if name == type_name:
                return id
        return None

    def next_type(self):
        return (self.__type + 1) % len(Square.TYPE_NAMES.keys())
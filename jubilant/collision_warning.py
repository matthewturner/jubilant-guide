class CollisionWarning(RuntimeError):
    def __init__(self, distance):
        self.__distance = distance
    
    @property
    def distance(self):
        return self.__distance
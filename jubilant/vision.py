import board
from .eye import Eye
from .collision_warning import CollisionWarning

class Vision:
    INFINITY = 99999

    def __init__(self):
        self.__left_eye = Eye(board.D9, board.D8, name='left')
        self.__right_eye = Eye(board.D10, board.D8, name='right')

    def is_straight_infront(self):
        distance_from_left_eye = self.__distance_from(self.__left_eye)
        distance_from_right_eye = self.__distance_from(self.__right_eye)
        min_distance = min(distance_from_left_eye, distance_from_right_eye)
        if min_distance <= 22:
            raise CollisionWarning(min_distance)
        return distance_from_left_eye == distance_from_right_eye

    def is_closer_to_left(self):
        distance_from_left_eye = self.__distance_from(self.__left_eye)
        distance_from_right_eye = self.__distance_from(self.__right_eye)
        return distance_from_left_eye < distance_from_right_eye

    def is_closer_to_right(self):
        distance_from_left_eye = self.__distance_from(self.__left_eye)
        distance_from_right_eye = self.__distance_from(self.__right_eye)
        return distance_from_right_eye < distance_from_left_eye

    def __distance_from(self, eye):
        try:
            last_distance = int(eye.last_distance)
            current_distance = int(eye.distance)
            if current_distance != last_distance:
                print("Distance (%s): % 3d" % (eye.name, current_distance))
            return current_distance
        except RuntimeError:
            print("Retrying!")
            return Vision.INFINITY

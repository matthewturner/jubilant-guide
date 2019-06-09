from jubilant import Square, Map, MapRepository, Point
import numpy as np
import math


class MapCanvasManager:
    PADDING = 5
    DEFAULT_ROOM_HEIGHT = 20
    DEFAULT_ROOM_WIDTH = 40
    SQUARE_SIZE = 10

    def __init__(self, canvas):
        self.__square_map = {}
        self.__canvas = canvas
        self.__canvas.bind("<Configure>", self.__configure)
        self.__canvas.tag_bind(
            'square', '<ButtonPress-1>', self.__on_square_click)
        self.__robot_last_position = None

        self.__map_repository = MapRepository()
        self.__map = Map('map', square_size_cm=MapCanvasManager.SQUARE_SIZE)
        for y in range(MapCanvasManager.DEFAULT_ROOM_HEIGHT):
            for x in range(MapCanvasManager.DEFAULT_ROOM_WIDTH):
                self.__map.append(Square(Point(x, y), type=Square.OPEN))

    def __configure(self, event):
        self.__draw(event.width)

    def __on_square_click(self, event):
        id = event.widget.find_closest(event.x, event.y)[0]
        square = self.__square_map[id]
        square.type = square.next_type()
        fill = self.__fill_for(square.type)
        self.__canvas.itemconfigure(id, fill=fill)

    def __draw(self, max_width=None):
        self.__canvas.delete("all")
        square_size = int((max_width - 10) / self.__map.width)
        self.__square_map.clear()
        for square in self.__map.squares:
            fill = self.__fill_for(square.type)
            rectangle_id = self.__canvas.create_rectangle(square.x * square_size + MapCanvasManager.PADDING,
                                                          square.y * square_size + MapCanvasManager.PADDING,
                                                          square.x * square_size + square_size + MapCanvasManager.PADDING,
                                                          square.y * square_size + square_size + MapCanvasManager.PADDING,
                                                          fill=fill, outline='black', tags='square')
            self.__square_map[rectangle_id] = square

    def __fill_for(self, type):
        fills = {
            Square.OPEN: 'gray',
            Square.SOLID: 'blue',
            Square.TRANSPARENT: 'orange'
        }
        return fills[type]

    def locate(self, robot):
        robot.update()
        square = self.__map.locate(robot.body.point.x, robot.body.point.y)

        if self.__robot_last_position:
            self.__canvas.itemconfigure(
                self.__robot_last_position, fill='gray')
        self.__robot_last_position = self.__find_square(square)
        self.__canvas.itemconfigure(self.__robot_last_position, fill='pink')
        self.__distance_from_obstacle(robot)
    
    def __distance_from_obstacle(self, robot):
        north = robot.body.point.translate(Point(0, 1))
        for square in self.__map.interesting_squares():
            for line in square.lines(MapCanvasManager.SQUARE_SIZE, robot.body.point):
                start_point = line[0]
                end_point = line[1]
                start_angle = self.__angle(north, robot.body.point, start_point)
                end_angle = self.__angle(north, robot.body.point, end_point)
                if (start_angle <= robot.body.heading <= end_angle) or (start_angle >= robot.body.heading >= end_angle):
                    distance_between = robot.body.point.distance_from(start_point)
                    robot.vision.left_eye.sensor.distance = distance_between
                    robot.vision.right_eye.sensor.distance = distance_between
                    return
        
        robot.vision.left_eye.sensor.distance = 400
        robot.vision.right_eye.sensor.distance = 400            

    def __angle(self, p0, p1, p2):
        ''' compute angle (in degrees) for p0p1p2 corner
        Inputs:
            p0,p1,p2 - points in the form of [x,y]
        '''
        v0 = np.array(p0.array()) - np.array(p1.array())
        v1 = np.array(p2.array()) - np.array(p1.array())

        angle = np.math.atan2(np.linalg.det([v0, v1]), np.dot(v0, v1))
        return np.degrees(angle)

    def __find_square(self, square):
        for key, value in self.__square_map.items():
            if value == square:
                return key
        return None

    def load_map(self):
        self.__map = self.__map_repository.find('map')
        self.__draw(self.__canvas.winfo_width())

    def save_map(self):
        self.__map_repository.save(self.__map)

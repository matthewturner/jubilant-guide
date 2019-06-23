from jubilant import Square, Map, MapRepository, Point
from world import ObstacleIdentifier


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
        self.__robot_last_square = None
        self.__robot_last_position = None
        self.__robot_avatar = None
        self.__square_size = 1
        self.__scale = 1

        self.__map_repository = MapRepository()
        self.__map = Map('map', square_size_cm=MapCanvasManager.SQUARE_SIZE)
        for y in range(MapCanvasManager.DEFAULT_ROOM_HEIGHT):
            for x in range(MapCanvasManager.DEFAULT_ROOM_WIDTH):
                self.__map.append(Square(Point(x, y), type=Square.OPEN))

        self.__obstacle_identifier = ObstacleIdentifier(self.__map)

    def __configure(self, event):
        self.__draw(event.width)

    def __on_square_click(self, event):
        id = event.widget.find_closest(event.x, event.y)[0]
        square, tl = self.__square_map[id]
        square.type = square.next_type()
        fill = self.__fill_for(square.type)
        self.__canvas.itemconfigure(id, fill=fill)

    def __draw(self, max_width=None):
        self.__canvas.delete("all")
        self.__robot_last_position = None
        self.__robot_avatar = None
        self.__square_size = square_size = int(
            (max_width - 10) / self.__map.width)
        self.__scale = (max_width - 10) / (self.__map.width * self.__map.square_size)
        self.__square_map.clear()
        for square in self.__map.squares:
            fill = self.__fill_for(square.type)
            tl = Point(square.point.x * square_size + MapCanvasManager.PADDING,
                       square.point.y * square_size + MapCanvasManager.PADDING)
            br = Point(square.point.x * square_size + square_size + MapCanvasManager.PADDING,
                       square.point.y * square_size + square_size + MapCanvasManager.PADDING)
            rectangle_id = self.__canvas.create_rectangle(
                tl.x, tl.y, br.x, br.y, fill=fill, outline='black', tags='square')
            self.__square_map[rectangle_id] = (square, tl)

    def __fill_for(self, type):
        fills = {
            Square.OPEN: 'gray',
            Square.SOLID: 'blue',
            Square.TRANSPARENT: 'orange'
        }
        return fills[type]

    def locate(self, robot):
        robot.update()
        square = self.__map.locate(robot.body.point)

        if self.__robot_last_square:
            self.__canvas.itemconfigure(self.__robot_last_square, fill='gray')
        self.__robot_last_square = self.__find_square(square)
        self.__canvas.itemconfigure(self.__robot_last_square, fill='pink')
        self.__draw_robot(robot)
        self.__distance_from_obstacle(robot)

    def __create_circle(self, point, r, fill='green'):
        radius = Point(r, r)
        tl = point - radius
        br = point + radius
        return self.__canvas.create_oval(tl.x, tl.y, br.x, br.y, fill=fill)

    def __draw_robot(self, robot):
        if not self.__robot_avatar:
            current_position = robot.body.point
            print("Robot current position %s" % current_position)
            avatar_size = self.__square_size / 2
            if avatar_size < 2:
                avatar_size = 2
            canvas_position = current_position.scale(self.__scale)
            self.__robot_avatar = self.__create_circle(
                canvas_position, avatar_size)
            self.__robot_last_position = robot.body.point

        delta = (robot.body.point - self.__robot_last_position).scale(self.__scale)

        self.__canvas.move(self.__robot_avatar, delta.x, delta.y)
        self.__robot_last_position = robot.body.point

    def __distance_from_obstacle(self, robot):
        square = self.__obstacle_identifier.obstacle(robot)
        if square:
            distance_between = robot.body.point.distance_from(
                square.center(self.__map.square_size))
            robot.vision.left_eye.sensor.distance = distance_between
            robot.vision.right_eye.sensor.distance = distance_between
            return

        robot.vision.left_eye.sensor.distance = 400
        robot.vision.right_eye.sensor.distance = 400

    def __find_square(self, square):
        for key, value in self.__square_map.items():
            sq, tl = value
            if sq == square:
                return key
        return None

    def load_map(self):
        self.__map = self.__map_repository.find('map')
        self.__obstacle_identifier = ObstacleIdentifier(self.__map)
        self.__draw(self.__canvas.winfo_width())

    def save_map(self):
        self.__map_repository.save(self.__map)

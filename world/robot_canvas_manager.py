from jubilant import Square, Map, MapRepository


class RobotCanvasManager:
    PADDING = 5

    def __init__(self, canvas):
        self.__canvas = canvas

    def draw(self):
        canvas = self.__canvas
        self.__robot_sonar_id = \
            canvas.create_rectangle(20 + RobotCanvasManager.PADDING,
                                    RobotCanvasManager.PADDING,
                                    20 + 60 + RobotCanvasManager.PADDING,
                                    10 + RobotCanvasManager.PADDING,
                                    fill='gray', outline='black', tags='square')
        self.__robot_left_wheel_id = \
            canvas.create_rectangle(RobotCanvasManager.PADDING,
                                    20 + RobotCanvasManager.PADDING,
                                    20 + RobotCanvasManager.PADDING,
                                    20 + 40 + RobotCanvasManager.PADDING,
                                    fill='black', outline='black', tags='square')
        self.__robot_rectangle_id = \
            canvas.create_rectangle(20 + RobotCanvasManager.PADDING,
                                    20 + 10 + RobotCanvasManager.PADDING,
                                    20 + 60 + RobotCanvasManager.PADDING,
                                    20 + 10 + 80 + RobotCanvasManager.PADDING,
                                    fill='gray', outline='black', tags='square')
        self.__robot_right_wheel_id = \
            canvas.create_rectangle(20 + 60 + RobotCanvasManager.PADDING,
                                    20 + RobotCanvasManager.PADDING,
                                    20 + 60 + 20 + RobotCanvasManager.PADDING,
                                    20 + 40 + RobotCanvasManager.PADDING,
                                    fill='black', outline='black', tags='square')

    def show_sonar(self):
        self.__canvas.itemconfigure(
            self.__robot_sonar_id, fill='white')
        self.__canvas.after(300, self.__stop_sonar)

    def __stop_sonar(self):
        self.__canvas.itemconfigure(
            self.__robot_sonar_id, fill='gray')

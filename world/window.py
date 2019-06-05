import tkinter as tk
import board
from jubilant import Robot, Square, queue
from world import WorkerWindow, MapCanvasManager, RobotCanvasManager, PinManager
from functools import partial


class Window(WorkerWindow):
    def _init_layout(self):
        super().window.title("World")

        self.__frame_left = tk.Frame(super().window)
        self.__frame_left.pack(side=tk.LEFT, ipadx=10, ipady=10)

        self.__button_load = tk.Button(
            self.__frame_left, text="Load", command=self.__load_map)
        self.__button_load.pack()

        self.__button_save = tk.Button(
            self.__frame_left, text="Save", command=self.__save_map)
        self.__button_save.pack()

        self.__frame_right = tk.Frame(super().window)
        self.__frame_right.pack(side=tk.RIGHT)

        self.__frame_right_top = tk.Frame(self.__frame_right, height=20)
        self.__frame_right_top.pack(ipadx=10, ipady=10)
        self.__frame_right_middle = tk.Frame(self.__frame_right, height=100)
        self.__frame_right_middle.pack(ipadx=10, ipady=10)
        self.__frame_right_bottom = tk.Frame(self.__frame_right, height=20)
        self.__frame_right_bottom.pack(ipadx=10, ipady=10)

        self.__button_start = tk.Button(
            self.__frame_right_top, text="Start", command=partial(self._start, self.__start_robot))
        self.__button_start.pack()
        self.__button_ping = tk.Button(
            self.__frame_right_top, text="Ping", command=partial(self._start, self.__ping))
        self.__button_ping.pack()

        self.__canvas_robot = tk.Canvas(self.__frame_right_middle, width=100)
        self.__canvas_robot.pack()
        self.__robot_canvas_manager = RobotCanvasManager(self.__canvas_robot)
        self.__robot_canvas_manager.draw()

        self.__robot = Robot()
        self.__robot.body.x = 100
        self.__robot.body.y = 60
        self.__robot.body.time_scale = 10

        self.__pin_manager = PinManager(self.__frame_right_bottom)
        self.__pin_manager.listener = self.__pin_listener

        self.__canvas = tk.Canvas(super().window)
        self.__canvas.pack(fill="both", expand=True)
        self.__map_canvas_manager = MapCanvasManager(self.__canvas)
        self.__map_canvas_manager.locate(self.__robot)

    def __load_map(self):
        self.__map_canvas_manager.load_map()

    def __save_map(self):
        self.__map_canvas_manager.save_map()

    def __start_robot(self):
        self.__robot.start()

        while True:
            queue.work_off()

    def __ping(self):
        print(self.__robot.vision.right_eye.distance)

    def __pin_listener(self, args=None):
        if self._invoke_required:
            self._invoke(self.__pin_listener, args)
            return

        self.__pin_manager.update(args)
        if args.pin == board.D9 and args.value:
            self.__robot_canvas_manager.show_sonar()
        self.__map_canvas_manager.locate(self.__robot)

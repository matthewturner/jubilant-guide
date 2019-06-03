from tkinter import *
import threading
import time
import board
from queue import Queue, Empty
from jubilant import Robot, Square, queue
from digitalio import DigitalInOut
from world import MapCanvasManager, RobotCanvasManager


class Window:
    def __init__(self):
        self.__window = Tk()

        self.__window.title("World")

        self.__frame_left = Frame(self.__window)
        self.__frame_left.pack(side=LEFT, ipadx=10, ipady=10)

        self.__button_load = Button(
            self.__frame_left, text="Load", command=self.__load_map)
        self.__button_load.pack()

        self.__button_save = Button(
            self.__frame_left, text="Save", command=self.__save_map)
        self.__button_save.pack()

        self.__frame_right = Frame(self.__window)
        self.__frame_right.pack(side=RIGHT)

        self.__frame_right_top = Frame(self.__frame_right, height=20)
        self.__frame_right_top.pack(ipadx=10, ipady=10)
        self.__frame_right_middle = Frame(self.__frame_right, height=100)
        self.__frame_right_middle.pack(ipadx=10, ipady=10)
        self.__frame_right_bottom = Frame(self.__frame_right, height=20)
        self.__frame_right_bottom.pack(ipadx=10, ipady=10)

        self.__button_start = Button(
            self.__frame_right_top, text="Start", command=self.__start)
        self.__button_start.pack()

        self.__pins = {}
        for pin in range(14):
            self.__registerPin(pin)

        self.__canvas_robot = Canvas(self.__frame_right_middle, width=100)
        self.__canvas_robot.pack()
        self.__robot_canvas_manager = RobotCanvasManager(self.__canvas_robot)
        self.__robot_canvas_manager.draw()

        self.__robot = Robot()
        self.__robot.body.x = 100
        self.__robot.body.y = 60
        self.__robot.body.time_scale = 10

        self.__canvas = Canvas(self.__window)
        self.__canvas.pack(fill="both", expand=True)
        self.__map_canvas_manager = MapCanvasManager(self.__canvas)
        self.__map_canvas_manager.locate(self.__robot)

        self.__invoke_queue = Queue()
        self.__window.after(50, self.__process_queue)

    def show(self):
        self.__window.mainloop()

    def __registerPin(self, pin):
        label_pin = Label(self.__frame_right_bottom, text="D%d" % pin)
        label_pin.pack(side=LEFT)
        self.__pins[pin] = label_pin

    def __process_queue(self):
        try:
            for _ in range(5):
                callable, args = self.__invoke_queue.get_nowait()
                callable(args)
        except Empty:
            pass
        self.__window.after(50, self.__process_queue)

    def __callback(self, args):
        print(args)

    def __load_map(self):
        self.__map_canvas_manager.load_map()

    def __save_map(self):
        self.__map_canvas_manager.save_map()

    def __start(self):
        self.__worker_thread = threading.Thread(target=self.__start_robot)
        self.__worker_thread.start()

    def __start_robot(self):
        self.__robot.start()
        for pin in DigitalInOut.Instances:
            pin.listener = self.__pin_listener

        while True:
            queue.work_off()

    @property
    def __invoke_required(self):
        return threading.current_thread() == self.__worker_thread

    def __pin_listener(self, args=None):
        if self.__invoke_required:
            self.__invoke_queue.put((self.__pin_listener, args))
        else:
            label_pin = self.__pins[args.pin]
            if args.value:
                label_pin.configure(background='red')
            else:
                label_pin.configure(background='gray')
            if args.pin == board.D9 and args.value:
                self.__robot_canvas_manager.show_sonar()
            self.__map_canvas_manager.locate(self.__robot)

from tkinter import *
import _thread as thread
import time
from queue import Queue, Empty
from jubilant import robot, Square, Map, MapRepository, queue
from digitalio import DigitalInOut


class Window:
    DEFAULT_ROOM_HEIGHT = 20
    DEFAULT_ROOM_WIDTH = 40
    PADDING = 5

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
        self.__frame_right.pack(side=RIGHT, ipadx=10, ipady=10)

        self.__button_start = Button(
            self.__frame_right, text="Start", command=self.__start)
        self.__button_start.pack()

        self.__pins = {}
        for pin in range(14):
            self.__registerPin(pin)

        self.__canvas = Canvas(self.__window)
        self.__canvas.pack(fill="both", expand=True)

        self.__canvas.bind("<Configure>", self.__configure)
        self.__canvas.tag_bind(
            'square', '<ButtonPress-1>', self.__on_square_click)

        self.__map_repository = MapRepository()
        self.__map = Map('map')
        for y in range(Window.DEFAULT_ROOM_HEIGHT):
            for x in range(Window.DEFAULT_ROOM_WIDTH):
                self.__map.append(Square(x, y, type=Square.OPEN))

        self.__square_map = {}
        self.__invoke_queue = Queue()
        self.__window.after(100, self.__process_queue)

    def show(self):
        self.__window.mainloop()

    def __registerPin(self, pin):
        label_pin = Label(self.__frame_right, text="D%d" % pin)
        label_pin.pack(side=LEFT)
        self.__pins[pin] = label_pin

    def __process_queue(self):
        try:
            for _ in range(5):
                callable, args = self.__invoke_queue.get_nowait()
                callable(args)
        except Empty:
            pass
        self.__window.after(10, self.__process_queue)

    def __callback(self, args):
        print(args)

    def __load_map(self):
        self.__map = self.__map_repository.find('map')
        self.__canvas.delete("all")
        self.__draw(self.__canvas.winfo_width())

    def __save_map(self):
        self.__map_repository.save(__map)

    def __start(self):
        thread.start_new_thread(self.__start_robot)

    def __fill_for(self, type):
        fills = {
            Square.OPEN: 'gray',
            Square.SOLID: 'blue',
            Square.TRANSPARENT: 'orange'
        }
        return fills[type]

    def __draw(self, max_width):
        square_size = int((max_width - 10) / self.__map.width)
        self.__square_map.clear()
        for square in self.__map.squares:
            fill = self.__fill_for(square.type)
            rectangle_id = self.__canvas.create_rectangle(square.x * square_size + Window.PADDING,
                                                          square.y * square_size + Window.PADDING,
                                                          square.x * square_size + square_size + Window.PADDING,
                                                          square.y * square_size + square_size + Window.PADDING,
                                                          fill=fill, outline='black', tags='square')
            self.__square_map[rectangle_id] = square

    def __configure(self, event):
        self.__canvas.delete("all")
        self.__draw(event.width)

    def __on_square_click(self, event):
        id = event.widget.find_closest(event.x, event.y)[0]
        square = self.__square_map[id]
        square.type = square.next_type()
        fill = self.__fill_for(square.type)
        self.__canvas.itemconfigure(id, fill=fill)

    def __start_robot(self):
        robot.start()
        for pin in DigitalInOut.Instances:
            pin.listener = self.__pin_listener

        while True:
            queue.work_off()

    def __pin_listener(self, args=None):
        if args.invoke_required:
            args.invoke_required = False
            self.__invoke_queue.put((self.__pin_listener, args))
        else:
            label_pin = self.__pins[args.pin]
            if args.value:
                label_pin.configure(background='red')
            else:
                label_pin.configure(background='gray')


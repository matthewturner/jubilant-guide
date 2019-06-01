from tkinter import *
from jubilant.square import Square
from jubilant.map import Map
from jubilant.map_repository import MapRepository
import _thread as thread
from jubilant.queue import queue
from jubilant import robot
import time

window = Tk()

window.title("World")


def load_map():
    global __map
    __map = __map_repository.find('map')
    canvas.delete("all")
    draw(canvas.winfo_width())


def save_map():
    __map_repository.save(__map)

frame_left = Frame(window)
frame_left.pack(side=LEFT, ipadx=10, ipady=10)

button_load = Button(frame_left, text="Load", command=load_map)
button_load.pack()

button_save = Button(frame_left, text="Save", command=save_map)
button_save.pack()


def start():
    thread.start_new_thread(start_robot)

frame_right = Frame(window)
frame_right.pack(side=RIGHT, ipadx=10, ipady=10)

button_start = Button(frame_right, text="Start", command=start)
button_start.pack()

canvas = Canvas(window)
canvas.pack(fill="both", expand=True)

DEFAULT_ROOM_HEIGHT = 20
DEFAULT_ROOM_WIDTH = 40
PADDING = 5

__map_repository = MapRepository()
__map = Map('map')
for y in range(DEFAULT_ROOM_HEIGHT):
    for x in range(DEFAULT_ROOM_WIDTH):
        __map.append(Square(x, y, type=Square.OPEN))

__square_map = {}


def fill_for(type):
    fills = {
        Square.OPEN: 'gray',
        Square.SOLID: 'blue',
        Square.TRANSPARENT: 'orange'
    }
    return fills[type]


def draw(max_width):
    square_size = int((max_width - 10) / __map.width)
    __square_map.clear()
    for square in __map.squares:
        fill = fill_for(square.type)
        rectangle_id = canvas.create_rectangle(square.x * square_size + PADDING,
                                               square.y * square_size + PADDING,
                                               square.x * square_size + square_size + PADDING,
                                               square.y * square_size + square_size + PADDING,
                                               fill=fill, outline='black', tags='square')
        __square_map[rectangle_id] = square


def configure(event):
    canvas.delete("all")
    draw(event.width)


def on_square_click(event):
    id = event.widget.find_closest(event.x, event.y)[0]
    square = __square_map[id]
    square.type = square.next_type()
    fill = fill_for(square.type)
    canvas.itemconfigure(id, fill=fill)


def start_robot():
    robot.start()

    while True:
        queue.work_off()


canvas.bind("<Configure>", configure)
canvas.tag_bind('square', '<ButtonPress-1>', on_square_click)

window.mainloop()

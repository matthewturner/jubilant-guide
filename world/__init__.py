import json
from tkinter import *
from jubilant.square import Square
from jubilant.map import Map

window = Tk()

window.title("World")

def load_map():
    print("Load!")

button_load = Button(window, text="Load", command=load_map)
button_load.pack()

def save_map():
    data = {}  
    map = data['map'] = {}
    map['width'] = __map.width
    map['height'] = __map.height
    squares = map['squares'] = []
    for square in __map.interesting_squares():
        squares.append({
            'x': square.x,
            'y': square.y,
            'type': square.type
        })

    with open('map.json', 'w') as outfile:  
        json.dump(data, outfile, indent=4)

button_save = Button(window, text="Save", command=save_map)
button_save.pack()

canvas = Canvas(window)
canvas.pack(fill="both", expand=True)

ROOM_HEIGHT = 20
ROOM_WIDTH = 40
PADDING = 5

__map = Map()
for y in range(ROOM_HEIGHT):
    for x in range(ROOM_WIDTH):
        __map.append(Square(x, y, Square.OPEN))

__square_map = {}

def draw(max_width):
    square_size = int((max_width - 10) / ROOM_WIDTH)
    __square_map.clear()
    for square in __map.squares:
        fill = 'gray' if square.type == Square.OPEN else 'blue'
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
    canvas.itemconfigure(id, fill='blue')
    __square_map[id].type = Square.SOLID if __square_map[id].type == Square.OPEN else Square.OPEN
    

canvas.bind("<Configure>", configure)      
canvas.tag_bind('square', '<ButtonPress-1>', on_square_click)   

window.mainloop()
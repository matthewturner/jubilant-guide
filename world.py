from tkinter import *

window = Tk()

window.title("World")

canvas = Canvas(window, width=200, height=100)
canvas.pack()

canvas.create_rectangle(50, 25, 150, 75, fill='blue')

window.mainloop()
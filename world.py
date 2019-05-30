from tkinter import *

window = Tk()

window.title("World")

canvas = Canvas(window)
canvas.pack(fill="both", expand=True)

for i in range(20):
    canvas.create_rectangle(i*20+5, i*20+5, i*20+25, i*20+25, 
        fill='gray', outline='black')

window.mainloop()
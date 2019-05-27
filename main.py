import time
import jubilant.voltage
import jubilant.swirl
import jubilant.motion
import jubilant.led
import jubilant.something
from jubilant.queue import queue

i = 0


def check_in_front():
    if something.is_infront():
        led.on()
        motion.turn_right(90)
    else:
        led.off()
        motion.forward()


def show_swirl():
    global i
    swirl.next(i)
    i = (i+1) % 256


queue.enqueue(check_in_front, delay=0.2, repeat=True)
queue.enqueue(show_swirl, repeat=True)

while True:
    queue.work_off()

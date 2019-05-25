import time
import voltage
import swirl
import motion
import led
import something
from queue import Queue

# motion.test()
led.on()

queue = Queue()


def check_in_front():
    if something.is_infront():
        led.on()
        motion.turn_right(90)
    else:
        led.off()
        motion.forward()


i = 0


def show_swirl():
    global i
    swirl.next(i)
    i = (i+1) % 256


queue.enqueue(check_in_front, delay=0.2, repeat=True)
queue.enqueue(show_swirl, repeat=True)

while True:
    queue.work_off()

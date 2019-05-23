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
    print('Turning...')
    motion.turn_right(90)
  else:
    print('Moving forward...')
    motion.forward()
  queue.enqueue(check_in_front, 0.5)

queue.enqueue(check_in_front, 0.5)

i = 0
while True:
  swirl.next(i)
  queue.work_off()
  i = (i+1) % 256

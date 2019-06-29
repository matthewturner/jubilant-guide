import logging
from jubilant import queue, robot

logging.basicConfig(level=logging.INFO)

robot.start()

while True:
    queue.work_off()

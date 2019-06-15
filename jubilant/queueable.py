import time
from .queue import queue as q


class Queueable:
    def __init__(self, delay=0, repeat=False, queue=q):
        self.__delay = delay
        self.__repeat = repeat
        self.__queue = queue
        self.__wrapped_action = None

    def delay(self):
        self.__queue.enqueue(self.__wrapped_action,
                             delay=self.__delay,
                             repeat=self.__repeat)

    def __call__(self, action):
        def wrapped_action(*args, **kwargs):
            action(*args, **kwargs)
        self.__wrapped_action = wrapped_action
        return self.delay

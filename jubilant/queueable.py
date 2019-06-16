import time
import types
from .queue import queue as q


class Queueable:
    def __init__(self, delay=0, repeat=False, queue=q):
        self.__delay = delay
        self.__repeat = repeat
        self.__queue = queue

    def __call__(self, action):
        queue = self.__queue
        delay = self.__delay
        repeat = self.__repeat
        def wrapped_action(self=None):
            bound_action = action
            if self:
                bound_action = types.MethodType(action, self)
            queue.enqueue(bound_action, delay=delay, repeat=repeat)
        return wrapped_action

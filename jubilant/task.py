import time


class Task:
    def __init__(self, action, delay, repeat):
        self.__delay = delay
        self.__action = action
        self.__registered = time.monotonic()
        self.__repeat = repeat

    @property
    def ready(self):
        return time.monotonic() >= self.__registered + self.__delay

    @property
    def repeat(self):
        return self.__repeat

    def reset(self):
        self.__registered = time.monotonic()

    def perform(self):
        self.__action()

    def perform_if_ready(self):
        if not self.ready:
            return False

        self.perform()
        return True

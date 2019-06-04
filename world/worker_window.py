import tkinter as tk
import threading
import time
from queue import Queue, Empty

class WorkerWindow:
    def __init__(self):
        self.__window = tk.Tk()

        self._init_layout()

        self.__invoke_queue = Queue()
        self.__window.after(50, self.__process_queue)

    def _init_layout(self):
        pass
    
    def show(self):
        self.__window.mainloop()

    def _start(self, target):
        self.__worker_thread = threading.Thread(target=target)
        self.__worker_thread.start()

    @property
    def _invoke_required(self):
        return threading.current_thread() == self.__worker_thread

    def _invoke(self, target, args):
        self.__invoke_queue.put((target, args))

    @property
    def window(self):
        return self.__window
    
    def frame(self):
        return tk.Frame(self.__window)

    def __process_queue(self):
        try:
            for _ in range(5):
                callable, args = self.__invoke_queue.get_nowait()
                callable(args)
        except Empty:
            pass
        self.__window.after(50, self.__process_queue)
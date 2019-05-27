from jubilant.task import Task


class Queue:
    def __init__(self):
        self.__tasks = []
        self.__processed_tasks = []

    def enqueue(self, action, delay=0, repeat=False):
        self.__tasks.append(Task(action, delay, repeat))

    def work_off(self):
        for task in self.__tasks:
            if task.perform_if_ready():
                self.__processed_tasks.append(task)

        for task in self.__processed_tasks:
            self.__tasks.remove(task)
            if task.repeat:
                task.reset()
                self.__tasks.append(task)

        self.__processed_tasks.clear()

    @property
    def count(self):
        return len(self.__tasks)
    
    @property
    def count_processed(self):
        return len(self.__processed_tasks)


queue = Queue()

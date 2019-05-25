from task import Task

class Queue:
  def __init__(self):
    self.__tasks = []

  def enqueue(self, action, delay=0, repeat=False):
    self.__tasks.append(Task(action, delay, repeat))

  def work_off(self):
    tasks_to_remove = []
    for task in self.__tasks:
      if task.perform_if_ready():
        tasks_to_remove.append(task)

    for task in tasks_to_remove:
      self.__tasks.remove(task)
      if task.repeat:
        task.reset()
        self.__tasks.append(task)
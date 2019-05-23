from task import Task

class Queue:
  def __init__(self):
    self.__tasks = []
  
  def enqueue(self, action, delay):
    self.__tasks.append(Task(action, delay))

  def work_off(self):
    for task in self.__tasks:
      if task.perform_if_ready():
        self.__tasks.remove(task)
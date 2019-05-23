import time

class Task:
  def __init__(self, action, delay):
    self.__delay = delay
    self.__action = action
    self.__registered = time.monotonic()

  @property
  def ready(self):
    return time.monotonic() > self.__registered + self.__delay

  def perform(self):
    print('Performing...')
    self.__action()

  def perform_if_ready(self):
    if not self.ready:
      return False
    
    self.perform()
    return True
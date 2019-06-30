from types import SimpleNamespace
from events import Events

class DigitalInOut:
    Instances = []

    def __init__(self, pin):
        self.events = Events(('value_changed')) 
        self.__pin = pin
        self.__value = False
        DigitalInOut.Instances.append(self)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
        self.events.value_changed(SimpleNamespace(
                pin=self.__pin, value=self.__value))

    @property
    def pin(self):
        return self.__pin

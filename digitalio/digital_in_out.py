from types import SimpleNamespace


class DigitalInOut:
    Instances = []

    def __init__(self, pin):
        self.__pin = pin
        self.__value = False
        self.__listener = None
        DigitalInOut.Instances.append(self)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
        if self.__listener:
            self.__listener(SimpleNamespace(
                pin=self.__pin, value=self.__value, invoke_required=True))

    @property
    def pin(self):
        return self.__pin

    @property
    def listener(self):
        return self.__listener

    @listener.setter
    def listener(self, listener):
        self.__listener = listener

import tkinter as tk
from digitalio import DigitalInOut


class PinManager:
    def __init__(self, container):
        self.__container = container
        self.__pin_listener = None
        self.__pins = {}

        for pin in range(14):
            self.__registerPin(pin)
        
        for pin in DigitalInOut.Instances:
            pin.listener = self.__pin_listener

    def __pin_listener(self, args=None):
        if self.__listener:
            self.__listener(args)
    
    def update(self, args):
        label_pin = self.__pins[args.pin]
        if args.value:
            label_pin.configure(background='red')
        else:
            label_pin.configure(background='gray')

    @property
    def listener(self):
        return self.__listener
    
    @listener.setter
    def listener(self, listener):
        self.__listener = listener

    def __registerPin(self, pin):
        label_pin = tk.Label(self.__container, text="D%d" % pin)
        label_pin.pack(side=tk.LEFT)
        self.__pins[pin] = label_pin

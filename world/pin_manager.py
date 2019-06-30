import tkinter as tk
from digitalio import DigitalInOut
from events import Events


class PinManager:
    def __init__(self, container):
        self.events = Events(('pin_value_changed'))
        self.__container = container
        self.__pins = {}

        for pin in range(14):
            self.__registerPin(pin)
        
        for pin in DigitalInOut.Instances:
            pin.events.value_changed += self.__pin_value_changed

    def __pin_value_changed(self, args=None):
        self.events.pin_value_changed(args)
    
    def update(self, args):
        label_pin = self.__pins[args.pin]
        if args.value:
            label_pin.configure(background='red')
        else:
            label_pin.configure(background='gray')

    def __registerPin(self, pin):
        label_pin = tk.Label(self.__container, text="D%d" % pin)
        label_pin.pack(side=tk.LEFT)
        self.__pins[pin] = label_pin

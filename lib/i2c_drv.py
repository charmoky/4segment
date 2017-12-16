
from . import gpio
from .gpio import Gpio

from time import sleep
import time

def bit_delay():
    return 0
    #sleep(0.00005)

class I2C:
    def __init__(self, clk_pin, data_pin):
        self.clk  = Gpio(clk_pin, "out")
        self.data = Gpio(data_pin, "out")
        
        self.clk.set(1)
        self.data.set(1)

    def start(self):
        self.data.set(0)
        bit_delay()

    def stop(self):
        self.data.set(0)
        bit_delay()
        self.clk.set(1)
        bit_delay()
        self.data.set(1)

    def send(self, data):
        for i in range(0, 8):
            self.clk.set(0)
            bit_delay()
            
            self.data.set(data & 0x01)
            bit_delay()

            self.clk.set(1)
            bit_delay()
            data = data >> 1

        # Wait for ack
        self.clk.set(0)
        self.data.set(1)
        self.data.change_dir("in")
        bit_delay()
        self.clk.set(1)
        ack = self.data.get()

        bit_delay()
        self.clk.set(0)
        self.data.change_dir("out")
        self.data.set(1)
        bit_delay()

        return ack 

from . import common, error

from .common import *
from .error import *

class Gpio:
    def __init__(self, number, direction):
        self.number     = number
        self.direction  = direction
        print(get_export_file())
        fd_export = open(get_export_file(), "w")
        fd_export.write("%d" % number)
        fd_export.close()

        print(get_gpio_direction_file(number))
        fd = open(get_gpio_direction_file(number), "w")
        fd.write("\"%s\"" % direction)
        fd.close()
            
    def set(self, value):
        if self.direction != "out":
            return ERR_WRONG_TYPE

        fd = open(get_gpio_value_file(number), "w")
        if fd < 0:
            return ERR_NO_FILE

        fd.write("%d" % value)
        fd.close()

        return ERR_NO_ERROR

    def get(self):
        if self.direction != "in":
            return ERR_WRONG_TYPE

        fd = open(get_gpio_value_file(number), "w")
        if fd < 0:
            return ERR_NO_FILE

        return fd.read()


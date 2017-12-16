from . import common, error
from .common import *
from .error import *

from time import sleep
import os.path
import os

class Gpio:
    def __init__(self, number, direction):
        self.number     = number
        self.direction  = direction
        # Check if gpio was already exported, then clean
        if os.path.isfile(get_gpio_value_file(number)):
            print("File exists, removing it first")
            self.clean()

        # export gpio
        with open(get_export_file(), "w") as fd_export:
            fd_export.write("%d\n" % number)
            fd_export.flush()

        sleep(1)
        # set direction
        os.system("bash -c \"echo \"out\" > %s\"" % get_gpio_direction_file(number))
        #with open(get_gpio_direction_file(number), "w") as fd:
        #    fd.write("\"%s\"" % direction)
        #    #fd.flush()

    def clean(self):
        with open(get_unexport_file(), "w") as unexport:
            unexport.write("%d\n" % self.number)
            unexport.flush()

    def set(self, value):
        if self.direction != "out":
            return ERR_WRONG_TYPE

        with open(get_gpio_value_file(self.number), "w") as fd:
            fd.write("%d\n" % value)
            #fd.flush()

        return ERR_NO_ERROR

    def get(self):
        if self.direction != "in":
            return ERR_WRONG_TYPE

        with open(get_gpio_value_file(self.number), "r") as fd:
            value = fd.read()

        return value

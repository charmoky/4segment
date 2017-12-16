#!/usr/bin/python

import lib
from time import sleep

gpio17 = lib.Gpio(17, "out")

print (gpio17)

TIME = 0.5

while True:
    sleep (TIME)
    gpio17.set(1)
    sleep (TIME)
    gpio17.set(0)

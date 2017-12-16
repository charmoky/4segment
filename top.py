#!/usr/bin/python

import lib
from time import sleep


#i2c = lib.I2C(17,27)
#i2c.start()
#i2c.send(0x55)
#i2c.stop()

dis = lib.display(17, 27)

segments = [0xff, 0xff, 0xff, 0xff]

dis.set_brightness(7)
dis.set_segments(segments, 0)




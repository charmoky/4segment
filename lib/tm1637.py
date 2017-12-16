from . import i2c_drv, gpio

from .i2c_drv import I2C

COMMAND1 = 0x48
COMMAND2 = 0XC0
COMMAND3 = 0x80

class display:
    def __init__(self, clk_pin, data_pin):
        self.i2c = I2C(clk_pin, data_pin)
        self.brightness = 0

    def set_brightness(self, brightness, on=True):
        if on == True:
            self.brightness = brightness & 0x7 | 0x8
        else:
            self.brightness = 0

    def set_segments(self, segments, pos = 0):
        # display is not lit, no point in updating it
        if self.brightness == 0:
            return 0

        # Send COMMAND1
        self.i2c.start()
        self.i2c.send(COMMAND1)
        self.i2c.stop()

        # Send COMMAND2 and first digit address
        self.i2c.start()
        self.i2c.send(COMMAND2 + (pos & 0x03))

        count = 0
        for seg in segments:
            self.i2c.send(seg)
            count = count + 1
            if count + pos == 4:
                break

        self.i2c.stop
   
        # Send COMMAND3 and brightness
        self.i2c.start()
        self.i2c.send(COMMAND3+(self.brightness & 0xf))
        self.i2c.stop()


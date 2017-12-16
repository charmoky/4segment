
def get_export_file():
    return "/sys/class/gpio/export"

def get_unexport_file():
    return "/sys/class/gpio/unexport"

def get_gpio_direction_file(number):
    filename = "/sys/class/gpio/gpio{}/direction".format(number)
    return filename 

def get_gpio_value_file(number):
    filename = "/sys/class/gpio/gpio{}/value".format(number)
    return filename 


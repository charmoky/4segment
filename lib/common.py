
def get_export_file():
    return "/sys/class/gpio/export"

def get_gpio_direction_file(number):
    filename = "/sys/class/gpio{}/direction".format(number)
    return filename 

def get_gpio_value_file(number):
    filename = "/sys/class/gpio{}/value".format(number)
    return filename 


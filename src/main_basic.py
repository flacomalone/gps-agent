from lib.pytrack import Pytrack
from lib.L76GNSS import L76GNSS
from helpers.led_control import *
import machine, time
import pycom


constant_color("WHITE")
py = Pytrack()
L76 = L76GNSS(pytrack=py)

first_measurement = True
try:
    while 1:
        lat,long = L76.coordinates(debug=False)
        if first_measurement:
            first_measurement = False
            constant_color("GREEN")
        if (lat is None or lat == "") or (long is None or long == ""): # Poor signal
            constant_color("ORANGE")
            continue
        else:
            constant_color("GREEN")

        print(str(lat) + "," + str(long))

except KeyboardInterrupt:
    constant_color("OFF")
except:
    constant_color("MAGENTA")

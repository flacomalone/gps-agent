from lib.pytrack import Pytrack
from lib.L76GNSV4 import L76GNSS
from helpers.led_control import *
import machine, time
import pycom
import gc

latitude = None
longitude = None
altitude = None
HDOP = None

def main():
    py = Pytrack()
    while 1: # Keep on rebooting if it crashes
        try:
            L76 = L76GNSS(pytrack=py)
            fix = False
            L76.setAlwaysOn()
            while 1:
                gc. collect()
                while not fix:
                    fix = L76.get_fix(timeout=1)
                    print("0," + str(L76.gps_message('GGA')['NumberOfSV']) + ",None,None,None,None")
                    gc.collect()

                location = L76.get_location(debug=False)

                latitude = location["latitude"]
                longitude = location["longitude"]
                altitude = location["altitude"]
                HDOP = location["HDOP"]

                if (latitude is None or latitude == "") or (longitude is None or longitude == ""):
                    constant_color("RED")

                if HDOP >= "2.0": # Poor signal
                    constant_color("ORANGE")
                else:
                    constant_color("GREEN")

                # send message as {fix, NumberOfSV, latitude, longitude, altitude, HDOP}
                print(
                str(1 if fix else 0) + ","  +
                str(L76.gps_message('GGA')['NumberOfSV']) + "," +
                str(latitude) + "," +
                str(longitude) + "," +
                str(altitude) + "," +
                str(HDOP))

        except KeyboardInterrupt:
            constant_color("OFF")
            return -1
        except:
            constant_color("MAGENTA")
            time.sleep(1)
            continue

try:
    main()
except Exception as e:
    print("######## EXCEPTION CATCHED ########")
    print("\t", e)
    print("######## REBOOTING NOW ########\n\n")

    time.sleep(0.2)
    import machine
    machine.reset()

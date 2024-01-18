import pycom

colors = {
    "RED": 0x7f0000,
    "GREEN": 0x00FF00,
    "ORANGE": 0xff5100,
    "BLUE": 0x00007f,
    "OFF": 0x000000,
    "WHITE": 0x7f7f7f,
    "MAGENTA": 0x7f007f,
    "CYAN": 0x007f7f,
    "YELLOW": 0x7f5100
}

def heartbeat(color):
    pycom.heartbeat(False)
    pycom.rgbled(colors[color])
    pycom.heartbeat(True)

def constant_color(color):
    pycom.heartbeat(False)
    pycom.rgbled(colors[color])

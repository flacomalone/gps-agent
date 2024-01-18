from network import WLAN
import pycom

def connect():
    wlan=WLAN()
    pycom.wifi_on_boot(True)
    pycom.wifi_mode_on_boot(WLAN.STA)
    pycom.wifi_ssid_sta("RAMBOT_POST_LOVEYOU")
    pycom.wifi_pwd_sta('28532538')
    ifconfig = wlan.ifconfig()
    print("Successfully connected with the following params:")
    print("IP address: ", ifconfig[0], ", subnet mask: ", ifconfig[1], ", gateway: ", ifconfig[2], ", DNS: ", ifconfig[3]) # When connected to RAMBOT_POST_LOVEYOU, IP address uses to be 192.168.0.104

if __name__ == "__main__":
    connect()

#! /bin/python3
###Author: NyboMønster
### Imports fra ESP'en selv
import esp
esp.osdebug(None)
#import webrepl
#webrepl.start()
import network
import time
import ubinascii
import machine
import micropython
import gc
import random
gc.collect()
### Imports fra scripts
from umqttsimple import MQTTClient
import MQlib
#from CreditsInformation import creditsInformationList
##Variables:
cooldownTimer = 5
last_message = 0
counter = 0
message_interval = 5
### Credits:
ssid = 'HotSpot'
password = 'Daniel2901Nybo!'
RPI_IP_Add = '192.168.239.54'
ESP32_IP_Add = '192.168.239.88'
port = 1883
client_id = f'python-mqtt-{2901}'
#client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'Received'
topic_pub = b'measuredData'
topic = "ESP32Data"
### MainCode
#creditsInformationList()
station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass
print('Connection succesful')
print(station.ifconfig())
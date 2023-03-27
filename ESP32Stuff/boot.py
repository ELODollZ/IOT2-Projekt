### Imports
import esp
esp.osdebug(None)
#import webrepl
#webrepl.start()
import network
import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import gc
import random
gc.collect()
#from CreditsInformation import creditsInformationList

##Variables:
cooldownTimer = 5
last_message = 0
counter = 0
message_interval = 5
### Credits:
ssid = 'HotSpot'
password = 'Daniel2901Nybo!'
mqtt_server = '192.168.239.54'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 100)}'
#client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'Received'
topic_pub = b'measuredData'

### MainCode
#creditsInformationList()
station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass
print('Connection succesful')
print(station.ifconfig())
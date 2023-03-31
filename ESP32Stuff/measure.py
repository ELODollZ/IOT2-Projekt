#! /bin/python3
### Author: NyboMønster
###Imports fra system
from machine import Pin
import dht
import random
#import MQlib
###Variables
dhtsensor = dht.DHT11(Pin(25))
#mq135 = MQlib.MQ135(Pin(26))
# Location: KEA Parkerings grønareal
message = ("t, h, s, 55.69194647082459, 12.554169821375735")
message.split(", ", 5)
###MainCode
def measuredData(message):
    #dhtsensor.measure()
    #t = dhtsensor.temperature()
    #print('Temperatur: %3.1f C' %t)
    #h = dhtsensor.humidity()
    #print('Humidit: %3.1f P' %h)
    #cb = mq135.get_corrected_ppm(t, h)
    t = random.randint(1, 100)
    h = random.randint(1, 100)
    cb = random.randint(1, 2000)
    #print('Carbondixiode: %3.1f CB' %cb)
    #print(t,h)
    if (t is not None) and (h is not None) and (cb is not None):
        print('Temperatur: %3.1f C' %t)
        print('Humidit: %3.1f P' %h)
        print('Carbondixiode: %3f Corrected PPM' %cb)
    else:
        print("Invalid sensor readings") 
    Swaped = str(t)
    newmsg = message.replace("t", Swaped)
    Swaped = str(h)
    newmsg = newmsg.replace("h", Swaped)
    if cb > 2500:
        newmsg = newmsg.replace("s", "True")
    else:
        newmsg = newmsg.replace("s", "False")
    print(newmsg)
    message = newmsg
    return message
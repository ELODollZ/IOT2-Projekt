#! /bin/python3
### Author: NyboMønster
###Imports fra system
from machine import Pin
import dht
import MQlib
###Variables
dhtsensor = dht.DHT11(Pin(25))
cb = MQlib.MQ135(Pin(26))
# Location: KEA Parkerings grønareal
msg = ("t, h, s, 55.69194647082459, 12.554169821375735")
msg.split(", ", 5)
#cb = 400.00
###MainCode
def measuredData(msg):
    dhtsensor.measure()
    t = dhtsensor.temperature()
    #print('Temperatur: %3.1f C' %t)
    h = dhtsensor.humidity()
    #print('Humidit: %3.1f P' %h)
    #cb = carbonsensor.carbondixiode()
    #cb = 300.2
    #print('Carbondixiode: %3.1f CB' %cb)
    #print(t,h)
    if (t is not None) and (h is not None) and (cb is not None):
        print('Temperatur: %3.1f C' %t)
        print('Humidit: %3.1f P' %h)
        print('Carbondixiode: %3.1f CB' %cb)
    else:
        print("Invalid sensor readings") 
    Swaped = str(t)
    newmsg = msg.replace("t", Swaped)
    Swaped = str(h)
    newmsg = newmsg.replace("h", Swaped)
    if cb > 500:
        newmsg = newmsg.replace("s", "True")
    else:
        newmsg = newmsg.replace("s", "False")
    print(newmsg)
    msg = newmsg
    return msg
msg = measuredData(msg)
###Imports
from machine import Pin
import dht
###Variables
dhtsensor = dht.DHT11(Pin(25))
carbonsensor = carbonsensor(Pin(24))
msg = ("t, h, s, x, y")
msg.split(", ", 5)
###MainCode
def measuredData(msg):
    dhtsensor.measure()
    t = dhtsensor.temperature()
    #print('Temperatur: %3.1f C' %t)
    h = dhtsensor.humidity()
    #print('Humidit: %3.1f P' %h)
    cb = carbonsensor.carbondixiode()
    #print('Carbondixiode: %3.1f CB' %cb)
    #print(t,h)
    if (t is not None) and (h is not None) and (cp is not None):
        print('Temperatur: %3.1f C' %t)
        print('Humidit: %3.1f P' %h)
        print('Carbondixiode: %3.1f CB' %cb)
    else:
        print("Invalid sensor readings") 
    Swaped = str(t)
    newmsg = msg.replace("t", Swaped)
    Swaped = str(h)
    newmsg = newmsg.replace("h", Swaped)
    if cp > 2500:
        newmsg = newmsg.replace("s", "True")
    else:
        newmsg = newmsg.replace("s", "False")
    #print(newmsg)
    msg = newmsg
    return msg
msg = measuredData(msg)

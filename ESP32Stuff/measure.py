from machine import Pin
import dht

sensor = dht.DHT11(Pin(25))
msg = ("t, h, s, x, y")
msg.split(", ", 5)
def measuredData(msg):
    sensor.measure()
    t = sensor.temperature()
    #print('Temperatur: %3.1f C' %t)
    h = sensor.humidity()
    #print('Humidit: %3.f P' %h)
    #print(t,h)
    if (t is not None) and (h is not None):
        print('Temperatur: %3.1f C' %t)
        print('Humidit: %3.1f P' %h)
    else:
        print("Invalid sensor readings") 
    Swaped = str(t)
    newmsg = msg.replace("t", Swaped)
    Swaped = str(h)
    newmsg = newmsg.replace("h", Swaped)  
    #print(newmsg)
    msg = newmsg
    return msg
msg = measuredData(msg)
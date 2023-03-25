from machine import Pin

sensor = DHT11(Pin(None, Pin.IN, Pin.PULL_UP))
msg = str(b'{0},{0}, {false}, {0000.0000}, {0000.0000}')
def measureData():
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    if ininstance(t, float) and isinstance(h, float):
        msg = (b'{0:3.1f},{1:3.1f}'.format(t,h ))
    else:
        print("Invalid sensor readings")
    
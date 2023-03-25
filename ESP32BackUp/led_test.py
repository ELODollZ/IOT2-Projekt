from machine import Pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(33))

while True:

    try:
        sleep(2)
        sensor.measure()
        temp = sensor.temperature()

        print('Temperatur: %3.1f C' %temp)

        if temp > 25:
            Pin(32, Pin.OUT, value=1)
            sleep(3)
            Pin(32, Pin.OUT, value=0)
        sleep(2)
        sensor.measure
        hum = sensor.humidity()

        print('Humidit: %3.f P' %hum)
        if hum < 25:
            Pin(26, Pin.OUT, value=1)
            sleep(3)
            Pin(26, Pin.OUT, value=0)

    except OSError as e:
        print('Failed to read sensor')

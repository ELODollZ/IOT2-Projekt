from machine import ADC, Pin
test = ADC(Pin(26))
test2 = ADC(Pin(27))
try:
    print(test)

except:
    print(test2)

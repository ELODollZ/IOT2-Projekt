from machine import Pin, ADC
from time import sleep
# MQ135 sensor variabler
RL_VALUE = 10
RO_CLEAN_AIR_FACTOR = 9.83

# Instans af ADC klassen
adc = ADC(Pin(26))
adc.atten(ADC.ATTN_11DB)

# Funktion til at læse MQ135 sensor
def read_mq():
    test = adc.read()
    rs = adc.read() / 4095 * 3.3 / (5.0 - adc.read() / 4095 * 3.3) * RL_VALUE
    ratio = rs / RO_CLEAN_AIR_FACTOR
    co2_ppm = round(1.8 * pow(ratio, -1.769034857))
    print(test)
    return co2_ppm

# Funktion til tråd 1
def sensor_indikator():
    while True:
        co2_ppm = read_mq()
        print(f"CO2 Level: {co2_ppm} ppm")
        sleep(1)
read_mq()
sensor_indikator()

    def get_corrected_ppm(self, temperature, humidity):
        """Returns the ppm of CO2 sensed (assuming only CO2 in the air)
        corrected for temperature/humidity"""
        return self.PARA * math.pow((self.get_corrected_resistance(temperature, humidity)/ self.RZERO), -self.PARB)
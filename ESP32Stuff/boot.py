# This file is executed on every boot (including wake-boot from deepsleep)
### Imports
import esp
import ubinascii
import machine
import micropython
esp.osdebug(None)
#import webrepl
#webrepl.start()
gc.collect()
#from CreditsInformation import creditsInformationList
#import InternetConnector



#! /bin/python3
### Author: NyboMønster
###Imports
import time
###Variables
resualt = ["Year","Mounth","Day","Hour","Minute","Secounds"]
###MainCode
def FunctionTimer(resualt):
    Localtid = time.gmtime()
    print(Localtid)
    return resualt
    
    time.sleep(0.2)
FunctionTimer(resualt)
print(resualt)
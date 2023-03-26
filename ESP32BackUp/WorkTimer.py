import time
resualt = ["Year","Mounth","Day","Hour","Minute","Secounds"]
def FunctionTimer(resualt):
    Localtid = time.gmtime()
    print(Localtid)
    return resualt
    
    time.sleep(0.2)
FunctionTimer(resualt)
print(resualt)
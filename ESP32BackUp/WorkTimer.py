import time
resualt = ["Year","Mounth","Day","Hour","Minute","Secounds"]
def FunctionTimer():
    Localtid = time.localtime()
    resualt = Localtid
    print(resualt)
    
    time.sleep(0.2)
FunctionTimer()
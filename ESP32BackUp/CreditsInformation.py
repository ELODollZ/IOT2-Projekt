##Credits
def creditsInformationList():
    ssid = 'NyboMønsterHotSpot'
    password = 'Daniel2901Nybo!'
    mqtt_server = '192.168.239.55'
    client_id = ubinascii.hexlify(machine.unique_id())
    topic_sub = b'Notification'
    topic_pub = b'measuredData'

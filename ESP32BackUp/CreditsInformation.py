##Credits
def creditsInformationList():
    ssid = 'HotSpot'
    password = 'Daniel2901Nybo!'
    mqtt_server = '192.168.239.54'
    client_id = ubinascii.hexlify(machine.unique_id())
    topic_sub = b'Notification'
    topic_pub = b'measuredData'

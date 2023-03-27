#! Python 3
###Main File
### Imports
import sys
from umqttsimple import MQTTClient
import random
#import graphFile
#import indexFile
#import measure
### StartUps
#measure.measuredData()

### Variables
username = 'RPI'
password = 'public'
Broker = 'broker.RPI.io'
counter = 0

### Main Functions
def sub_cb(topic, msg):
    print((topic, msg))
    if topic == b'Notification' and msg == b'received':
        print('ESP received hello message')

def connect_and_subscribe():
    global client_id, mqtt_server, topic_sub
    client = MQTTClient(client_id, mqtt_server)
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic_sub)
    print('Connected to %s MQTT broker, subribed to %s topic' % (mqtt_server, topic_sub))
    return client
def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()
try:
   client = connect_and_subscribe()
except OSError as e:
   restart_and_reconnect()

### Main Loop
while True():
    try:
        client.check_msg()
        if(time.time() - last_message) > message_interval:
            msg = b'measuredData #%d' % counter
            client.publish(topic_pub, msg)
            last_message = time.time()
            counter += 1
    except OSError as e:
        restart_and_reconnect()

    except TypeError:
        print("Type error somewhere in code, functional")
    except:
        print("Code Error")
    finally:
        print("code done")




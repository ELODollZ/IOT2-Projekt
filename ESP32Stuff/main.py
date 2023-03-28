#! Python 3
###Main File
### Imports
import sys
from umqttsimple import MQTTClient
import random
#import graphFile
#import indexFile
from measure import measuredData, message
import time
### StartUps
#measure.measuredData()

### Variables
username = 'RPI'
password = 'public'
broker = 'broker.RPI.io'
counter = 0

### Main Functions
def sub_cb(topic, msg):
    print((topic, msg))
    if topic_pub == b'Received' and msg == b'received':
        print('ESP Sendt Data')

def connect_and_subscribe():
    global client_id, RPI_IP_Add, topic_pub, topic_sub, topic, port
    client = MQTTClient(client_id, RPI_IP_Add)
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic)
    print('Connected to %s MQTT broker, subribed to %s topic' % (RPI_IP_Add, topic))
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
while True:
    try:
        client.check_msg()
        if(time.time() - last_message) > message_interval:
            msg = message
            client.publish(topic, msg)
            last_message = time.time()
            counter += 1
    except OSError as e:
        restart_and_reconnect()
    except TypeError:
        print("Type error somewhere in code, functional")
    except:
        print("STOP!")
        exit
        time.sleep(2)

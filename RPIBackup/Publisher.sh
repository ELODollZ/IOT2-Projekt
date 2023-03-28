#!/bin/bash

###Variables
messages=""
SentMessages="Messages sent"
###Functions
while :
do
mosquitto_pub	-h	localhost	-t	"ESP32Data"	-m	"Received"
echo SentMessages
done

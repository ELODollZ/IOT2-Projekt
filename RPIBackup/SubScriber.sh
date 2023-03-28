#!/bin/bash

###Variables
messages=""
SentMessages="Messages sent"
###Functions
while :
do
mosquitto_sub	-h	localhost	-t	"ESP32Data"
read messages
echo messages
done


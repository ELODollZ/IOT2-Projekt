#!/bin/bash

###Variables
messages=""
SentMessages="Messages sent"
###Functions
runMosquittoSub () {
	while :
	do
	mosquitto_sub	-h	localhost	-t	"ESP32Data"
	read messages
	echo messages
done
}

runMosquittoPub () {
	while :
	do
	mosquitto_pub	-h	localhost	-t	"ESP32Data"	-m	"Received"
	echo SentMessages
done
}



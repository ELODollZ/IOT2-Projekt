#!/bin/bash

###Variables
messages=""

###Functions
runMosquittoPub () {
	mosquitto_pub -h localhost -t "ESP32Data" -m "Received"
}

runMosquittoSub () {
	mosquitto_sub	-h	localhost	-t	"ESP32Data"	-m	"Received"
}



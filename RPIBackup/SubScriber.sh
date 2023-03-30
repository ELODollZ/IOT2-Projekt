#!/bin/bash

###Variables
messages=""
pastmessages=""
SentMessages="Messages sent"

###Functions
while :
do
echo pastmessages
mosquitto_sub	-h	localhost	-t	"ESP32Data"
read messages
echo messages
IFS=',' read -r -a array <<< messages
$TEMP = array[0]
$HUMD = array[1]
$SMOKE = array[2]
$XLOCATION = array[3]
$YLOCATION = array[4]
pastmessages = messages
echo $TEMP $HUMD $SMOKE $XLOCATION $YLOCATION "IS IT WORKING!"
vores.db = ~/IOT2-Projekt/DataBase/measuredData.db
sqlite3 vores.db "INSERT INTO measuredData(TEMP, HUMD, SMOKE, XLOCATION, YLOCATION) VALUES ($TEMP,$HUMD, "$SMOKE", $XLOCATION, $YLOCATION);"
done


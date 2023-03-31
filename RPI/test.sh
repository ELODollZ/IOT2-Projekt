#!/bin/bash
###Variables
messages=""
pastmessages=""
testmessages="123.4, 123.4, False, 123.4, 123.4"
SentMessages="Messages sent"
TEMP=
HUMD=
SMOKE=
XLOCATION=
YLOCATION=
DataBase="measuredData.db"
###Functions
while :
do
mosquitto_sub	-h	localhost	-t	"ESP32Data"
read $messages
IFS=',' read -r TEMP HUMD SMOKE XLOCATION YLOCATION <<<"${messages}"
echo $TEMP $HUMD $SMOKE $XLOCATION $YLOCATION
echo $messages
sqlite3 measuredData.db "INSERT INTO measuredData(TEMP,HUMD,SMOKE,XLOCATION,YLOCATION) VALUES ($TEMP, $HUMD, '$SMOKE', $XLOCATION, $YLOCATION)"
done

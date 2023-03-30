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
###Functions
while :
do
mosquitto_sub	-h	localhost	-t	"ESP32Data"
read $messages
IFS=',' read -r TEMP HUMD SMOKE XLOCATION YLOCATION <<<"${messages}"
	if [[ "$pastmessages" == "$messages" ]]
	echo $TEMP $HUMD $SMOKE $XLOCATION $YLOCATION
	Database=~/IOT2Projekt/RPI/measuredData.db
	if [[ ! -r "$Database" ]]
		sqlite3 $DataBase "INSERT INTO measuredData(TEMP, HUMD, SMOKE, XLOCATION, YLOCATION) VALUES ($TEMP, $HUMD, "$SMOKE", $XLOCATION, $YLOCATION);"
	then
		echo No DataBase
	fi
then
echo $SentMessages
fi
done


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
function reader {
	mosquitto_sub	-h	localhost	-t	"EPS32Data"
	read $messages
	return $messages
}
while :
do
	mosquitto_sub	-h	localhost	-t	"ESP32Data"
	read $messages
	#reader 
	IFS=',' read -r TEMP HUMD SMOKE XLOCATION YLOCATION <<<"${messages}"
	if [[ "$pastmessages" == "$messages" ]]; then
		echo $TEMP $HUMD $SMOKE $XLOCATION $YLOCATION
		#if [[ measuredData.db == $DataBase ]]; then
			sqlite3 $DataBase "INSERT INTO measuredData(TEMP,HUMD,SMOKE,XLOCATION,YLOCATION) VALUES $($TEMP $HUMD '$SMOKE' $XLOCATION $YLOCATION)"
			#echo "inserted into Database"
		#else
		#	echo "No DataBase found"
		#fi
	else
		echo $SentMessages
		$pastmessages = $messages
	fi
echo "test"
done

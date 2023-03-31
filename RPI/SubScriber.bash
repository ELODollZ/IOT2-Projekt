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
function readerFunction() {
	mosquitto_sub	-h	localhost	-t	"EPS32Data"
	read $messages
		
	return $messages
}
while :
do
	#mosquitto_sub	-h	localhost	-t	"ESP32Data"
	#read $messages
	readerFunction 
	IFS=',' read -r TEMP HUMD SMOKE XLOCATION YLOCATION <<<"${messages}"
	if [[ "$pastmessages" == "$messages" ]]; then
		echo $TEMP $HUMD $SMOKE $XLOCATION $YLOCATION
		if [[ measuredData.db == $DataBase ]]; then
			echo "trying to insert into SQLite3"
			sqlite3 $DataBase "INSERT INTO measuredData(TEMP,HUMD,SMOKE,XLOCATION,YLOCATION) values ($TEMP $HUMD '$SMOKE' $XLOCATION $YLOCATION)"
			echo "inserted into Database"
		else
			echo "No DataBase found"
		fi
	else
		echo $SentMessages
		$pastmessages = $messages
	fi
echo "test"
done

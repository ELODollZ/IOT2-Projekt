<?php
	class MeasuredData extends SQLite3 {
		function __construct(){
		$this->open('measuredData.db')
		}
	}
	$db = new MeasuredData();
	if(!$db) {
		echo $db->lastErrorMsg();
	}
	else {
		echo "Open database successfully\n"
	}
	function InsertIntoHTML() {
   $sql =<<<EOF
      INSERT INTO measuredData(ID, TEMP, HUMD, SMOKE, XLOCATION, YLOCATION);
	VALUES ([ID], [TEMP], [HUMD], [SMOKE], [XLOCATION], [YLOCATION])
EOF;

   $ret = $db->exec($sql);
   if(!$ret) {
	   echo $db->lastErrorMsg();
   }
   else {
	   echo "Records created successfully\n";
   }
   $db->close();
	}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IOT</title>
    <link rel="stylesheet" href="Style.css">
</head>
<body>
    <h1>FOREST SAVER</h1>
    <nav>
        <div class="link">
            <a href="main.html">MAIN</a>
        </div>
        <div class="link">
            <a href="graph.html">GRAPH</a>
        </div>
        <div class="link">
            <a href="table.html">TABLE</a>
        </div>
    </nav>
	<?php
	include('SQLite3Importer.php');
	?>
        <div class="table">
            <div class="table_item">ID</div>
            <div class="table_item">Temperature</div>
            <div class="table_item">Humidity</div>
            <div class="table_item">Co2</div>
            <div class="table_item">Location X</div>
            <div class="table_item">Location Y</div>
            <div class="table_item"><p id="id1"></p></div>
            <div class="table_item"><p id="t1"></p></div>
            <div class="table_item"><p id="h1"></p></div>
            <div class="table_item"><p id="s1"></p></div>
            <div class="table_item"><p id="x1"></p></div>
            <div class="table_item"><p id="y1"></p></div>
        
        </div>
</body>
</html>
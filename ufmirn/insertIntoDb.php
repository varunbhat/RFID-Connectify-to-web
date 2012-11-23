<?php
	include_once("includes/functions.php");
	$con = openDB();
	$values = implode("','",$_GET);
	$keys = array_keys($_GET);
	//$keys = implode('","',$keys);
//	echo $values;
//	echo "<br>";
//	echo $keys;
	$sql = 'INSERT INTO devicelist (status , sliderValue , name , address, pinNumber,slider,command) 
	VALUES ( "'. $_GET[$keys[0]]. 
	'" , "'. $_GET[$keys[1]]. 
	'" , "'. $_GET[$keys[2]]. 
	'" , "'. $_GET[$keys[3]]. 
	'" , "'. $_GET[$keys[4]]. 
	'" , "'. $_GET[$keys[5]].
	'" , "'. $_GET[$keys[6]].'"  )';
	
	mysql_query($sql);
	echo mysql_error();
	echo "<br>";
	echo $sql;
	closeDB($con);
	header('Location: deviceList.php')
?>
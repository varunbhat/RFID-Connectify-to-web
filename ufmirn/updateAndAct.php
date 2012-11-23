<?php
	include_once "includes/functions.php";

	$con = openDB();
	foreach ($_GET as $key => $value)
	{
		echo "checking values:key:"+$key+'\tvalue:'+$value+'\n';
		if ($key=="id")
			$id = $value;
		else
		{
			$query = "UPDATE devicelist SET ". $key."=". $value." WHERE id=". $id;
			mysql_query($query);
			echo mysql_error();
		}	
	}

	if($_GET['status'==1])
	{
		$query = "SELECT command FROM devicelist where id=".$id;
		exec($_GET["command"]);
		
		
	}
	//exec("smsLink.py");
	closeDB($con);
//	header('Location: deviceStatus.php?device='.$id);
?>
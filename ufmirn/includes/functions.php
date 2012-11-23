<?php
	function openDB()
	{
		
		$con = mysql_connect("localhost","root","djptwm241");
		
		if (!$con)
		{
			die('Could not connect: ' . mysql_error());
  		}


		return $con;
	}
	function closeDB($con)
	{
		mysql_close($con);	
	}
?>

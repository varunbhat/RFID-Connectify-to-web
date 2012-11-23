
<?php 
$f = fopen("COM5",'w');
for($i=0;$i<100;$i++)
	fwrite($f , "hello");
	fclose($f);


?>

<?php
header("content-type:text/html;charset=utf-8"); 
if(isset($_COOKIE['id'])&& isset($_COOKIE['time']) && isset($_POST['data']) ){
	$id=$_COOKIE['id'];
	$time=$_COOKIE['time'];
	$data=$_POST['data'];
	$myfile = fopen("log.txt", "w") or die("Unable to open file!");
	$txt = $data.",".$id.",".$time;
	fwrite($myfile, $txt);
	fclose($myfile);
}
?>

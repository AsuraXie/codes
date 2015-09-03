<?php
class singletondemo1{
	private static $instance;
	private function __construct(){
		echo "myinit\n\r";
	}
	public static function getinstance(){
		if(self::$instance==null)
		{
			self::$instance=new singletondemo1();
			echo "init";
		}
		return self::$instance;
	}
}
$b=singletondemo1::getinstance();
var_dump($b);
$c=singletondemo1::getinstance();
var_dump($c);
$d=new singletondemo1();
var_dump($d);
?>

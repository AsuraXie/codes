<?php
namespace simpleMVC;
class  error{
	public static $errors=array();
	 
	public static function add($errno, $errstr, $errfile, $errline){
		 array_push($errors,$errno);
	}
	
	public static function adderror($errno, $errstr, $errfile, $errline){
		echo $errstr;
		die();
	}
}
?>
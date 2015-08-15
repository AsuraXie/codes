<?php
namespace simpleMVC;

class route{
	private static $controller="";
	private static $action="";
	private static $param=array();
	private static $type="GET";
	
	public static function  init(){
		$type=$_SERVER['REQUEST_METHOD'];
		$all_path=$_SERVER["REQUEST_URI"];
		$path=array();
		///剔除特殊情况 ///aa/bbb/cccc////dd//eee,多个‘/’的情况
		$temp="";
		for($i=0;$i<strlen($all_path);)
		{
			if($all_path[$i]=="/"&&$all_path[$i+1]=="/")
				$i++;
			else{ 
				$temp=$temp.$all_path[$i];
				$i++;
			}
		}
		$all_path=$temp;
		$path=explode("/",$all_path);
		switch(count($path))
		{
			case 0:
			self::$controller=default_controller;
			self::$action=default_action;
			break;
			case 1:
			self::$controller=default_controller;
			self::$action=default_action;
			break;
			case 2:
			///   /a/b/c/d,其中第一个为空
			self::$controller=default_controller;
			self::$action=default_action;
			break;
			case 3:
			self::$controller=$path[2];
			self::$action=default_action;
			break;
			case 4:
			self::$controller=$path[2];
			///剔除传递的参数
			$temp_action=explode("?",$path[3]);
			self::$action=$temp_action[0];
			break;
			default:break;
		}
		switch(self::$type)
		{
			case "GET":self::$param=$_GET;break;
			case "POST":self::$param=$_POST;break;
			default:break;
		}
		return;
	}
	
	public static function get($type)
	{
		switch($type)
		{
			case "controller":return self::$controller;
			case "action":return self::$action;
			case "param":return self::$param;
			default :return false;
		}	
	}
}
?>
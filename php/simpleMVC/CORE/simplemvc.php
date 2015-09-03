<?php
///初始化simplemvc的参数处理，加载相应的处理函数
///解析前台传递过来的参数，然后进行解析并放置到相应的位置
namespace simpleMVC;

class simpleMVC{
	private static $version="0.1";
	static public function start(){
		
		require("CORE/route.class.php");
		require("CORE/controller.class.php");
		require("CORE/error.class.php");
		require("CORE/view.class.php");
		require("CORE/db.class.php");
		require("CORE/functions.php");
		require("CORE/model.class.php");
		
		if(!defined("default_debug"))
			defined("default_debug",false);
			
		$error=new error();
		set_error_handler(array($error, 'adderror'));
		db::init();
		/*$mydb=new db();
		var_dump($mydb->query("describe articles"));*/
		route::init();
		$controller=route::get("controller");
		$action=route::get("action");
		define("controller",$controller);
		define("action",$action);
		
		///查找到相应的文件位置，如果存在则执行，不存在则报错.
		///需要对参数进行封装
		
		///加载相应的controller文件，如果存在则加载，不存在则提示错误
		if(self::If_Exist_Class($controller))
		{
			self::Load_Controller($controller);
		}
		else {
			trigger_error("错误，找不到相应的Controller文件");
		}
		
		///加载相应的model文件，如果存在则加载
		if(self::If_Exist_Model($controller))
		{
			self::Load_Model($controller);
		}

		$method = new \ReflectionMethod("simpleMVC\\".$controller."Controller", Route::get("action"));
		if (!$method->isPublic() || $method->isStatic()) {
			trigger_error("错误，调用方法非公开或者是静态");
		}
		$ReqParamsCount=$method->getNumberOfParameters(); // 参数个数
		$ReqParams=$method->getParameters(); // 函数需要的参数对象数组
		$class="simpleMVC\\".$controller."Controller";
		$instance  = new $class;
		if($ReqParamsCount==0)
		{
			///无参数执行
			$method->invoke($instance);
		}
		else
		{
			///参数处理，如果参数不满足则提示错误
			$args=array();
			$allParams=route::get("param");
			foreach($ReqParams as $item)
			{
				if(array_key_exists($item->name,$allParams))
				{
					array_push($args,$allParams[$item->name]);
				}
				else 
				{
					trigger_error("错误，传递的参数错误,需要：".$item->name);
				}
			}
			$method->invokeArgs($instance,$args);
		}
	}
	
	///检查Controller文件是否存在
	static public function If_Exist_Class($name){
		 $results=file_exists(getcwd()."/Controller/".$name."Controller.class.php");
		 return $results;
	}
	///检查Model文件是否存在
	static public function If_Exist_Model($name){
		 $results=file_exists(getcwd()."/Model/".$name."Model.class.php");
		 return $results;
	}
	///加载Controller文件
	static public function Load_Controller($name){
		require("Controller/".$name."Controller.class.php");
	}
	///加载Model文件
	static public function Load_Model($name){
		require("Model/".$name."Model.class.php");
	}
}
?>
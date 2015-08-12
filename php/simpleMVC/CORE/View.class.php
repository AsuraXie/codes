<?php
namespace simpleMVC;
class View{
	public static function Load_html(){
		$results=file_exists(getcwd()."/View/".controller."/".action.".html");
		if(!$results)
			trigger_error("错误，未找到相应的前台模板文件:".controller."/".action.".html");
		return file_get_contents(getcwd()."/View/".controller."/".action.".html");
	}
	
	///先是变量替换，然后是支持for循环，然后支持if语句
	public static function Rendering($data=null){
		$content=self::Load_html();
		if($data!=null)
		{
			
		}
		return $content;
	}
}
?>
<?php
namespace simpleMVC;
class view{
	public static function Load_html($path=null){
		if($path!=null)
		{
			$results=file_exists(getcwd().$path);
			if(!$results)
				trigger_error("错误，未找到相应的前台模板文件:".$path);
			return file_get_contents(getcwd().$path);
		}
		else {
			$results=file_exists(getcwd()."/View/".controller."/".action.".html");
			if(!$results)
				trigger_error("错误，未找到相应的前台模板文件:".controller."/".action.".html");
			return file_get_contents(getcwd()."/View/".controller."/".action.".html");
		}
	}
	
	
	///先是变量替换，然后是支持for循环，然后支持if语句
	///@ViewBag.
	///@require()，将文件放入进行替换
	public static function Rendering($data=null){
		$content=self::Load_html();
		if($data!=null)
		{
			$count=preg_match_all("/@ViewBag[^ <'\"]*/",$content,$matchs);
			if($count>0)
			{
				for($i=0;$i<$count;$i++)
				{
					$t=substr($matchs[0][$i],9,strlen($matchs[0][$i])-9);
					$a=explode(".",$t);
					$temp_data=$data;
					$signal=0;
					for($j=0;$j<count($a);$j++)
					{
						if(array_key_exists($a[$j],$temp_data))
						{
							$temp_data=$temp_data[$a[$j]];
						}
						else {
							$signal=1;
							break;
						}
					}
					if($signal==0)
						$content=str_replace($matchs[0][$i],$temp_data,$content);
				}
			}
		}
		///替换require
		$count=preg_match_all("/@require([^)].*)/",$content,$matchs);
		if($count>0)
		{
			for($i=0;$i<$count;$i++)
			{
				$file=substr($matchs[0][$i],9,strlen($matchs[0][$i])-10);
				$file=str_replace("\"","",$file);
				$file=str_replace("\'","",$file);
				$file=str_replace(" ","",$file);
				$temp=self::Load_html($file);
				$content=str_replace($matchs[0][$i],$temp,$content);
			}
		}	
		return $content;
	}
}
?>
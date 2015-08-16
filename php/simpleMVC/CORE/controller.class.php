<?php
namespace simpleMVC;
class controller{
	
	///将结果渲染成前台模板返回
	public function display($data=null){
		header("Content-Type:text/html;charset=utf8");
		///暂时不写Cache支持
		///header('Cache-control:');
		header("X-Powered-By:simpleMVC");
		echo View::Rendering($data);
	}
	
	///将结果组装成ajax串返回
	public function ajaxReturn($data){
		header("Content-Type:text/html;charset=utf8");
		///暂时不写Cache支持
		///header('Cache-control:');
		header("X-Powered-By:simpleMVC");
		$strs=$this->ajax($data);
		echo $strs;
	}
	
	private function ajax($data){
		if($data==null||$data=="")
			return "";
		$keys=array_keys($data);
		$bracket_start="{";
		$bracket_end="}";
		///only array,键值为0,1,2,3,之类
		if(count($keys)>0&&is_int($keys[0]))
		{
			$bracket_start="[";
			$bracket_end="]";
		}
		$strs=$bracket_start;
		for($i=0;$i<count($keys);$i++)
		{
			///处理数组情况
			if(is_array($data[$keys[$i]]))
			{
				if(!is_int($keys[$i]))
					$strs=$strs."\"".$keys[$i]."\":".$this->ajax($data[$keys[$i]]);
				else $strs=$strs.$this->ajax($data[$keys[$i]]);
			}
			else 
				$strs=$strs."\"".$keys[$i]."\":\"".$data[$keys[$i]]."\"";
			if($i<count($keys)-1)
				$strs=$strs.",";
		}
		$strs=$strs.$bracket_end;
		return $strs;
	}
}
?>
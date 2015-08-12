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
		
	}
}
?>
<?php
namespace simpleMVC;
class indexController extends controller{
	public function index($a,$c){
		$a=M("articles");
		$data=array();
		$data['id']=1;
		$result=$a->delete($data);
		$this->display($data);
	}
}
?>
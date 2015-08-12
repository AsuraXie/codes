<?php
namespace simpleMVC;
class indexController extends controller{
	public function index($a,$c){
		var_dump($a);
		var_dump($c);
		$this->display();
	}
}
?>
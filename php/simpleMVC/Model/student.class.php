<?php
namespace simpleMVC;
class student extends model{
	public $id;
	public $name;
	public $classid;
	public function prikey()
	{
		return "id";
	}
}
?>
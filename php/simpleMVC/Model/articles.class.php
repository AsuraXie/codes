<?php
namespace simpleMVC;
class articles extends model{
	public $id;
	public $title;
	public $body;
	public function prikey()
	{
		return "id";
	}
}
?>
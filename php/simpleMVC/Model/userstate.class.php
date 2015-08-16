<?php
namespace simpleMVC;
class userstate extends model{
	public $id;
	public $state;
	public function prikey()
	{
		return "id";
	}
}
?>
<?php
namespace simpleMVC;
class dept extends model{
	public $deptno;
	public $dname;
	public $loc;
	public function prikey()
	{
		return "deptno";
	}
}
?>
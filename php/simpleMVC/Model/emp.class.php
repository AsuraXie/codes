<?php
namespace simpleMVC;
class emp extends model{
	public $empno;
	public $ename;
	public $job;
	public $mgr;
	public $hiredate;
	public $sal;
	public $comm;
	public $deptno;
	public function prikey()
	{
		return "empno";
	}
}
?>
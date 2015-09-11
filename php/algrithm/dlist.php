<?php
class node{
	public $pre;
	public $data;
	public $next;
}

class mylist{
	private $head;
	public function __construct(){
		$this->head=new node();
		$this->head->pre=&$this->head;
		$this->head->next=&$this->head;
		$this->head->data=0;
		var_dump($this->head);
	}

	public function add($data)
	{
		$temp=$this->head;
		$temp_pre=NULL;
		while($temp->next!=$this->head)
		{
			echo $temp."\n\r";
			$temp=$temp->next;
		}
		$temp_pre=$temp->pre;
		$temp->next=new node();
		$temp=$temp->next;
		$temp->data=$data;
		$temp->next=$this->head;
		$temp->pre=$temp_pre;
	}

	public function show()
	{
		$temp=$this->head;
		while($temp->next!=$this->head)
		{
			echo $temp->data."\n\r";
			$temp=$temp->next;
		}
	}
}

$list=new mylist();
$list->add('a');
$list->add('b');
$list->add('c');
$list->add('f');
$list->show();
?>

<?php
class node{
	public $data;
	public $next;
}

class mylist{
	private $header;
	public function __construct()
	{
		$this->header=new node();
		$this->header->data=0;
		$this->header->next=NULL;
	}
	public function add($data)
	{
 		$temp=$this->header;
		while($temp->next!=NULL)
			$temp=$temp->next;
		$temp->next=new node();
		$temp=$temp->next;
		$temp->data=$data;
		$temp->next=NULL;	
	}
	public function delete($index=-1)
	{
		$temp=$this->header;
		$pre=NULL;
		$i=1;
		if($index>0)
		{
			$pre=$temp;
			$temp=$temp->next;
			while($i<$index&&$temp)
			{
				$temp=$temp->next;
				$pre=$pre->next;
				$i++;
			}
			if($i==$index&&$temp)
			{
				$pre->next=$temp->next;
			}
		}
	}

	public function show()
	{
		$temp=$this->header->next;
		while($temp!=NULL)
		{
			echo $temp->data."\n\r";
			$temp=$temp->next;
		}
	}
	public function search($key)
	{
		$temp=$this->header->next;
		$index=1;
		while($temp)
		{
			if($temp->data==$key)
			{
				echo "posion:".$index."\n\r";	
				break;
			}
			$temp=$temp->next;
			$index++;
		}
		if($temp==NULL)
			echo "Not Found\n\r";

	}
}

$list=new mylist();
$list->add(1);
$list->add('a');
$list->add(3);
$list->add(6);
$list->delete(1);
$list->search(2);
$list->search(3);
$list->show();
?>

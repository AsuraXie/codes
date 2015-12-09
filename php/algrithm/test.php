<?php
class node{
	public $data;
	public $next;
}

$a=new node();
$b=new node();
$a->data=1;
$b->data=2;
$b->next=&$a;
$a->next=&$b;
echo $a->next->data."\n\r";
?>

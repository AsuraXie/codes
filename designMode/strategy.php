<?php
interface filter
{
    function filter($obj);
}

class filterByA
{
    public function filter($item){
        echo "filterByA".$item."\n";
    }
}

class filterByB
{
    public function filter($item){
        echo "filterByB".$item."\n";
    }
}

class Users
{
    private $_users = array();

    public function __construct(){
    }

    public function addItem($item){
        $this->_users[] = $item;
    }

    public function myFilter($filter){
        foreach($this->_users as $item){
            $filter->filter($item);
        }
    }
}

$fA = new filterByA();
$fb = new filterByB();

$myUser = new Users();
$myUser->addItem("nihao");
$myUser->addItem("hello");
$myUser->addItem("world");
$myUser->addItem("hehe");
$myUser->myFilter($fA);
$myUser->myFilter($fb);
?>

<?php

interface Observer
{
    function onChange();
}

interface Observable
{
    function addCustomer();
}

class Observers implements Observable{
    private $allObj;
    public function addCustomer(){
        foreach($this->allObj as $item){
            $item->onChange();
        }
    }

    public function addListener($obser){
        $this->allObj[] = $obser;
    }
}

class Item implements Observer{
    public function onChange(){
        echo "hello world\n";
    }
}

$ob = new Observers();
$a = new Item();
$ob->addListener($a);
$ob->addCustomer();
$b = new Item();
$ob->addListener($b);
$ob->addCustomer();
?>

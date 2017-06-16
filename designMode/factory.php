<?php

interface IUser
{
    function getName();
}

class User implements IUser
{

    public function __construct($id){

    }

    public function getName(){
        return "Asura";
    }
}

class UseFactory{
    public static function Create($id){
        return new User($id);
    }
}

$uo = UseFactory::Create(1);
echo $uo->getName();

?>

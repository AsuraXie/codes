<?php
interface IUser{
    function getName();
}

class User implements IUser
{
    function __construct($id){

    }

    public static function Load($id){
        return new User($id);
    }

    public static function Create(){
        return new User(null);
    }

    public function getName(){
       return "Asura";
    }
}

$uo = User::Create();
echo $uo->getName();
?>

<?php

class DB{
    public static $db ;
    function __construct(){
        if(empty(DB::$db)){
            DB::$db = rand();
        }
        return DB::$db;
    }

    public function getDB(){
        return DB::$db;
    }
}

$a = new db();
echo $a->getDB();
echo "\n";
$b = new db();
echo $b->getDB();
echo "\n";
?>

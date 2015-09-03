<?php
interface car{
	public function run();
}
class audi implements car{
	public function run(){
		echo "audi run\n\r";
	}
}
class byd implements car{
	public function run(){
		echo "byd run\n\r";
	}
}
class car_factory{
	public static function create_car($type){
		switch($type){
			case "audi":return new audi();break;
			case "byd":return new byd();break;
			defaul:break;
		}
	}
}
$factory=new car_factory();
$a=$factory->create_car("audi");
$b=$factory->create_car("byd");
$a->run();
$b->run();
?>

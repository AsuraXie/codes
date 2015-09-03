<?php
interface create_car{
	public static function create_car();
}

class audi_factory implements create_car{
	public static function create_car(){
		return new audi();
	}
}
class benz_factory implements create_car{
	public static function create_car(){
		return new benz();
	}
}

interface run{
	public function run();
}

class audi{
	public function run(){
		echo "audi run\n\r";
	}
}

class benz{
	public function run(){
		echo "benz run\n\r";
	}
}

$a=audi_factory::create_car();
$a->run();
$b=benz_factory::create_car();
$b->run();
?>

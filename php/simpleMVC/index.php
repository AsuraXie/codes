<?php
	define("default_controller","index");
	define("default_action","index");
	define("default_debug",true);
	require('CORE/simplemvc.php');
	simpleMVC\simpleMVC::start();
	/*phpinfo();*/
?>
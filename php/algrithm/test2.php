<?php
class a{
	public function show($data)
	{
		$x=count($data);
		$y=count($data[0]);
		$count=$x*$y;
		for($i=0;$i<$count;$i++)
		{
			echo $data[$i/$x][$i%$y];
			echo " ";
		}
	}
}
$b=new a();
$data=array();
for($i=0;$i<10;$i++)
	for($j=0;$j<10;$j++)
		$data[$i][$j]=$i*$j;
$b->show($data);

?>


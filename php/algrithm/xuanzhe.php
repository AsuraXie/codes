<?php
$data=array('2342','21','42','1','64','23','2421','32','6','72','99');
function shunxu(){
	Global $data;
	for($i=0;$i<count($data);$i++)
	{
		$min=$data[$i];
		$index=$i;
		for($j=$i+1;$j<count($data);$j++)
		if($min>$data[$j])
		{
			$min=$data[$j];
			$index=$j;
		}	
		if($i!=$index)
		{
			$temp=$data[$i];
			$data[$i]=$min;
			$data[$index]=$temp;
		}		
	}
}
shunxu($data);
for($i=0;$i<count($data);$i++)
	echo $data[$i].",";
?>

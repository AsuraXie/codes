<?php
$data=array('2342','21','42','1','64','23','2421','32','6','72','99');
function shunxu(){
	Global $data;
	for($i=0;$i<count($data);$i++)
	{
		for($j=0;$j<count($data)-$i-1;$j++)
		if($data[$j]>$data[$j+1])
		{
			$temp=$data[$j];
			$data[$j]=$data[$j+1];
			$data[$j+1]=$temp;
		}
		for($k=0;$k<count($data);$k++)
			echo $data[$k].",";
		echo "\n";	
	}
}
shunxu($data);
for($i=0;$i<count($data);$i++)
	echo $data[$i].",";
?>

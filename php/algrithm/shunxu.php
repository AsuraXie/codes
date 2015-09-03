<?php
$data=array('2342','21','42','1','64','23','2421','32','6','72','99');
function shunxu(){
	Global $data;
	for($i=0;$i<count($data);$i++)
	{
		for($j=$i;$j<count($data);$j++)
		if($data[$i]>$data[$j])
		{
			$temp=$data[$i];
			$data[$i]=$data[$j];
			$data[$j]=$temp;
		}	
	}
}
shunxu($data);
for($i=0;$i<count($data);$i++)
	echo $data[$i].",";
?>

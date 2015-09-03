<?php
$data=array('2342','21','42','1','64','23','2421','32','6','72','99');
function shunxu(){
	Global $data;
	for($i=0;$i<count($data);$i++)
	{
		$tt=$data[$i];
		for($j=$i-1;$j>=0;$j--)
		{
			if($tt<$data[$j])	
			{
				$temp=$data[$j];
				$data[$j]=$data[$j+1];
				$data[$j+1]=$temp;
			}
			else break;
		}
		$data[$j+1]=$tt;	
	}
}
shunxu($data);
for($i=0;$i<count($data);$i++)
	echo $data[$i].",";
?>

<?php
class a{
	public function xier($data,$start,$step){
		$count=count($data);
		for($i=$start;$i<$count;$i+=$step)
		{
			$min=$data[$i];
			$index=$i;
			for($j=$i;$j<$count;$j+=$step)
			{
				if($min>$data[$j])
				{
					$min=$data[$j];
					$index=$j;
				}	
			}
			$temp=$data[$i];
			$data[$i]=$min;
			$data[$index]=$temp;
		}
		return $data;
	}
}
$b=new a();
$data=array();
for($i=1;$i<count($argv);$i++)
	array_push($data,$argv[$i]);
if(count($argv)==1)
	echo "none input\n\r";
else {
	$data=$b->xier($data,0,3);
	$data=$b->xier($data,1,3);
	$data=$b->xier($data,2,3);
	$data=$b->xier($data,0,1);
	for($i=0;$i<count($argv);$i++)
		echo $data[$i]." ";
	echo "\n\r";
}
?>

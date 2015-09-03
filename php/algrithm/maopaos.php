<?php
class a{
	public function maopao($data){
		$a=0;
		$b=count($data)-1;
		for($i=0;$i<count($data)/2;$i++)
		{
			for($j=$i;$j<count($data)-$i-1;$j++)
			{
				if($data[$j]>$data[$j+1])
				{
					$temp=$data[$j+1];
					$data[$j+1]=$data[$j];
					$data[$j]=$temp;
				}
			}
			for($j=count($data)-$i-2;$j>$i;$j--)
			{
				if($data[$j]<$data[$j-1])
				{
					$temp=$data[$j-1];
					$data[$j-1]=$data[$j];
					$data[$j]=$temp;
				}
			}
		}
		for($k=0;$k<count($data);$k++)
			echo $data[$k]." ";
		echo "\n\r";
	}
}

$data=array();
$b=new a();
for($i=1;$i<count($argv);$i++)
	array_push($data,$argv[$i]);
if(count($argv)==0)
	echo "none input array";
else $b->maopao($data);
?>

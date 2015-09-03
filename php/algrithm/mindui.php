<?php
class a{
	public function adjust($data,$len){
		$i=1;
		$count=$len+1;
		while($i<$count||2*$i<=$count||2*$i+1<=$count)
		{
			$num=0;
			if(2*$i<=$count&&$data[$i-1]>$data[2*$i-1])
			{
				$temp=$data[2*$i-1];
				$data[2*$i-1]=$data[$i-1];
				$data[$i-1]=$temp;
				$num++;
			}
			if(2*$i+1<=$count&&$data[$i-1]>$data[2*$i])
			{
				$temp=$data[2*$i];
				$data[2*$i]=$data[$i-1];
				$data[$i-1]=$temp;
				$num++;
			}
			$i++;
			if($num==0)
				break;
			for($j=0;$j<$count;$j++)
				echo $data[$j]." ";
			echo "\n\r";
		}
		return $data;
	}
	public function swap($data,$len){
		$count=$len;
		$temp=$data[$count];
		$data[$count]=$data[0];
		$data[0]=$temp;
		return $data;
	}
}
$b=new a();
$data=array();
for($i=1;$i<count($argv);$i++)
	array_push($data,$argv[$i]);
if(count($argv)==1)
	echo "none input\n\r";
else{
	for($i=0;$i<count($data);$i++)
	{
		$data=$b->adjust($data,count($data)-1);
		echo "$i temp\n\r";
	}
	for($i=0;$i<count($data);$i++)
	{
		$data=$b->swap($data,count($data)-1-$i);
		$data=$b->adjust($data,count($data)-2-$i);
		echo "-----------------\n\r";
		for($j=0;$j<count($data);$j++)
			echo $data[$j]." ";
		echo "\n\r*****************\n\r";
	}
	for($i=0;$i<count($data);$i++)
		echo $data[$i]." ";	
	echo "\n\r";
}
?>

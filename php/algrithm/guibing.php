<?php
class a{
	public function guibing($data,$a,$b){
		if($a>=$b)
			return ;
		else {
			$mid=floor(($a+$b)/2);
			$this->guibing($data,$a,$mid);
			$this->guibing($data,$mid+1,$b);
			$this->merge($data,$a,$mid,$b);
		}	
	}
	
	public function merge($data,$a,$mid,$b){
		$p=$a;
		$q=$mid+1;
		$temp=array();
		while($p<=$mid&&$q<=$b)
		{
			if($data[$p]<$data[$q])
			{
				array_push($temp,$data[$p]);
				$p++;
			}
			else{
				array_push($temp,$data[$q]);
				$q++;
			}
		}
		while($p<$mid)
		{
			array_push($temp,$data[$p]);
			$p++;
		}
		while($q<$b)
		{
			array_push($temp,$data[$q]);
			$q++;
		}
		for($i=$a;$i<=$b;$i++)
			$data[$i]=$temp[$i-$a];	
	}
}
$data=array();
$b=new a();
for($i=1;$i<count($argv);$i++)
	array_push($data,$argv[$i]);
if(count($data)==1)
	echo "none input";
else {
	$mid=floor(count($data)/2);
	$b->guibing($data,0,$mid);
	$b->guibing($data,$mid+1,count($data)-1);
	$b->merge($data,0,$mid,count($data)-1);
	for($i=0;$i<count($data);$i++)
		echo $data[$i]." ";
	echo "\n\r";
}
?>

<?php
class a{
	public function digui($data,$a,$b,$key)
	{
		if($a>$b||$a<0||$b<0||$a>=count($data)||$b>=count($data))
			return;
		if($a==$b)
		{
			if($data[$a]==$key)
				echo "found in $a";	
		}
		else
		{
			$mid=($a+$b)/2;
			if($data[$mid]==$key)
				echo "found in $mid";	
			else {
				if($data[$mid]>$key)
					$this->digui($data,$a,$mid-1,$key);
				if($data[$mid]<$key)
					$this->digui($data,$mid+1,$b,$key); 
			}
		}
	}
}
$b=new a();
$data=array();
$key=$argv[1];
for($i=2;$i<count($argv);$i++)
	array_push($data,$argv[$i]);
if(count($argv)==1)
	echo "none input";
else $b->digui($data,0,count($data)-1,$key);
?>

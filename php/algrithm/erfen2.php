<?php
class a{
	public function not_digui($data,$key){
		$a=0;
		$b=count($data)-1;
		while($a<=$b)
		{
			$mid=floor(($a+$b)/2);
			if($data[$mid]==$key)
				return $mid;
			else if($data[$mid]>$key)
			{
				$b=$mid-1;
				continue;
			}
			else if($data[$mid]<$key)
			{
				$a=$mid+1;
				continue;
			}
		}
		return -1;
	}
}
$data=array();
for($i=2;$i<count($argv);$i++)
	array_push($data,$argv[$i]);
$key=$argv[1];
$b=new a();
echo $b->not_digui($data,$key);
?>

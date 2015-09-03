<?php
class a{
	public function erfen($data,$key,$a,$b){
		if($a>$b)
			return -1;
		$mid=floor(($a+$b)/2);
		if($data[$mid]==$key&&(($mid-1>=0&&$data[$mid-1]!=$key)||($mid+1<=$b&&$data[$mid+1]!=$key)))
			return $mid;
		else {
			if($data[$mid]>$key)
				return $this->erfen($data,$key,$a,$mid-1);
			else if($data[$mid]<$key)
				return $this->erfen($data,$key,$mid+1,$b);
			else if($data[$mid]==$key)
			{
				$start=$this->erfen($data,$key,$a,$mid-1);
				echo "start:$start\n\r";
				$start=$start>=0?$start:$mid;
				$end=$this->erfen($data,$key,$mid+1,$b);
				echo "end:$end\n\r";
				$end=$end>=0?$end:$mid;
				if($start==$end&&$start>=0)
					return 1;
				else return $end-$start+1;
			}
		}
	}
}
$b=new a();
$data=array();
for($i=2;$i<count($argv);$i++)
	array_push($data,$argv[$i]);
if(count($argv)==2)
	echo "none input\n\r";
else echo $b->erfen($data,$argv[1],0,count($argv)-2);
?>

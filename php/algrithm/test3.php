<?php
class a {
	public function show($data,$n){
		if($n==count($data)-1)
			return true;
		else return ($data[$n]<$data[$n+1])&&($this->show($data,$n+1));	
	}
}
$b=new a();
$data=array();
for($i=1;$i<$argc;$i++)
	array_push($data,$argv[$i]);
if(count($data)==0)
	echo "none input";
echo $b->show($data,1);
?>

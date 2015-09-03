<?php
class  a{
	public function digui($data,$n){
		if($n<0)
			return 0;
		return $data[$n]==1?1:$data[$n]+$this->digui($data,$n-1);
	}
}
$d=new a();
$myarray=array();
for($i=1;$i<count($argv);$i++)
{
	array_push($myarray,$argv[$i]);
}
echo $d->digui($myarray,count($myarray)-1);
?>

<?php
namespace simpleMVC;
class model{	
	///获取主键的名称
	public function prikey(){
		return "";
	}
	
	public function add($data=null){
		if($data==null)
		{
				trigger_error("未传递数组参数给add方法");
				return false;
		}
		$classname=get_class($this);
		$simplename=explode("\\",$classname);
		$class=new $classname;
		$reflect = new \ReflectionClass($class);
		$props   = $reflect->getProperties(\ReflectionProperty::IS_PUBLIC | \ReflectionProperty::IS_PROTECTED);
		$cmd="insert into ";
		if(db::$dbprefix!=null&&db::$dbprefix!="")
			$cmd=$cmd.db::$prefix."_".$simplename[1];
		else $cmd=$cmd.$simplename[1];
		$cmd=$cmd." values(";
		for($i=0;$i<count($props);$i++)
		{
			$name=$props[$i]->getName();
			if(array_key_exists($name,$data))
			{
				$cmd=$cmd."\"".$data[$name]."\"";
				if($i<count($props)-1)
					$cmd=$cmd.",";
			}
		}
		$cmd=$cmd.")";
		$result=db::query($cmd);
		if($result==1)
			return true;
		else return false;
	}
	
	public function update($data){
		$classname=get_class($this);
		$simplename=explode("\\",$classname);
		$class=new $classname;
		$reflect = new \ReflectionClass($class);
		$props   = $reflect->getProperties(\ReflectionProperty::IS_PUBLIC | \ReflectionProperty::IS_PROTECTED);
		$cmd="update ";
		if(db::$dbprefix!=null&&db::$dbprefix!="")
			$cmd=$cmd.db::$dbprefix."_".$simplename[1];
		else $cmd=$cmd.$simplename[1];
		$cmd=$cmd." set ";
		for($i=0;$i<count($props);$i++)
		{
			$name=$props[$i]->getName();
			if(array_key_exists($name,$data)&&$this->prikey()!=$name)
			{
				$cmd=$cmd." ".$name."=\"".$data[$name]."\"";
				if($i<count($props)-1)
					$cmd=$cmd.",";
			}
		}
		$cmd=$cmd." where ".$this->prikey()."=".$data[$this->prikey()];
		$result=db::query($cmd);
		if($result==1)
			return true;
		else return false;
	}
	
	public function where($data){
		$classname=get_class($this);
		$simplename=explode("\\",$classname);
		$class=new $classname;
		$cmd="select * from ";
		if(db::$dbprefix!=null&&db::$dbprefix!="")
			$cmd=$cmd.db::$dbprefix."_".$simplename[1];
		else $cmd=$cmd.$simplename[1];
		$cmd=$cmd." where";
		$keys=array_keys($data);
		for($i=0;$i<count($keys);$i++)
		{
			$cmd=$cmd." ".$keys[$i]."=\"".$data[$keys[$i]]."\"";
			if($i<count($keys)-1)
				$cmd=$cmd." and ";
		}
		$result=db::query($cmd);
		///var_dump($result);
		if($result)
		{
			$result_data=array();
			$index=0;
			$reflect = new \ReflectionClass($class);
			$props   = $reflect->getProperties(\ReflectionProperty::IS_PUBLIC | \ReflectionProperty::IS_PROTECTED);
			for($i=0;$i<count($result);$i++)
			{
				$temp=array();
				for($j=0;$j<count($props);$j++)
				{
					$name=$props[$j]->getName();
					$temp[$name]=$result[$i][$j];
				}
				$result_data[$index]=$temp;
			}
			return $result_data;
		}
		else return false;
	}
	
	public function delete($data){
		$classname=get_class($this);
		$simplename=explode("\\",$classname);
		$class=new $classname;
		$cmd="delete from ";
		if(db::$dbprefix!=null&&db::$dbprefix!="")
			$cmd=$cmd.db::$dbprefix."_".$simplename[1];
		else $cmd=$cmd.$simplename[1];
		$cmd=$cmd." where ";
		$keys=array_keys($data);
		for($i=0;$i<count($keys);$i++)
		{
			$cmd=$cmd." ".$keys[$i]."=\"".$data[$keys[$i]]."\"";
			if($i<count($keys)-1)
				$cmd=$cmd." and ";
		}
		$result=db::query($cmd);
		if($result==1)
		{
			return true;
		}
		else return false;
	}
	
	public function maxid(){
		$classname=get_class($this);
		$simplename=explode("\\",$classname);
		$class=new $classname;
		$cmd="select max(".$this->prikey().") from ";
		if(db::$dbprefix!=null&&db::$dbprefix!="")
			$cmd=$cmd.db::$dbprefix."_".$simplename[1];
		else $cmd=$cmd.$simplename[1];
		echo $cmd;
		$result=db::query($cmd);
		if($result)
		{
			echo $result[0][0];
			return $result[0][0];
		}
		else return false;
	}
}
?>
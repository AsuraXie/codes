<?php
/*
M函数主要用于数据库模型的建立，以便于后期进行数据库的操作，返回一个数据库的对象
I函数主要用于获取前台传递给后台的参数，不论是GET方法的参数还是POST方法的参数.
*/
	function M($tablename){
		///首先检查是否存在相应的Model文件
		///不存在则根据表建立
		///存在则直接new后返回
		if(!default_debug)
		{
			require("/Model/".$tablename.".class.php");
			$result=new $tablename;
			return $result;
		}
		else 
		{
			///前缀合并到表名中
			$fullname="";
			if(simpleMVC\db::$dbprefix!=null&&simpleMVC\db::$dbprefix!="")
				$fullname=simpleMVC\db::$dbprefix."_".$tablename;
			else $fullname=$tablename;
		
			$table_describe=simpleMVC\db::query("describe ".$fullname);
			if($table_describe>=0)
			{
				$modelstr="";
				$modelstr=$modelstr."<?php\n";
				$modelstr=$modelstr."namespace simpleMVC;\n";
				$modelstr=$modelstr."class ".$tablename." extends model{\n";
				$prikey="";
				foreach($table_describe as $item)
				{
					if($item[3]=="PRI")
						$prikey=$item[0];
					$temp="	public $".$item[0].";\n";
					$modelstr=$modelstr.$temp;
				}
				$modelstr=$modelstr."	public function prikey()\n	{\n		return \"".$prikey."\";\n	}\n";
				$modelstr=$modelstr."}\n?>";
				$fp=fopen(getcwd()."/Model/".$tablename.".class.php","w");
				fwrite($fp,$modelstr);
		        fclose($fp);
				require(getcwd()."/Model/".$tablename.".class.php");
				$class="simpleMVC\\".$tablename;
				return new $class;
 			}
			else return false;
		}
	}
	
	function I($name)
	{
		
	}
?>
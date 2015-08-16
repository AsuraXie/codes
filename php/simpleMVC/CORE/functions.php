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
			if (!class_exists("simpleMVC\\".$tablename,false))
			{
				require(getcwd()."/Model/".$tablename.".class.php");
			}
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
				if (!class_exists("simpleMVC\\".$tablename,false))
				{
					require(getcwd()."/Model/".$tablename.".class.php");
				}
				$class="simpleMVC\\".$tablename;
				return new $class;
 			}
			else return false;
		}
	}
	
	function I($name)
	{
		$get=$_GET;
		$post=$_POST;
		if(array_key_exists($name,$get))
			return $get[$name];
		else if(array_key_exists($name,$post))
			return $post[$name];
		else return false;
	}
	
	function CREATE()
	{
		$all_table=simpleMVC\db::query("show tables");
		///创建了Model里面的所有文件
		foreach($all_table as $tablename)
		{
			if(is_array($tablename))
				$tablename=$tablename[0];
			$table=explode("_",$tablename);
			if(count($table)>1)
				$tablename=$table[1];
			M($tablename);
			V($tablename);
			C($tablename);
		}
	}
	
	function V($tablename)
	{
		if (!class_exists("simpleMVC\\".$tablename,false))
		{
			require("Model/".$tablename.".class.php");
		}
		$classname="simpleMVC\\".$tablename;
		$class=new $classname;
		$reflect = new \ReflectionClass($class);
		$props  = $reflect->getProperties(\ReflectionProperty::IS_PUBLIC | \ReflectionProperty::IS_PROTECTED);
		$table_th="";
		$table_tr="";
		$controller=$tablename;
		$prikey=$class->prikey();
		$hidden_prikey="<input name=\"".$prikey."\" hidden=\"hidden\"/>\n";
		for($i=0;$i<count($props);$i++)
		{
			$name=$props[$i]->getName();
			if($name!=$prikey)
			{
				$table_th=$table_th."					<th field=\"".$name."\" width=\"50\">".$name."</th>\n";
				$table_tr=$table_tr."<tr>\n						<td>".$name.":</td>\n<td><input name=\"".$name."\" class=\"easyui-textbox\" required=\"true\"></td>\n					</tr>\n";
			}
		}
		$content=simpleMVC\view::Load_html("/CORE/Template_view.html");
		$count=preg_match_all("/@table_th/",$content,$matchs);
		if($count>0)
		{
			for($i=0;$i<$count;$i++)
			{
				$content=str_replace($matchs[0][$i],$table_th,$content);
			}
		}
		$count=preg_match_all("/@table_tr/",$content,$matchs);
		if($count>0)
		{
			for($i=0;$i<$count;$i++)
			{
				$content=str_replace($matchs[0][$i],$table_tr,$content);
			}
		}
		$count=preg_match_all("/@controller/",$content,$matchs);
		if($count>0)
		{
			for($i=0;$i<$count;$i++)
			{
				$content=str_replace($matchs[0][$i],$controller,$content);
			}
		}
		$count=preg_match_all("/@prikey/",$content,$matchs);
		if($count>0)
		{
			for($i=0;$i<$count;$i++)
			{
				$content=str_replace($matchs[0][$i],$prikey,$content);
			}
		}
		$count=preg_match_all("/@hidden_prikey/",$content,$matchs);
		if($count>0)
		{
			for($i=0;$i<$count;$i++)
			{
				$content=str_replace($matchs[0][$i],$hidden_prikey,$content);
			}
		}
		///变量替换
		if (!file_exists(getcwd()."/View/".$tablename))
			 mkdir (getcwd()."/View/".$tablename); 
		$fp=fopen(getcwd()."/View/".$tablename."/index.html","w");
		fwrite($fp,$content);
		fclose($fp);
	}
	
	function C($tablename)
	{		
		if (!class_exists("simpleMVC\\".$tablename,false))
			require("Model/".$tablename.".class.php");
		$classname="simpleMVC\\".$tablename;
		$class=new $classname;
		$reflect = new \ReflectionClass($class);
		$props  = $reflect->getProperties(\ReflectionProperty::IS_PUBLIC | \ReflectionProperty::IS_PROTECTED);
		$controller=$tablename;
		$prikey=$class->prikey();
		$add="\$data['".$prikey."']=\$temp->maxid()+1;\n";
		$modify="\n";
		for($i=0;$i<count($props);$i++)
		{
			$name=$props[$i]->getName();
			if($name!=$prikey)
				$add=$add."		\$data['".$name."']=I(\"".$name."\");\n";
			$modify=$modify."		\$data['".$name."']=I(\"".$name."\");\n";
		}
		$content=simpleMVC\view::Load_html("/CORE/Template_controller.php");
		$count=preg_match_all("/@add/",$content,$matchs);
		if($count>0)
		{
			for($i=0;$i<$count;$i++)
			{
				$content=str_replace($matchs[0][$i],$add,$content);
			}
		}
		$count=preg_match_all("/@modify/",$content,$matchs);
		if($count>0)
		{
			for($i=0;$i<$count;$i++)
			{
				$content=str_replace($matchs[0][$i],$modify,$content);
			}
		}
		$count=preg_match_all("/@controller/",$content,$matchs);
		if($count>0)
		{
			for($i=0;$i<$count;$i++)
			{
				$content=str_replace($matchs[0][$i],$controller,$content);
			}
		}
		$count=preg_match_all("/@prikey/",$content,$matchs);
		if($count>0)
		{
			for($i=0;$i<$count;$i++)
			{
				$content=str_replace($matchs[0][$i],$prikey,$content);
			}
		}
		///变量替换
		$fp=fopen(getcwd()."/Controller/".$tablename."Controller.class.php","w");
		fwrite($fp,$content);
		fclose($fp);
	}
?>
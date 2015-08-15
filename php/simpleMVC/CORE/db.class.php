<?php
namespace simpleMVC;
	class db{
		public static $dburl;///数据库地址
		public static $dbname;///数据库名
		public static $dbuser;///数据库用户名
		public static $dbpwd;///密码
		public static $dbprefix;///数据库表前缀
		public static $dbcon;///数据库连接
		
		public static function init(){
			if(!file_exists(getcwd()."/View/web.config"))
			{
				trigger_error("错误，未找到web.config配置文件");
				return;
			}
			$doc = new \DOMDocument(); 
			$doc->load(getcwd()."/View/web.config"); //读取xml文件 
			$dbconfig = $doc->getElementsByTagName( "dbconfig" ); //取得humans标签的对象数组 
			foreach( $dbconfig as $item ) 
			{ 
				$dburl_temp = $item->getElementsByTagName( "dburl" ); //取得name的标签的对象数组 
				self::$dburl = $dburl_temp->item(0)->nodeValue; //取得node中的值，如<name> </name> 
				$dbname_temp = $item->getElementsByTagName( "dbname" ); 
				self::$dbname = $dbname_temp->item(0)->nodeValue; 
				$dbuser_temp = $item->getElementsByTagName( "dbuser"); 
				self::$dbuser = $dbuser_temp->item(0)->nodeValue;
				$dbpwd_temp = $item->getElementsByTagName( "dbpwd" ); 
				self::$dbpwd = $dbpwd_temp->item(0)->nodeValue;
				$dbprefix_temp = $item->getElementsByTagName( "dbprefix" ); 
				self::$dbprefix = $dbprefix_temp->item(0)->nodeValue;
			}
		}
	
		///打开连接
		public static function connect(){
			self::$dbcon=new \mysqli(self::$dburl,self::$dbuser,self::$dbpwd,self::$dbname);
			if(!self::$dbcon)
				trigger_error("错误，数据库连接不成功");
		}
		///关闭连接
		public static function close(){
			if(!mysqli_close(self::$dbcon))
				trigger_error("错误，数据库连接关闭错误");
			self::$dbcon=null;
		}
				
		public static function query($cmd){
			$count=0;
			if(self::$dbcon==null)
				self::connect();
			$result=mysqli_query(self::$dbcon,$cmd);
			///如果查询结果不正确，则返回为-1
			if(is_int($result)&&!$result)
			{
				self::close();
				return -1;
			}
			else if(is_bool($result))
			{
				if($result)
				{
					$count=mysqli_affected_rows(self::$dbcon);
					self::close();
					return $count;
				}
				else return $result;
			}
			else $result=$result->fetch_all();
			self::close();
			return $result;
		}
	}
?>
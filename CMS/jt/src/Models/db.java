package Models;

import DB.Results.results;
import javafx.scene.layout.Region;

import javax.xml.parsers.ParserConfigurationException;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

import org.apache.jasper.tagplugins.jstl.core.If;
import org.xml.sax.SAXException;

import sun.management.counter.Variability;

import com.mysql.jdbc.Field;

import Models.config;

import java.io.IOException;
import java.lang.reflect.Modifier;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.text.SimpleDateFormat;
import java.util.Date;


public class db {
	private String dburls="";
	private String dbuser="";
	private String dbpwd="";
	
	public db(){
		///解析config.xml文件，获取数据库基本配置信息
		try {
			SAXParserFactory parserFactory=SAXParserFactory.newInstance();
			SAXParser parser;
			parser = parserFactory.newSAXParser();
			config dbconfig=new config();
			parser.parse("/home/asura/codes/CMS/jt/WebContent/WEB-INF/config.xml",dbconfig);
			dburls=dbconfig.getDburls();
			dbpwd=dbconfig.getDbpwd();
			dbuser=dbconfig.getDbuser();
			
		} catch (ParserConfigurationException e) {
			e.printStackTrace();
		} catch (SAXException e) {
			e.printStackTrace();
		} catch (IOException e){
			e.printStackTrace();
		}
	}
	
	///新增操作
	public results add(Object myobj) throws Exception {
			Connection conn=null;
			Class.forName("com.mysql.jdbc.Driver");
			conn=DriverManager.getConnection(dburls,dbuser,dbpwd);
			String cmd="";
			modelsbasic myobj2=(modelsbasic)myobj;
			///对象反射获取属性
			Class temp=myobj.getClass();
			java.lang.reflect.Field[] fields=temp.getDeclaredFields();
			///CMD拼装
			cmd=cmd+"insert into "+temp.getSimpleName()+" values(";
			for(int i=0;i<fields.length;i++)
			{
				cmd=cmd+"\""+myobj2.Get(fields[i].getName())+"\"";
				if(i==fields.length-1)
					cmd=cmd+")";
				else cmd=cmd+",";
			}
			PreparedStatement ps = conn.prepareStatement(cmd);
			results myResults=new results();
			myResults.success=ps.executeUpdate()>0?true:false;
			if(myResults.success)
				myResults.message="新增成功";
			else myResults.message="新增失败";
			return myResults;
	}
	
	///修改操作
	public results modify(Object myobj) throws Exception{
		Connection conn=null;
		Class.forName("com.mysql.jdbc.Driver");
		modelsbasic myobj2=(modelsbasic)myobj;
		conn=DriverManager.getConnection(dburls,dbuser,dbpwd);
		String cmd="";
		String priString="";
		String [] prikey=((modelsbasic)myobj).GetPrimaryKey().split(",");
		///反射获取类属性
		Class temp=myobj.getClass();
		java.lang.reflect.Field[] fields=temp.getDeclaredFields();
		
		///CMD封装
		cmd=cmd+"update "+temp.getSimpleName()+" set ";
		for(int i=0;i<fields.length;i++)
		{
			///拼接主键
			for (String tt:prikey) {
				if(tt.equals(fields[i].getName())){
					if(priString.equals(""))
						priString=tt+"=\""+myobj2.Get(tt)+"\"";
					else priString=" and "+tt+"=\""+myobj2.Get(tt)+"\"";
				}
				else {
					cmd=cmd+fields[i].getName()+"=\""+myobj2.Get(fields[i].getName())+"\" ";
					if(i!=fields.length-1)
						cmd=cmd+",";
				}
			}
		}
		cmd=cmd+" where "+priString;
		
		PreparedStatement ps = conn.prepareStatement(cmd);
		results myResults=new results();
		if(ps.executeUpdate()>0)
			myResults.success=true;
		else myResults.success=false;
		if(myResults.success)
			myResults.message="修改操作成功";
		else myResults.message="修改操作失败";
		return myResults;
		
	}
	
	///删除操作
	public results remove (Object myobj) throws Exception{
		Connection conn=null;
		Class.forName("com.mysql.jdbc.Driver");
		conn=DriverManager.getConnection(dburls,dbuser,dbpwd);
		String cmd="";
		String priString="";
		String [] prikey=((modelsbasic)myobj).GetPrimaryKey().split(",");
		///反射获取类属性
		Class temp=myobj.getClass();
		modelsbasic ttModelsbasic=(modelsbasic)myobj;
		java.lang.reflect.Field[] fields=temp.getDeclaredFields();
		
		///封装cmd
		cmd=cmd+"delete from "+temp.getSimpleName();
		for(int i=0;i<fields.length;i++)
		{
			///拼接prikey
			for (String tt:prikey) {
				if(tt.equals(fields[i].getName())){
					if(priString.equals(""))
						priString=tt+"='"+ttModelsbasic.Get(fields[i].getName())+"'";
					else priString=" and "+tt+"='"+ttModelsbasic.Get(fields[i].getName())+"'";
				}
			}
		}
		cmd=cmd+" where "+priString;
		PreparedStatement ps = conn.prepareStatement(cmd);
		results myResults=new results();
		if(ps.executeUpdate()>0)
			myResults.success=true;
		else myResults.success=false;
		if(myResults.success)
			myResults.message="删除操作成功";
		else myResults.message="删除操作失败";
		return myResults;
	}
	
	///查询
	public results query(String cmd){
		try{
			Connection conn=null;
			Class.forName("com.mysql.jdbc.Driver");
			conn=DriverManager.getConnection(dburls,dbuser,dbpwd);
			PreparedStatement ps = conn.prepareStatement(cmd);
			results myresult=new results();
			myresult.success=ps.execute();
			if(myresult.success)
				myresult.message="查询操作成功";
			else myresult.message="查询操作失败";
			return myresult;
		}
		catch(Exception e){
			System.out.println(e.getMessage());
			return new results(false,e.getMessage());
		}
	}
	
	///获取所有的数据
	public results getall(Object target,String cmd,Integer page,Integer rows){
		try{
			Integer total=0;
			Integer SkipCount=0;
			Integer index=0;
			Integer RowIndex=0;
			
			Connection conn=null;
			ResultSet rs=null;
			Class.forName("com.mysql.jdbc.Driver");
			conn=DriverManager.getConnection(dburls,dbuser,dbpwd);
			PreparedStatement ps = conn.prepareStatement(cmd);
			rs=ps.executeQuery();
			results myresult=new results();
			myresult.success=true;
			SkipCount=(page-1)*rows;
			
			myresult.message="";
			///对象放射获取属性
			Class temp=target.getClass();
			java.lang.reflect.Field[] fields=temp.getDeclaredFields();
			
			while(rs.next())
			{
				if(index<SkipCount)
				{
					index++;
					continue;
				}
				///json数据拼装
				myresult.message=myresult.message+"{";
				for(int i=0;i<fields.length;i++)
				{
					myresult.message=myresult.message+"\""+fields[i].getName()+"\"";
					myresult.message=myresult.message+":\""+rs.getString(fields[i].getName())+"\"";
					if(i!=fields.length-1)
						myresult.message=myresult.message+",";
				}
				myresult.message=myresult.message+"}";
				RowIndex++;
				if(rows!=0)
				{
					if(!rs.isLast()&&RowIndex<rows&&rows!=0)
						myresult.message=myresult.message+",";
				}
				else if(!rs.isLast())
					myresult.message=myresult.message+",";
				if(RowIndex>=rows&&rows!=0)
					break;
			}
			rs.last();
			total=rs.getRow();
			myresult.message="{\"total\":\""+total+"\",\"rows\":["+myresult.message;
			myresult.message=myresult.message+"]}";
			return myresult;
		}
		catch(Exception e){
			System.out.println(e.getMessage());
			return new results(false,e.getMessage());
		}
	}
	
	///获取主键14位时间+4位随机数
	public String GetPrikey(){
		String temp="";
		SimpleDateFormat df = new SimpleDateFormat("yyyyMMddHHmmss");
		temp=df.format(new Date());
		temp=temp+String.valueOf((int)(Math.random()*8999+1000));
		return temp;
	}
}
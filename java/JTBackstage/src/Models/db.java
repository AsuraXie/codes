package Models;

import DB.Results.results;
import javafx.scene.layout.Region;

import javax.xml.parsers.ParserConfigurationException;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

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


public class db {
	private String dburls="";
	private String dbuser="";
	private String dbpwd="";
	
	public db(){
		///解析config.xml，从中获取数据库连接的基本配置信息
		try {
			SAXParserFactory parserFactory=SAXParserFactory.newInstance();
			SAXParser parser;
			parser = parserFactory.newSAXParser();
			config dbconfig=new config();
			parser.parse("H:/javaproject/JTBackstage/WebContent/WEB-INF/config.xml",dbconfig);
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
			///类型反射获取属性值
			Class temp=myobj.getClass();
			java.lang.reflect.Field[] fields=temp.getDeclaredFields();
			///CMD数据拼装
			cmd=cmd+"insert into "+temp.getName()+" values(";
			for(int i=0;i<fields.length;i++)
			{
				cmd=cmd+fields[i].toString();
				if(i==fields.length-1)
					cmd=cmd+")";
				else cmd=cmd+",";
			}
			System.out.println(cmd);
			
			PreparedStatement ps = conn.prepareStatement(cmd);
			results myResults=new results();
			myResults.success=ps.execute();
			if(myResults.success)
				myResults.message="新增执行成功";
			else myResults.message="新增执行失败";
			return myResults;
	}
	
	///修改操作
	public results modify(Object myobj) throws Exception{
		Connection conn=null;
		Class.forName("com.mysql.jdbc.Driver");
		conn=DriverManager.getConnection(dburls,dbuser,dbpwd);
		String cmd="";
		String priString="";
		String [] prikey=((modelsbasic)myobj).GetPrimaryKey().split(",");
		///类型反射获取属性值
		Class temp=myobj.getClass();
		java.lang.reflect.Field[] fields=temp.getDeclaredFields();
		
		
		///CMD数据拼装
		cmd=cmd+"update "+temp.getName()+" set ";
		for(int i=0;i<fields.length;i++)
		{
			cmd=cmd+fields[i].getName()+"='"+fields[i].toString()+"' ";
			if(i==fields.length-1)
				cmd=cmd+")";
			else cmd=cmd+",";
			for (String tt:prikey) {
				if(tt.equals(fields[i].getName())){
					if(priString.equals(""))
						priString=tt+"="+fields[i].toString();
					else priString=" and "+tt+"="+fields[i].toString();
				}
			}
		}
		cmd=cmd+" where "+priString;
		
		System.out.println(cmd);
		
		PreparedStatement ps = conn.prepareStatement(cmd);
		results myResults=new results();
		myResults.success=ps.execute();
		if(myResults.success)
			myResults.message="修改执行成功";
		else myResults.message="修改执行失败";
		return myResults;
		
	}
	
	public results query(String cmd){
		try{
			Connection conn=null;
			Class.forName("com.mysql.jdbc.Driver");
			conn=DriverManager.getConnection(dburls,dbuser,dbpwd);
			PreparedStatement ps = conn.prepareStatement(cmd);
			results myresult=new results();
			myresult.success=ps.execute();
			if(myresult.success)
				myresult.message="删除执行成功";
			else myresult.message="删除执行失败";
			return myresult;
		}
		catch(Exception e){
			System.out.println(e.getMessage());
			return new results(false,e.getMessage());
		}
	}
	
	public results getall(Object target,String cmd){
		try{
			Connection conn=null;
			ResultSet rs=null;
			Class.forName("com.mysql.jdbc.Driver");
			conn=DriverManager.getConnection(dburls,dbuser,dbpwd);
			PreparedStatement ps = conn.prepareStatement(cmd);
			rs=ps.executeQuery();
			results myresult=new results();
			myresult.success=true;
			myresult.message="[";
			///类型反射获取属性值
			Class temp=target.getClass();
			java.lang.reflect.Field[] fields=temp.getDeclaredFields();
			while(rs.next())
			{
				///json数据拼装
				myresult.message=myresult.message+"{";
				for(int i=0;i<fields.length;i++)
				{
					myresult.message=myresult.message+"'"+fields[i].getName()+"'";
					myresult.message=myresult.message+":'"+rs.getString(fields[i].getName())+"'";
				}
				myresult.message=myresult.message+"}";
				if(!rs.isLast())
					myresult.message=myresult.message+",";
			}
			myresult.message=myresult.message+"]";
			return myresult;
		}
		catch(Exception e){
			System.out.println(e.getMessage());
			return new results(false,e.getMessage());
		}
	}
}

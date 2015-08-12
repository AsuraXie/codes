package Work;
import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Iterator;
import java.util.List;
import java.util.Random;

import javax.servlet.ServletException;
import javax.servlet.ServletInputStream;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.catalina.filters.AddDefaultCharsetFilter;

import com.sun.org.apache.bcel.internal.generic.NEW;
import com.sun.org.apache.xerces.internal.impl.xs.identity.Selector.Matcher;

import DB.Results.results;

import java.sql.*;

import Models.db;
import Models.usergroup;
import File.xlxfile;
import sun.net.www.content.text.plain;
public class group extends HttpServlet{
	
	db mydb=new db();
	///新增操作
	public String add(HttpServletRequest req){
		usergroup myModel=new usergroup();
		try {
			String tempID=req.getParameter("id");
			if(tempID!="")
				return modify(req);
		} catch (Exception e) {
			return modify(req);
		}
		myModel.id=mydb.GetPrikey();
		myModel.name=req.getParameter("name");
		myModel.bz=req.getParameter("bz");
		results myResults=new results();
		try {
			myResults=mydb.add(myModel);
			return myResults.toString();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			myResults.message=e.getMessage();
			myResults.success=false;
			return myResults.toString();
		}
	}
	
	///修改操作
	public String modify(HttpServletRequest req){
		usergroup myModel=new usergroup();
		myModel.id=req.getParameter("id");
		myModel.name=req.getParameter("name");
		myModel.bz=req.getParameter("bz");
		results myResults=new results();
		try {
			myResults=mydb.modify(myModel);
			return myResults.toString();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			myResults.message=e.getMessage();
			myResults.success=false;
			return myResults.toString();
		}
	}
	
	///删除操作
	public String delete(HttpServletRequest req){
		usergroup myModel=new usergroup();
		myModel.id=req.getParameter("id");
		myModel.name=req.getParameter("name");
		myModel.bz=req.getParameter("bz");
		results myResults=new results();
		try {
			myResults=mydb.remove(myModel);
			return myResults.toString();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			myResults.message=e.getMessage();
			myResults.success=false;
			
			return myResults.toString();
		}
	}

	///获取所有内容
	public String GetAllData(HttpServletRequest req){
		usergroup myModel=new usergroup();
		int page=0;
		int rows=0;
		try {
			page=Integer.getInteger(req.getParameter("page"));
			rows=Integer.getInteger(req.getParameter("rows"));
		} catch (Exception e) {
			// TODO: handle exception
		}
		results myResults=new results();
		try {
			myResults=mydb.getall(myModel,"select * from usergroup", page, rows);
			return myResults.message.toString();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			myResults.message=e.getMessage();
			myResults.success=false;
			e.printStackTrace();
			return myResults.toString();
		}
	}
	@Override
	protected void service(HttpServletRequest req, HttpServletResponse resp)
			throws ServletException, IOException {
		// TODO Auto-generated method stub
		String[] path=req.getPathInfo().split("/");
		List<String> allpath = new ArrayList<String>();
		for(int i=0;i<path.length;i++)
			if(!path[i].equals(""))
				allpath.add(path[i]);
		///返回固定的编码格式,以便浏览器能够解析
		resp.setContentType("text/html; charset=utf-8");
		PrintWriter out=resp.getWriter();
		switch(allpath.get(0))
		{
			case "add":out.print(add(req));break;
			case "modify":out.print(modify(req));break;
			case "delete":out.print(delete(req));break;
			case "GetAllData":out.print(GetAllData(req));break;
			default:results myresult=new results();
			myresult.message="未知操作，参数错误";
			out.print(myresult);
				break;
		}
	}

}

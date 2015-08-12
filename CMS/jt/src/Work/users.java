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

import com.sun.org.apache.bcel.internal.generic.NEW;
import com.sun.org.apache.xerces.internal.impl.xs.identity.Selector.Matcher;

import DB.Results.results;

import java.sql.*;

import Models.db;
import Models.userinfos;
import File.xlxfile;
import sun.net.www.content.text.plain;

public class users extends HttpServlet {

	/**
	 * 
	 */
	private static final long serialVersionUID = 7917156173425166581L;
	private db mydb=new db();
	
	public String add(HttpServletRequest req) {
		
		userinfos temp=new userinfos();
		results myresult=new results();
		temp.name=req.getParameter("name");
		temp.login_name=req.getParameter("login_name");
		temp.pwd=req.getParameter("pwd");
		temp.email=req.getParameter("email");
		temp.address=req.getParameter("address");
		temp.telphone=req.getParameter("telphone");
		temp.miaoshu=req.getParameter("miaoshu");
		temp.group=req.getParameter("group");
		temp.id=mydb.GetPrikey();
		try {
			myresult=mydb.add(temp);
			return myresult.toString();
		} catch (Exception e) {
			e.printStackTrace();
			
			return e.getMessage();
		}
	}

	///保存照片
	public String SavePNG(HttpServletRequest req) throws IOException{
		return xlxfile.savefile(req);
	}
	
	///修改内容
	public String modify(HttpServletRequest req) {
		userinfos temp=new userinfos();
		results myresult=new results();
		try {
			myresult=mydb.modify(temp);
			return myresult.toString();
		} catch (Exception e) {
			e.printStackTrace();
			return e.getMessage();
		}
	}


	public String delete(HttpServletRequest req) {
		userinfos temp=new userinfos();
		results myresult=new results();
		temp.id=req.getParameter("id");
		try {
			myresult=mydb.remove(temp);
			return myresult.toString();
		} catch (Exception e) {
			e.printStackTrace();
			return e.getMessage();
		}
	}


	public String GetAllData(HttpServletRequest req){
		try{
			int rows=0;
			int page=0;
			rows=Integer.parseInt(req.getParameter("rows"));
			page=Integer.parseInt(req.getParameter("page"));
			return mydb.getall(new userinfos(),"select * from userinfos",page,rows).message;
		}
		catch(Exception e){
			System.out.println(e.getMessage());
			return e.getMessage();
		}
	}
	
	@Override
	protected void service(HttpServletRequest req, HttpServletResponse resp)
			throws ServletException, IOException {
		
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
			case "AcceptFile":out.print(SavePNG(req));break;
			case "GetAllData":out.print(GetAllData(req));break;
			default:results myresult=new results();
			myresult.message="未知操作，参数错误";
			out.print(myresult);
				break;
		}
	}

}

package Work;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import DB.Results.results;

import java.sql.*;

import Models.db;
import Models.userinfos;

public class users extends HttpServlet {

	/**
	 * 
	 */
	private static final long serialVersionUID = 7917156173425166581L;
	private db mydb=new db();
	public String add(HttpServletRequest req) {
		results myresult=new results();
		
		return null;
	}


	public String modify(HttpServletRequest req) {
		return null;
	}


	public String delete(HttpServletRequest req) {
		return null;
	}


	public String GetAllData(HttpServletRequest req){
		try{
			return mydb.getall(new userinfos(),"select * from userinfo where id='4'").toString();
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

		PrintWriter out=resp.getWriter();
		
		switch(allpath.get(0))
		{
			case "add":out.print(add(req));break;
			case "modify":out.print(modify(req));break;
			case "delete":out.print(delete(req));break;
			case "GetAllData":out.print(GetAllData(req));break;
			default:results myresult=new results();
			myresult.success=false;
			myresult.message="路径错误，无效路径";
			out.print(myresult);
				break;
		}
	}

}

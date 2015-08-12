package Denglu;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import DB.Results.results;

public class Denglu extends HttpServlet {

	/**
	 * 
	 */
	private static final long serialVersionUID = 4733272479778594688L;

	@Override
	protected void service(HttpServletRequest req, HttpServletResponse resp)
			throws ServletException, IOException {
		String[] path=req.getPathInfo().split("/");
		List<String> allpath = new ArrayList<String>();
		for(int i=0;i<path.length;i++)
			if(!path[i].equals(""))
				allpath.add(path[i]);
		for(int i=0;i<allpath.size();i++)
			System.out.println(allpath.get(i));

		PrintWriter out=resp.getWriter();
		
		switch(allpath.get(0))
		{
			case "login":out.print(login(req));break;
			case "logout":out.print(logout(req));break;
			default:results myresult=new results();
			myresult.success=false;
			myresult.message="路径错误，无效路径";
			out.print(myresult);
				break;
		}
	}

	private results login(HttpServletRequest req){
		results myresult=new results();
		String loginname=req.getParameter("loginname");   
		String pwd=req.getParameter("pwd");   
		String code=req.getParameter("code");   
		if(loginname.equals("")||pwd.equals("")||code.equals(""))
		{
			myresult.success=false;
			myresult.message="请填写完用户名,密码,验证码等";
			return myresult;
		}
		else{
			
		}
		return myresult;
	}
	
	private results logout(HttpServletRequest req){
		results myresult=new results();
		return myresult;
	}
}

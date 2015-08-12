package Models;

import org.eclipse.jdt.internal.compiler.ast.ThisReference;

public class usergroup extends modelsbasic{
	public String id;
	public String name;
	public String bz;
	@Override
	public String GetPrimaryKey() {
		// TODO Auto-generated method stub
		return "id";
	}
	@Override
	public String Get(String xname) {
		Object temp;
		switch(xname){
		case "id":temp=this.id;break;
		case "name":temp=this.name;break;
		case "bz":temp=this.bz;break;
		default:temp= "";break;
		}
		if(temp==null)
			return "";
		else return temp.toString();
	}
}

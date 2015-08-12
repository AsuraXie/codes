package Models;

import org.eclipse.jdt.internal.compiler.ast.ThisReference;

import com.sun.javafx.scene.layout.region.Margins.Converter;

public class userinfos extends modelsbasic{
	public String id;
	public String name;
	public String login_name;
	public String pwd;
	public String email;
	public String address;
	public String telphone;
	public String miaoshu;
	public String group;
	public String image;
	@Override
	public String GetPrimaryKey() {
		return "id";
	}
	@Override
	public String Get(String xname) {
		Object temp;
		switch(xname){
		case "id":temp=this.id;break;
		case "name":temp=this.name;break;
		case "login_name":temp=this.login_name;break;
		case "pwd":temp=this.pwd;break;
		case "email":temp=this.email;break;
		case "address":temp= this.address;break;
		case "telphone":temp= this.telphone;break;
		case "miaoshu":temp= this.miaoshu;break;
		case "group":temp= this.group;break;
		case "image":temp=this.image;break;
		default:temp= "";break;
		}
		if(temp==null)
			return "";
		else return temp.toString();
	}
}

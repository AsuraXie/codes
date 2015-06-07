package Models;

public class userinfos extends modelsbasic{
	public int id;
	public String name;
	public String login_name;
	public String pwd;
	public String email;
	public String address;
	public String telphone;
	public String miaoshu;
	public String group;
	@Override
	public String GetPrimaryKey() {
		return "id";
	}
}

package DB.Results;

import java.io.UnsupportedEncodingException;

public class results {
	
	public results(){
		this.success=false;
		this.message="undefined";
	}
	
	@Override
	public String toString() {
		String temp="";
		temp=temp+"{\"success\":"+this.success.toString()+",";
		if(this.message.charAt(0)=='[')
			temp=temp+"\"message\":"+this.message+"}";
		else temp=temp+"\"message\":\""+this.message+"\"}";
		temp=temp+"";
		try {
			String aaString=new String(temp.getBytes("utf-8"),"utf-8");
			return aaString;
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return temp;
	}

	public results(Boolean suc,String msg){
		this.success=suc;
		this.message=msg;
	}
	public Boolean success;
	public String message;
}

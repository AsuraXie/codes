package DB.Results;

import java.util.ArrayList;

import javax.swing.text.html.HTMLDocument.Iterator;

import com.sun.xml.internal.bind.v2.schemagen.xmlschema.List;

public class Json {
	
	public String name;
	public Object value;
	
	public static String OtoJ(){
		String temp=new String();
		
		return "";
	}
	public static Json JtoO(){
		Json resultJson=new Json();
		return resultJson;
	}
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getValue() {
		return value.toString();
	}
	public void setValue(Object value) {
		this.value = value;
	}
	
	@Override
	public String toString() {
		if(value.getClass().getName().contains("String"))
			return (String)value;
		else if(value.getClass().getName().contains("List"))
		{
			ArrayList<Json> lists=(ArrayList<Json>)value;
			java.util.Iterator<Json>  myIterator=lists.iterator();
			String results="";
			while(myIterator.hasNext())
			{
				results=results+myIterator.next().toString()+",";
			}
			return results;
		}
		else 
			return ((Json)value).toString();
	}
}

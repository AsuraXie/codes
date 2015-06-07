package Models;
import java.io.IOException;

import javax.xml.parsers.ParserConfigurationException;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;

import com.sun.org.apache.xml.internal.resolver.readers.SAXParserHandler;

public class config extends DefaultHandler {
	
	private String dburls;
	private String dbuser;
	private String dbpwd;
	private String node;
	
	public config(){
		super();
	}
	
	@Override
	public void startDocument() throws SAXException {
		// TODO Auto-generated method stub
		super.startDocument();
	}

	@Override
	public void endDocument() throws SAXException {
		// TODO Auto-generated method stub
		super.endDocument();
	}

	@Override
	public void startElement(String uri, String localName, String qName,
			Attributes attributes) throws SAXException {
		if(qName.equals("dburl"))
			node="dburl";
		else if(qName.equals("dbuser"))
			node="dbuser";
		else if(qName.equals("dbpwd"))
			node="dbpwd";
		else node="";
		super.startElement(uri, localName, qName, attributes);
	}

	@Override
	public void endElement(String uri, String localName, String qName)
			throws SAXException {
		// TODO Auto-generated method stub
		super.endElement(uri, localName, qName);
	}

	@Override
	public void characters(char[] ch, int start, int length)
			throws SAXException {
		String temp="";
		if(node!=null){
			switch (node) {                      
			case "dburl":
				temp = new String(ch,  start, length); 
				dburls=temp;
				node="";
				break;
			case "dbuser":
				temp = new String(ch, start, length); 
				dbuser=temp;
				node="";
				break;
			case "dbpwd":
				temp = new String(ch, start, length); 
				dbpwd=temp;
				node="";
				break;
			default:
				break;
			}
		}
		super.characters(ch, start, length);
	}

	public String getDburls() {
		return dburls;
	}

	public String getDbuser() {
		return dbuser;
	}

	public String getDbpwd() {
		return dbpwd;
	}
	
	public String getall(){
		return dburls+"   "+dburls+"    "+dbpwd;
	}
}

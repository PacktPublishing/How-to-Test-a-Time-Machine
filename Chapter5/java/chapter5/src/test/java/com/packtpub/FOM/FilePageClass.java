package com.packtpub.FOM;
import org.openqa.selenium.By; 
import org.openqa.selenium.WebElement; 
import org.openqa.selenium.WebDriver; 
import org.w3c.dom.Document; 
import org.w3c.dom.Element;
import org.xml.sax.SAXException;

import javax.xml.parsers.DocumentBuilder;  
import javax.xml.parsers.DocumentBuilderFactory;  
import javax.xml.parsers.ParserConfigurationException;  
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;


public class FilePageClass {
    private WebDriver driver;
    private static final Path objectsPath = Paths.get(System.getProperty("user.dir"), "src", "test", "java", "com", "packtpub", "FOM" , "Elements.xml");
    private Document objDoc; 
    public FilePageClass(WebDriver driver) throws ParserConfigurationException, SAXException, IOException { 
        this.driver = driver; 
        DocumentBuilderFactory documentBuilderFactory = DocumentBuilderFactory.newInstance();
        DocumentBuilder docBuilder = documentBuilderFactory.newDocumentBuilder();  
        objDoc = docBuilder.parse(objectsPath.toFile()); 
    /* Letting purposedly the exception flow, as if something goes wrong, we want to kno before trying to find the element */ 
} 

public WebElement getSearchElement() {		 
    Element searchElement = (Element) objDoc.getElementsByTagName("search").item(0); /* we should only get one element, otherwise we are doing something wrong. We can add some checkers and exceptions to validate this.*/ 
    By byId = By.id(searchElement.getAttribute("id"));
    return driver.findElement(byId); 
} 

// Note – we could have a small method to add text to search element 
}

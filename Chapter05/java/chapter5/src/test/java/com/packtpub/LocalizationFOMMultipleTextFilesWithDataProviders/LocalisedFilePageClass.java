package com.packtpub.LocalizationFOMMultipleTextFilesWithDataProviders;
import org.openqa.selenium.By; 
import org.openqa.selenium.WebElement; 
import org.openqa.selenium.WebDriver; 
import org.w3c.dom.Document; 
import org.w3c.dom.Element;

import javax.xml.parsers.DocumentBuilder;  
import javax.xml.parsers.DocumentBuilderFactory;

import java.nio.file.Path;
import java.nio.file.Paths;

public class LocalisedFilePageClass {
    private WebDriver driver;
    private static final Path objectsPath_EN_UK = Paths.get(System.getProperty("user.dir"), "src", "test", "java", "com", "packtpub", "LocalizationFOMMultipleTextFilesWithDataProviders" , "ElementsEN_UK.xml");
    private static final Path objectsPath_ES_ES = Paths.get(System.getProperty("user.dir"), "src", "test", "java", "com", "packtpub", "LocalizationFOMMultipleTextFilesWithDataProviders" , "ElementsES_ES.xml");
    private Document objDoc;
    
    public LocalisedFilePageClass(WebDriver driver, String locale) throws Exception { 
        this.driver = driver; 
        DocumentBuilderFactory documentBuilderFactory = DocumentBuilderFactory.newInstance();
        DocumentBuilder docBuilder = documentBuilderFactory.newDocumentBuilder();  
        switch(locale) {
            case "ES_ES":
                objDoc = docBuilder.parse(objectsPath_ES_ES.toFile());
                break;
            default:
                objDoc = docBuilder.parse(objectsPath_EN_UK.toFile());
                break;
        } /*
           * Letting purposedly the exception flow, as if something goes wrong, we want to
           * know before trying to find the element
           */
    }

public WebElement getSearchElement() {		 
    Element searchElement = (Element) objDoc.getElementsByTagName("search").item(0); /* we should only get one element, otherwise we are doing something wrong. We can add some checkers and exceptions to validate this.*/ 
    By byId = By.id(searchElement.getAttribute("id"));
    return driver.findElement(byId); 
} 

/* ... we could handle this from the module side or add a method like this to get the different strings from the object: */ 
    public String getSearchElementExpectedText() { 
        Element searchElement = (Element) objDoc.getElementsByTagName("search").item(0);
        return searchElement.getAttribute("text");
    } 

    public String getSearchElementActualText() {
        return getSearchElement().getAttribute("placeholder");
    } 

} 

package com.packtpub; 
import org.w3c.dom.Document; 
import org.w3c.dom.Element; 
import javax.xml.parsers.DocumentBuilder;  
import javax.xml.parsers.DocumentBuilderFactory;  
import javax.xml.parsers.ParserConfigurationException;  
import java.io.File; 
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
// for second example
import java.util.Map;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class CreateAutomation {

    private StringBuilder toPrintInPageClass;
    private Document objDoc;
    WebDriver driver = new ChromeDriver();

    public CreateAutomation(String objectsPath, String className, String packageName) throws ParserConfigurationException, SAXException, IOException {
        DocumentBuilderFactory documentBuilderFactory = DocumentBuilderFactory.newInstance();
        DocumentBuilder docBuilder = documentBuilderFactory.newDocumentBuilder();
        toPrintInPageClass.append("package " + packageName + ";\n");
        toPrintInPageClass.append("import org.openqa.selenium.By;\n"); 
        toPrintInPageClass.append("import org.openqa.selenium.WebElement;\n"); 
        toPrintInPageClass.append("import org.openqa.selenium.WebDriver;\n");
        toPrintInPageClass.append("\npublic class " + className + " {"); 
        objDoc = docBuilder.parse(new File(objectsPath)); 
        NodeList nodeList = objDoc.getChildNodes();
        for (int i = 0; i < nodeList.getLength(); i++){
            Element o = (Element) nodeList.item(i);
            switch(o.getAttribute("type")) {
                case "input": // define to try by all
                    toPrintInPageClass.append("WebElement " + o.getAttribute("name") + " = driver.findElement(By." + o.getAttribute("selector")+ "(\"" + o.getAttribute("id") + "\"));\n");
                    toPrintInPageClass.append("void " + o.getAttribute("name") + "_type(string toType) { \n\t" + o.getAttribute("name") + ".sendKeys(toType); \n}");
                    break;
                case "button":
                    toPrintInPageClass.append("WebElement " + o.getAttribute("name") + " = driver.findElement(By." + o.getAttribute("selector")+ "(\"" + o.getAttribute("id") + "\"));\n"); 
                    toPrintInPageClass.append("void " + o.getAttribute("name") + "_click() { \n\t" + o.getAttribute("name") + ".click(); \n}"); 
                    break;
                case "textBox":
                    toPrintInPageClass.append("WebElement " + o.getAttribute("name") + " = driver.findElement(By." + o.getAttribute("selector")+ "(\"" + o.getAttribute("id") + "\"));\n"); 
                    toPrintInPageClass.append("bool " + o.getAttribute("name") + "_verifyText(string text) { \n\treturn " + o.getAttribute("name") + ".text().equals(text); \n}"); 
                    break;
            }
        }
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(new File(className + ".java"))); 
        bufferedWriter.write(toPrintInPageClass.toString());
        bufferedWriter.flush(); 
        bufferedWriter.close(); 
    }

    public WebElement findElement(Map<String, String> locatorValue) { 

        WebElement found = null; 
        for (String key : locatorValue.keySet()) {
            found = findElementHelper(key, locatorValue.get(key));
            if(found!=null)
                return found;
        } 
        return found;

    } 
        
    public WebElement findElementHelper(String locator, String value) {
        switch(locator){ 
            case "id": 
                return driver.findElement(By.id(value)); 
            case "name": 
                return driver.findElement(By.name(value));
        // ...
        }
        return null; 
    }
}
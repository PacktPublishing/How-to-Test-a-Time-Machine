package com.packtpub.Inheritance;
import java.time.Duration;

import org.openqa.selenium.By; 
import org.openqa.selenium.WebElement; 
import org.openqa.selenium.WebDriver; 
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;

public class BasePage {

    protected WebDriver driver;
    protected WebDriverWait waitForElement;

    public BasePage (WebDriver driver) { 
        this.driver = driver;
        this.waitForElement = new WebDriverWait(driver, Duration.ofSeconds(60), Duration.ofSeconds(10));
    }
    
    public WebElement getSearchElement() { 
        By byIDSearch = By.id("__BVID__336"); // This id might vary a bit, please check is valid when running
        this.waitForElement.until(ExpectedConditions.presenceOfElementLocated(byIDSearch));
        return this.driver.findElement(byIDSearch);
    }
    
    public void waitForPartialLink(String bookName) {
        By partialLinkText = By.partialLinkText(bookName);
        this.waitForElement.until(ExpectedConditions.presenceOfElementLocated(partialLinkText));
    }
    
    public WebElement getBookPartialLink(String bookName) {
        this.waitForPartialLink(bookName);
        return this.driver.findElement(By.partialLinkText(bookName)); 
    } 
    // Note – add all the menu elements
}
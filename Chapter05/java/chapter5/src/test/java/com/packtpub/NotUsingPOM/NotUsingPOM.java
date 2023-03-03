package com.packtpub.NotUsingPOM;
import org.testng.annotations.Test; 
import org.testng.annotations.BeforeMethod; 
import org.testng.annotations.AfterMethod; 
import org.testng.Assert; 
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.chrome.ChromeDriver;

/**** Tests login feature */ 
public class NotUsingPOM { 
    private final String bookName = "Testing time machines"; 
    private WebDriver driver;
    
    @BeforeMethod
    public void beforeMethod() {
       this.driver = new ChromeDriver();
       this.driver.get("http://www.packtpub.com"); 
    }

    @AfterMethod
    public void afterMethod() {
        this.driver.close();
        this.driver.quit();
    }

    @Test
    public void testSearch() {
        //When 
        String Url = driver.getCurrentUrl(); 
        // find search data
        By byIDSearch = By.id("__BVID__336"); // This id might vary a bit, please check is valid when running
        WebDriverWait waitForElement = new WebDriverWait( this.driver, Duration.ofSeconds(60), Duration.ofSeconds(10));
        waitForElement.until(ExpectedConditions.presenceOfElementLocated(byIDSearch));
        this.driver.findElement(byIDSearch).sendKeys(bookName);
        this.driver.findElement(byIDSearch).sendKeys(Keys.ENTER);
        By partialLinkText = By.partialLinkText("achine"); // use bookname after book is publishing
        waitForElement.until(ExpectedConditions.presenceOfElementLocated(partialLinkText));
        // verify url has changed 
        Assert.assertNotEquals(Url,  this.driver.getCurrentUrl());
    } 

    @Test
    public void testAddElementToCart() { 
        // find search data
        By byIDSearch = By.id("__BVID__336");
        WebDriverWait waitForElement = new WebDriverWait( this.driver, Duration.ofSeconds(60), Duration.ofSeconds(10));
        waitForElement.until(ExpectedConditions.presenceOfElementLocated(byIDSearch));
        this.driver.findElement(byIDSearch).sendKeys(bookName); 
        this.driver.findElement(byIDSearch).sendKeys(Keys.ENTER);
        By partialLinkText = By.partialLinkText("achine"); // use bookname after book is publishing
        waitForElement.until(ExpectedConditions.presenceOfElementLocated(partialLinkText));
        this.driver.findElement(partialLinkText).click(); 
        // ... click add to cart , click cart, verify element is there 
    }
}
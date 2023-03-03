package com.packtpub.UsingPOM; 
import org.testng.annotations.Test; 
import org.testng.annotations.BeforeMethod; 
import org.testng.annotations.AfterMethod; 
import org.testng.Assert;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.WebElement;

public class TestPageClass {

  PageClass page;
  private final String bookName = "Testing time machines";
  private WebDriver driver;

  @BeforeMethod
  public void beforeMethod() {
    this.driver = new ChromeDriver();
    this.driver.get("http://www.packtpub.com");
    this.page = new PageClass(driver);
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
     WebElement searchElement = page.getSearchElement();
     searchElement.sendKeys(bookName);
     searchElement.sendKeys(Keys.ENTER);
     page.waitForPartialLink("achine");
     // verify url has changed 
     Assert.assertNotEquals(Url,  this.driver.getCurrentUrl());
  } 

  @Test
  public void testAddElementToCart() {
    page.getSearchElement().sendKeys(bookName);
    page.getSearchElement().sendKeys(Keys.ENTER);
    page.getBookPartialLink("achine").click();
    // ... click add to cart , click cart, verify element is there 
  } 
} 
package com.packtpub.FOM; 
import org.testng.annotations.Test; 
import org.testng.annotations.BeforeMethod; 
import org.testng.annotations.AfterMethod; 
import org.testng.Assert;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.WebElement;
import java.time.Duration;

public class TestPageClass {

  FilePageClass page;
  private final String bookName = "Testing time machines";
  private WebDriver driver;

  @BeforeMethod
  public void beforeMethod() throws Exception {
    this.driver = new ChromeDriver();
    this.driver.get("http://www.packtpub.com");
    this.page = new FilePageClass(driver);
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
     WebDriverWait waitForElement = new WebDriverWait(driver, Duration.ofSeconds(60), Duration.ofSeconds(10));
     waitForElement.until(ExpectedConditions.urlContains("search"));
     // verify url has changed 
     Assert.assertNotEquals(Url,  this.driver.getCurrentUrl());
  } 
} 
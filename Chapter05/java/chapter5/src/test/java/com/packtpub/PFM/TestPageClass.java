package com.packtpub.PFM; 
import org.testng.annotations.Test; 
import org.testng.annotations.BeforeMethod; 
import org.testng.annotations.AfterMethod; 
import org.testng.Assert;

import java.time.Duration;

import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.By;

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
  public void testSearch() throws InterruptedException {
     //When 
     String Url = driver.getCurrentUrl();
     WebDriverWait waitForElement = new WebDriverWait(driver, Duration.ofSeconds(60), Duration.ofSeconds(10));
     // find search data
     page.getSearchElement().sendKeys(this.bookName);
     page.getSearchElement().sendKeys(Keys.ENTER);
     waitForElement.until(ExpectedConditions.visibilityOfElementLocated(By.partialLinkText("achine")));
     // verify url has changed 
     Assert.assertNotEquals(Url,  this.driver.getCurrentUrl());
  } 

  @Test
  public void testAddElementToCart() {
    page.getSearchElement().sendKeys(this.bookName);
    page.getSearchElement().sendKeys(Keys.ENTER);
    // ... click add to cart , click cart, verify element is there 
  } 
} 
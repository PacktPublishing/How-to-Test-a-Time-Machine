package com.packtpub.Inheritance; 
import org.testng.annotations.Test; 
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.Assert;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.WebElement;

public class TestCaseClass {
    MainPage page;
    WebDriver driver;
    private final String bookName = "Testing time machines";

    @BeforeClass
    public void initPages() {
        this.driver = new ChromeDriver();
        this.page = new MainPage(this.driver);
    }

    @BeforeMethod
    public void beforeMethod() {
        this.driver.get("http://www.packtpub.com");
    }

    @AfterClass
    public void afterMethod() {
        this.driver.close();
        this.driver.quit();
    }

    @Test 
    public void testSearch() { 
        String Url = driver.getCurrentUrl(); 
        // find search data
        WebElement searchElement = page.getSearchElement();
        searchElement.sendKeys(this.bookName);
        searchElement.sendKeys(Keys.ENTER);
        page.waitForPartialLink("achine");
        // verify url has changed 
        Assert.assertNotEquals(Url,  this.driver.getCurrentUrl());
  }

  @Test 
  public void testTrial() {
      String Url = driver.getCurrentUrl();
      // click trial element
      WebElement trialElement = page.getFreeTrialElement();
      trialElement.click();
      // verify navigation
      page.waitTrialLoaded();
      Assert.assertNotEquals(Url,  this.driver.getCurrentUrl());
    }

  // ...  
}

package com.packtpub.Localization;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

public class TestCaseClass {
    PageClass page;
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
  
    @Test(dataProvider="searchLocale", dataProviderClass = LocaleDataProvider.class) 
    public void testSearchText(String expectedText) { 
      WebElement element = page.getSearchElement();
      Assert.assertTrue(element.getAttribute("placeholder").contains(expectedText), "expected " + expectedText); 
    }// Note - you WILL see this test failing the secont time around, as the website does not have spanish locales...
}
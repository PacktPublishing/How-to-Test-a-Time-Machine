package com.packtpub.LocalizationFOMMultipleTextFilesWithDataProviders;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

public class TestCaseClass { 

    LocalisedFilePageClass page; 
    private WebDriver driver;

    @BeforeMethod
    public void beforeMethod() throws Exception {
      this.driver = new ChromeDriver();
      this.driver.get("http://www.packtpub.com");
    }

    @AfterMethod
    public void afterMethod() {
      this.driver.close();
      this.driver.quit();
     }
  
    @Test(dataProvider="localeDataProvider", dataProviderClass= LocaleDataProvider.class) 
    public void testSearchText(String locale) throws Exception { 
      page = new LocalisedFilePageClass(driver, locale);
      Assert.assertTrue(page.getSearchElementActualText().contains(page.getSearchElementExpectedText())); 
    } 
}
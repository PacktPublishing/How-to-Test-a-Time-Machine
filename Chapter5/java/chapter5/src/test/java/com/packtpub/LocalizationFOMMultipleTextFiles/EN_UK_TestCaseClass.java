package com.packtpub.LocalizationFOMMultipleTextFiles;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

public class EN_UK_TestCaseClass { 

    LocalisedFilePageClass page; 
    private WebDriver driver;

    @BeforeMethod
    public void beforeMethod() throws Exception {
      this.driver = new ChromeDriver();
      this.driver.get("http://www.packtpub.com");
      this.page = new LocalisedFilePageClass(driver, "EN_UK");
    }

    @AfterMethod
    public void afterMethod() {
      this.driver.close();
      this.driver.quit();
     }
  
    @Test 
    public void testSearchText() { 
        Assert.assertTrue(page.getSearchElementActualText().contains(page.getSearchElementExpectedText()));
    }// ...  
}
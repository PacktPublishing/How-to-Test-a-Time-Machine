package com.packtpub.PFM; 
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class PageClass { 

@FindBy(id="__BVID__336")
WebElement searchElement;

public PageClass(WebDriver driver) {
    PageFactory.initElements(driver, this);
} 

public WebElement getSearchElement() { 
    return searchElement;
}
//
} 
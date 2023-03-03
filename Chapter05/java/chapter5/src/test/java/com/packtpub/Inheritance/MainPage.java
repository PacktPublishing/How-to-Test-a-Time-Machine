package com.packtpub.Inheritance;
import org.openqa.selenium.By; 
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.WebDriver; 

public class MainPage extends BasePage {
    String freeTrial = "freeTrial";
    String tryForFreeText = "TRY";

    public MainPage(WebDriver webdriver) { 
        super(webdriver); 
    } 

    public WebElement getFreeTrialElement() { 
        By partialLink = By.partialLinkText(tryForFreeText);
        this.waitForElement.until(ExpectedConditions.presenceOfElementLocated(partialLink));
        return driver.findElement(partialLink); 
    }

    public void waitTrialLoaded() {
        waitForElement.until(ExpectedConditions.urlContains(freeTrial));
    }

    /* Note, there are many other ways of doing this
     * One such would be to validate here the url, comparing with one by parameter
     * or checking that it contains freeTrial
     * then we can assertTrue from TestCaseClass
     * We can also check both things.
     * For continuity, we are implementing it as above.
     */
}

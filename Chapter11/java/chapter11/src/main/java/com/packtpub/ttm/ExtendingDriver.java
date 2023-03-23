package com.packtpub.ttm;
import org.openqa.selenium.remote.RemoteWebDriver;

public class ExtendingDriver extends RemoteWebDriver {
    public void sayHi(){
        System.out.println("hi");
    }
}

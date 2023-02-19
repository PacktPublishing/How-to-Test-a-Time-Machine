package com.packtpub.Localization;
import org.testng.annotations.DataProvider; 
    
public class LocaleDataProvider {   
    
    @DataProvider(name = "searchLocale") 
    public static Object[][] retrieveSeachLocale() { 
            return new Object[][] { { "Search" }, { "busqueda" } }; 
        } 
    } 
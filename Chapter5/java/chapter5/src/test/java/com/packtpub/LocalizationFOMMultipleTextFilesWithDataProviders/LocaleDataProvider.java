package com.packtpub.LocalizationFOMMultipleTextFilesWithDataProviders;

import org.testng.annotations.DataProvider; 

public class LocaleDataProvider {   
    @DataProvider(name = "localeDataProvider") 
    public static Object[][] retrieveData() { 
        return new Object[][] { { "EN_UK" }, { "ES_ES" } }; 
    } 
} 

from selenium import webdriver
import unittest

''' define your providerURL and providerCapabilities
 (you will need an account with such provider for 
 this code to run)''' 
providerURL = ""
providerCapabilities = ""

driver1 = webdriver.Remote(providerURL, providerCapabilities)

# note that this connection might take longer than a local one 

driver1.get("chaturl") 

# Assuming login done for user 1, in some way or having different URLs for different chats 

driver2 = webdriver.Remote(providerURL, providerCapabilities) 

# Assuming login done for user 2 

driver1.find_element_by_id("textBox").send_keys("hello user 2") 

assertTrue(driver2.find_element_by_id("chatBox").getText().contains("hello user 2")) 

driver1.quit() 

driver2.quit() 
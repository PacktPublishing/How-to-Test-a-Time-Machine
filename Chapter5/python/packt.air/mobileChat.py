# -*- encoding=utf8 -*- 

__author__ = "Noemi" 

from airtest.core.api import * 
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

# class setup omitted too, code could be run without it
# Note this code is not meant to run

android2 = connect_device("Android://127.0.0.1:5037/SERIAL1") 

poco2 = AndroidUiautomationPoco(android2) 

android1 = connect_device("Android://127.0.0.1:5037/SERIAL2") 

poco1 = AndroidUiautomationPoco(android1) 

chat_page = chat_page() # ne

chat_page.doLogin(poco1) # login omitted from example 

chat_page.doLoing(poco2) 
chat_page.touch_start_chat_with(poco1, "user2") 

chat_page.set_text(poco1, "hi from user1") 

assertTrue(chat_page.get_text(poco2, "hi from user1")) 

chat_page.set_text(poco2, "hi from user2") 

assertTrue(chat_page.get_text(poco1, "hi from user2")) 
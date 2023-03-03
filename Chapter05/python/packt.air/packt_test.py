# -*- encoding=utf8 -*- 

__author__ = "Noemi" 


from selenium import webdriver
from airtest_selenium.proxy import WebChrome
from selenium.webdriver.common.action_chains import ActionChains

from airtest.core.api import * 
import os 
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,path)
path = os.path.join(path, 'packt_pages') 
sys.path.insert(0, path)

from packt_page import *

driver = WebChrome()
driver.get("http://packtpub.com/") 
'''
page = packt_page()

page.click_search(driver)
ActionChains(driver).send_keys("Testing time machines").perform()
'''

### comment previous to check model
#'''
from model import *
model = model()
model.click_search(driver)
ActionChains(driver).send_keys("Testing time machines").perform()
# '''
### 
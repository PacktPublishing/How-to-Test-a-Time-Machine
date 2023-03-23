"""This module serves to demonstrate multiple drivers creation"""
# pip install Appium-Python-Client
# pip install selenium

from selenium import webdriver
from appium import webdriver as wd

capabilities = {"BROWSER_NAME": "Android",
                "VERSION": "4.4.2",
                "deviceName": "Emulator",
                "platformName":"Android"}

driver1 = webdriver.Chrome()
driver2 = webdriver.Remote("https://127.0.0.1:4723/wd/hub", capabilities)

driver1.get("https://www.packtpub.com/")
driver2.get("https://www.packtpub.com/")

#driver2 inits action on the app
#driver1 confirms action on the browser

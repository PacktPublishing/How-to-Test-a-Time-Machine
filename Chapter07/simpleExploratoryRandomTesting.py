from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import sys
import random
import nodeClass
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains

class simpleExploratoryRandomTesting:
    def __init__(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver=webdriver.Chrome(ChromeDriverManager().install())
        self.topLevel=5
        node = nodeClass.nodeClass("https://www.packtpub.com/free-learning")
        driver.get(node.url)
        self.simpleExploratoryRandomTesting(node, [], 0, driver)
        driver.close()
    def simpleExploratoryRandomTesting(self,node, visited, currentLevel, driver):
        currentLevel= currentLevel + 1
        if (currentLevel>=self.topLevel):
            sys.exit("Max visits reached")
        visited.append(node)
        if (requests.get(node.url).status_code < 200 or requests.get(node.url).status_code >= 300):
            sys.exit("Error on the url " + node.url)
        # get all actions first time in the node
        try:
            driver.find_element(By.XPATH,'//a[@class="accept_all"]').click()
        except:
            print("no cookies found")
        if (node.count == -1):
            node.count=0
            for a in driver.find_elements(By.TAG_NAME,'a'):
                # we only get the ones with packtput.com on them to be new nodes
                if("packtpub.com" in node.url):
                    node.count=node.count+1
                    href = a.get_attribute('href')
                    node.actions[href]=a.get_dom_attribute('href')
        # iterate through the actions randomly and visit them
        while node.count > 0:
            # randomly get one – then append to acted and remove a count
            suburl = self.randomGetOne(node.actions, node.acted)
            node.acted.append(suburl)
            node.count = node.count - 1
            # create a new subnode
            subnode = nodeClass.nodeClass(suburl)
            if (subnode not in visited):
                print("Visiting " + subnode.url + ". . .")
                self.tryClick('//a[@href="'+node.actions[suburl]+'"]', driver, driver)
                driver.implicitly_wait(5)
                # repeat the process for this subnode
                self.simpleExploratoryRandomTesting(subnode, visited, currentLevel, driver)
                # close any opened tabs
                if len(driver.window_handles) > 1:
                    driver.close()
            # verify we havent reached the max of actions taken, so the algorithm does not take too long
            if (currentLevel>=self.topLevel):
                sys.exit("Max visits reached")
            print("going back. . .")
            driver.get(node.url)
            driver.implicitly_wait(5)

    def randomGetOne(self,actions, acted):
        keys = list(actions.keys())
        count = len(keys)
        ransel = random.randrange(count)
        suburl = keys[ransel]
        while suburl in acted:
            ransel = random.randrange(count)
            suburl = keys[ransel]
        return suburl
    
    def tryClick(self, xpath, driver, parent):
        print("Trying to click " + str(xpath))
        element = parent.find_element(By.XPATH,xpath)
        try:
            ActionChains(parent).move_to_element(element).perform()
            element.click()
        except:
            driver.execute_script("arguments[0].click();", element)

simpleExploratoryRandomTesting()
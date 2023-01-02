'''
    Example of a random web crawler
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import sys
import random
import node_class
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains

class SimpleExploratoryRandomTesting:
    """ Class to explore a website up to "topLevel" levels of depth"""
    def __init__(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = webdriver.Chrome(ChromeDriverManager().install())
        self.top_level = 10
        url = "https://www.packtpub.com/free-learning"
        driver.get(url)
        handle = driver.current_window_handle
        node = node_class.NodeClass(url)
        node.add_handle(handle)
        self.simple_exploratory_random_testing(node, [], 0, driver)
        driver.close()
    def simple_exploratory_random_testing(self,node, visited, current_level, driver):
        """ method to start the exploration """
        current_level = current_level + 1
        opened_tabs = len(driver.window_handles)
        if current_level >= self.top_level:
            sys.exit("Max visits reached")
        visited.append(node)
        status_code = requests.get(node.url).status_code
        if status_code < 200 or (status_code >= 400 and status_code < 980):
            # hard exit to signify an issue on the url
            # use this line to debug bad status code
            # print(requests.get(node.url).status_code)
            sys.exit("Error on the url " + node.url)
        # get all actions first time in the node
        try:
            driver.switch_to(node.window_handle)
            driver.find_element(By.XPATH,'//a[@class="accept_all"]').click()
        except Exception:
            print("no cookies found")
        if node.count == -1:
            node.count=0
        for a_tag in driver.find_elements(By.TAG_NAME,'a'):
            # we only get the ones with packtput.com on them to be new nodes
            if "packtpub.com" in node.url:
                node.count=node.count+1
                href = a_tag.get_attribute('href')
                if href and not href.startswith("#"):
                    node.actions[href]=a_tag.get_dom_attribute('href')
                    # use this line for debugging purposes
                    # print(a_tag.get_dom_attribute('href'))
        # iterate through the actions randomly and visit them
        while node.count > 0:
            # randomly get one – then append to acted and remove a count
            suburl = self.random_get_one(node.actions, node.acted)
            node.acted.append(suburl)
            node.count = node.count - 1
            # create a new subnode
            subnode = node_class.NodeClass(suburl)
            if subnode not in visited:
                print("Visiting " + subnode.url + ". . .")
                self.try_click('//a[@href="'+node.actions[suburl]+'"]', driver, driver)
                # repeat the process for this subnode
                self.simple_exploratory_random_testing(subnode, visited, current_level, driver)
                driver.implicitly_wait(5)
                subnode.add_handle(driver.current_window_handle)
            # verify we havent reached the max of actions taken, 
            # so the algorithm does not take too long
            if current_level >= self.top_level:
                sys.exit("Max visits reached")
            # close any opened tabs
            if len(driver.window_handles) > opened_tabs:
                print("closing tab")
                driver.close()
                driver.switch_to().window(node.window_handle)
            else:
                print("going back. . . to " + node.url)
                driver.get(node.url)
                driver.implicitly_wait(5)

    def random_get_one(self, actions, acted):
        """ get one link at random """
        keys = list(actions.keys())
        count = len(keys)
        ransel = random.randrange(count)
        suburl = keys[ransel]
        while suburl in acted:
            ransel = random.randrange(count)
            suburl = keys[ransel]
        return suburl

    def try_click(self, xpath, driver, parent):
        """ try to click the element by xpath"""
        print("Trying to click " + str(xpath))
        try:
            element = parent.find_element(By.XPATH,xpath)
            ActionChains(parent).move_to_element(element).perform()
            driver.implicitly_wait(5)
        except Exception:
            print("Could not find the xpath" +
            ", it is possible that this object" +
            " is not available anymore")

SimpleExploratoryRandomTesting()

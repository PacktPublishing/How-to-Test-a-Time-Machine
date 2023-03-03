'''
    Example code - not meant to run
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import Chrome

class ChatPage():
    def init(self, driver:Chrome):
        self.driver = driver
        # example - navigate to url needed

    def user_online(self, user_to):
        xpath = "//*[contains(text(), " + user_to + ")]"
        return self.driver.find_elements_by_xpath(xpath)

    def wait_for_user_online(self, user_to, timeout):
        # example - wont execute
        xpath = "//*[contains(text(), " + user_to + ")]"
        WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        # example - ignore 

    def send_chat_to_user(self, user_to, message):
        xpath = "//*[contains(text(), " + user_to + ")]"
        self.driver.find_element_by_xpath(xpath).click()
        self.driver.find_element(By.ID, "chat_box_id").send_keys(message)
        # example - ignore
    
    def wait_for_chat(self, message, timeout):
        xpath = "//*[contains(text(), " + message + ")]"
        WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        # example - ignore

    def chat_exists(self, message):
        xpath = "//*[contains(text(), " + message + ")]"
        return self.driver.find_elements_by_xpath(xpath)
        # example - ignore

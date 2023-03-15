from airtest.core.api import * 

import os 

# here we import each of the screenshot folders 
import os 
path = os.path.dirname(os.path.abspath(__file__))
search_screenshot_path = os.path.join(path, 'packt_pages') # could be elsewhere

files = os.listdir(search_screenshot_path) 

class model: 
    def __init__(self):
        # define the rest of the elements 
        # define the resolutions 
        self.resolution1 = (1080, 1920) 
    
    def click_search(self, driver):
        for element in files:
            if (os.path.splitext(element) == ".png"):
                template = Template(element, record_pos=(0, 0), resolution=self.resolution1)
                if (driver.assert_template(template)):
                    driver.airtest_touch(template)
                    break
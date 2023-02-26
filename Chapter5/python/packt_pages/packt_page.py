from airtest.core.api import * 
import os

auto_setup(__file__) 

class packt_page:
    def __init__(self):
        self.chartElement = Template('tpl1631473475812.png', record_pos=(0, 0), resolution=(1080, 1920))

        self.chartElementMobile =Template(r"tpl1631473465222.png", record_pos=(0, 0), resolution=(1080, 1920))
        self.chartElements = [self.chartElement, self.chartElementMobile] 
        # define the rest of the elements

    def click_search(self, driver):
        for element in self.chartElements: 
            if (driver.assert_template(element)): 
                driver.airtest_touch(element)
                break
# we could and should define more elements or methods here 
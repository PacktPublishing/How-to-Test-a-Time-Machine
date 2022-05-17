'''
Example of integration api test - it would not run unless you change services and data!
'''
import unittest
import requests
class IntegrationAPITest(unittest.TestCase):
    ''' Class to test apis '''
    def when_serviceBDataChanges_serviceAResponseChanges(self):
        ''' Method to check B changes propagates to service '''
        service_A_original_response = requests.get(service_A_URL)
        service_B_data_change_request = requests.post(service_B_URL, data = {data_to_post})
        service_A_changed_response = requests.get(service_A_URL)
        self.assertNotEquals(service_A_original_response, service_A_changed_response)
        self.assertEquals(service_A_changed_response, some_expected_response)
    # Make sure the api goes back to its original state before the end of this test for test consistency (for example with another post reverting the first one).
    if __name__ == '__main__':
        unittest.main()

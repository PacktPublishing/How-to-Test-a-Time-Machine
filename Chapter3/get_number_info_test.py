'''
Tests the get_number_info_call class
'''
import unittest
import requests
class GetNumberInfoTest(unittest.TestCase):
    ''' Class to test get number info '''
    def test42correct(self):
        ''' tests correct inputs '''
        response = requests.get("http://numbersapi.com/42?json")
        status_code = response.status_code
        self.assertGreaterEqual(status_code, 200)
        self.assertLess(status_code, 400)
    def test_letter_incorrect(self):
        ''' test an incorrect input '''
        response = requests.get("http://numbersapi.com/a?json")
        status_code = response.status_code
        self.assertGreaterEqual(status_code, 400)
if __name__ == '__main__':
    unittest.main()
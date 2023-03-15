'''
Test the mocking functionality of unittest
'''
from unittest import TestCase
from unittest import main
from unittest.mock import patch
from request_call import invoke_get

class TestMock(TestCase):
    '''class to implement the mocking test'''
    def test_true(self):
        ''' test when status code is 200 '''
        with patch('request.get') as req:
            req.return_value.status_code = 200
            self.assertTrue(invoke_get())
    def test_false(self):
        ''' test when status code is 300 '''
        with patch('request.get') as req:
            req.return_value.status_code = 300
            self.assertFalse(invoke_get())

if __name__ == '__main__':
    main()

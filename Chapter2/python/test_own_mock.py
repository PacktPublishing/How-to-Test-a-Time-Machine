'''
Tests that our own mock implementation works as expected
'''
from unittest import TestCase
from unittest import main
from request_call_with_own_mock import invoke_get

class TestOwnMock(TestCase):
    '''class to test our own mock implementation'''
    def test_true(self):
        '''test the mocking class'''
        self.assertTrue(invoke_get(True))

if __name__ == '__main__':
    main()

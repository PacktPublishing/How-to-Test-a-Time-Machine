"""
Class to use for mocking request's responses
"""
from httplib2 import Response
import requests

def get_200() -> Response:
    """ Provides a 200 result mocked response """
    response = requests.Response()
    response.status_code = 200
    return response

"""
Class to demonstrate the request use with mocking
"""
import requests
from request_mock import get_200

def invoke_get(mock) -> bool:
    """ Returns true if the request to packtpub url returns 200 """
    url = "https://www.packtpub.com"
    response = requests.get(url)
    if mock:
        response = get_200()
    if response.status_code == 200:
        return True
    return False

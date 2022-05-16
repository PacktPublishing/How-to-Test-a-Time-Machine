"""
Class to demonstrate the request use
"""
import requests

def invoke_get() -> bool:
    """ Returns true if the request to packtpub url returns 200 """
    response = requests.get("https://www.packtpub.com")
    if response.status_code == 200:
        return True
    return False

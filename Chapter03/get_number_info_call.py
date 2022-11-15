'''
Calls the numbersapi API with parameter 42
'''
import requests
response = requests.get("http://numbersapi.com/42?json")
print(response.status_code)
print(response.json())

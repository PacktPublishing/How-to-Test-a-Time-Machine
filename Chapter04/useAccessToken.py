import requests

access_token = input('Insert access Token:')
headers = {'Authorization': 'Bearer '+ access_token}
response = requests.get('https://www.googleapis.com/userinfo/v2/me', headers=headers)
print(response.content)
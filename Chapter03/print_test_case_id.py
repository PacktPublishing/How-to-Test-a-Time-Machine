'''
Functionality to print a test case
'''
from testrail import APIClient
client = APIClient('http://yourtestrailURL/')
client.user = 'youruseremail' # These two lines are for authentication
client.password = 'yourApiKey'
case = client.send_get('get_case/id') # This line makes the request
print(case)

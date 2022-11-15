'''
Just an example, not functionality intended
'''
import requests
# make a get call
response = requests.get("URL")
# do something with the result
response.status_code # this gives you the status code as mentioned above
response.json() # this gives you a json with the response on it
# make a post call
response = requests.post("URL", {"json: data"})

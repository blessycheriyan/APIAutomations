import requests
import json
import jsonpath

url = 'https://reqres.in/api/users/2'
# Read Input Json file
file = open('C:\\Users\\bless\\OneDrive\\Desktop\\APIAutomation\\Post_Requests\\create.json', 'r')
json_input = file.read()
# Parse response  to Json Format (All Content fetching)

request_json = json.loads(json_input)

# Make PUT request with Json Input Format
response = requests.put(url, request_json)

# Validating Response Code
assert response.status_code == 200

# Parse response  to Json Format
response_json = json.loads(response.text)
print(response_json)
# Pick Id using Jsonpath
updated_li = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated_li[0])

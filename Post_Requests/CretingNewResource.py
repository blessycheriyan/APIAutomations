import requests
import json
import jsonpath

url = 'https://reqres.in/api/users'
# Read Input Json file
# file = open('create.json', 'r')
file = open('C:\\Users\\bless\\OneDrive\\Desktop\\APIAutomation\\Post_Requests\\create.json', 'r')
json_input = file.read()
# Parse response  to Json Format (All Content fetching)

request_json = json.loads(json_input)
print(request_json)

# Make POST request with Json Input Format
response = requests.post(url, request_json)
print(response.content)

# Validating Response Code

assert response.status_code == 201

# Fetch Header from Response
print(response.headers)

# Fetch Header from Response(Specific Content to Fetching)
print(response.headers.get('Content-Length'))

# Parse response  to Json Format
response_json = json.loads(response.text)

# Pick Id using Jsonpath
id = jsonpath.jsonpath(response_json, 'id')
print(id[0])

import requests
import json
import jsonpath

# API URL
url = 'https://reqres.in/api/users?page=2'
# Send get request

response = requests.get(url)

# Parse response  to Json Format (All Content fetching)
json_response = json.loads(response.text)
print(json_response)

# Fetch value using to Jsonpath (Specific Content fetching)
pages = jsonpath.jsonpath(json_response, 'total')
print(pages[0])
assert pages[0] == 12

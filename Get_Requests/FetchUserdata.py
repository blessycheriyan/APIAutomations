import requests

# API URL
url = 'https://reqres.in/api/users?page=2'
# Send get request

response = requests.get(url)
# Display Response Content

print(response.text)
print(response.content)
print(response.headers)

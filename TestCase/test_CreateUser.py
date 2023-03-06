import requests
import json
import jsonpath

url = 'https://reqres.in/api/users'

def test_create_new_user():
    file = open('C:\\Users\\bless\\OneDrive\\Desktop\\APIAutomation\\Post_Requests\\create.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    response = requests.post(url, request_json)
    print(response.content)
    assert response.status_code == 201
    print(response.headers)
    print(response.headers.get('Content-Length'))
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])

def test_create_other_user():
    file = open('C:\\Users\\bless\\OneDrive\\Desktop\\APIAutomation\\Post_Requests\\create.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    assert response.status_code == 201
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')

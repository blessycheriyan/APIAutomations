import requests
import json
import jsonpath

def test_create_new_user():
    url = 'https://jsonplaceholder.typicode.com/comments'
    file = open('C:\\Users\\bless\\PycharmProjects\\APIAutomation\\TestCase\\create.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    response = requests.post(url, request_json)
    print(response.content)
    # assert response.status_code == 201
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])

    url = 'https://jsonplaceholder.typicode.com/posts'
    file = open('C:\\Users\\bless\\PycharmProjects\\APIAutomation\\TestCase\\photos.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    response = requests.post(url, request_json)
    print(response.content)


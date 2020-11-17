import pytest
import requests
import json
import jsonpath


def test_Chain():
    global id
    API = "http://www.thetestingworldapi.com/api/studentsDetails"
    file = open('C:\\LocalRepos\\APIAutomationPython\\json\\End2End\\Addstudent.json', 'r')
    requests_json = json.loads(file.read())
    response = requests.post(API, requests_json)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(response.text)
    print(id[0])


def test_GetDetails():
    API = "http://www.thetestingworldapi.com/api/studentsDetails/" + str(id[0])
    response = requests.get(API)
    print(response.text)

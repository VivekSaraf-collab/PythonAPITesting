import json
import pytest
import requests
import jsonpath


def test_PostStudent():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("C:\\LocalRepos\\APIAutomationPython\\json\\End2End\\Addstudent.json", 'r')
    json_request = json.loads(file.read())
    response = requests.post(API_URL, json_request)
    print(response.text)

def test_PutStudent():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/79810"
    file_put = open("C:\\LocalRepos\\APIAutomationPython\\json\\End2End\\Addstudent.json", 'r')
    json_request = json.loads(file_put.read())
    new_response = requests.put(API_URL, json_request)
    print(new_response.text)

@pytest.mark.skip
def test_DeleteStudent():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/79806"
    response_Delete = requests.delete(API_URL)
    print(response_Delete.text)

@pytest.mark.skip
def test_GetStudent():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/79810"
    response = requests.get(API_URL)
    response_put = response.json()
    print(response_put)
    print(response.text)
    json_response = json.loads(response.text)
    idStudent = jsonpath.jsonpath(json_response, 'data.id')




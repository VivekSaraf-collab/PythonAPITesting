import json

import jsonpath
import requests


def test_StudentDetails():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open('C:\\LocalRepos\\APIAutomationPython\\json\\End2End\\Addstudent.json', 'r')
    requests_json = json.loads(file.read())
    response = requests.post(API_URL, requests_json)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(response.text)
    print(id[0])

    tech_API_URL = "http://www.thetestingworldapi.com/api/technicalskills"
    tech_file = open('C:\\Users\\vivek\\OneDrive\\Desktop\\json\\End2End\\TechnicalDetails.json', 'r')
    json_request_tech = json.loads(tech_file.read())
    json_request_tech['id'] = int(id[0])
    json_request_tech['st_id'] = id[0]
    response = requests.post(tech_API_URL, json_request_tech)


    Address_API_URL = "http://www.thetestingworldapi.com/api/addresses"
    address_file = open('C:\\Users\\vivek\\OneDrive\\Desktop\\json\\End2End\\Address.json', 'r')
    json_request_Address = json.loads(address_file.read())
    json_request_Address['stId'] = id[0]
    response = requests.post(Address_API_URL, json_request_Address)


    FullDetails_API_URL = "http://www.thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(FullDetails_API_URL)
    print(response.text)

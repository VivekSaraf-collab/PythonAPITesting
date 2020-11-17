import json
import pytest
import requests
import jsonpath
import openpyxl
from DataDriven import Library


def test_MultipleStudent():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open('C:\\Users\\vivek\\OneDrive\\Desktop\\json\\studentDetails.json', 'r')
    json_request = json.loads(file.read())

    obj = Library.common("C:/Users/vivek/OneDrive/Desktop/json/End2End/SD.xlsx", "Sheet1")
    obj.fetch_columnCount()
    obj.fetch_rowCount()
    obj.fetch_keyNames()

    for i in range(2, rows + 1):
        updated_json_request = obj.update_requestWithData(i, json_request, keyList)
        response = requests.post(API_URL, updated_json_request)
        print(response)

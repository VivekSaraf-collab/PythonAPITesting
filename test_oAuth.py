import requests
import json
import jsonpath
import pytest


def test_OAuth():
    token_url = "http://www.thetestingworldapi.com/Token"
    data = {'grant_type': 'password', 'useName': 'vivek123', 'password': 'Abcd@1234'}
    response = requests.post(token_url, data)
    token_value = jsonpath.jsonpath(response.json(), 'access_token')
    auth = {'Authorization': 'Bearer' + 'token_value[0]'}
    API = "http://www.thetestingworldapi.com/api/StDetails/11123"
    response = requests.get(API)
    print(response.text)

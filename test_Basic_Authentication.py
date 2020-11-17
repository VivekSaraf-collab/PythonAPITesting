import requests
from requests.auth import HTTPBasicAuth


def test_BasicAuthentication():
    API = "https://api.github.com/user"
    respone = requests.get(API, auth=HTTPBasicAuth('Vivekananda09497', '5690b8e5a9db8020c05fcb1c22a032bea988c68d'))
    print(respone.text)

import requests


def post(self, request_url, json_obj=None, params=None, files=None, headers=None):
    if headers is None:
        headers = default_headers

    if files is None:
        resp = requests.post(request_url, data=json.dumps(json_obj), params=params, files=files,
                             headers=headers, verify=False)
    else:
        resp = requests.post(request_url, params=params, files=files,
                             verify=False)
    return resp


user_cred = {
    "username": "admin",
    "password": "password"
}
gateway = "10.5.58.13"

login_to_gateway = "http://" + gateway + "/api/" + "authenticate/user"
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
response = post(login_to_gateway, user_cred, headers=headers)
print(response)
# authorization_code = response.json()["data"]["token"]
# print(authorization_code)



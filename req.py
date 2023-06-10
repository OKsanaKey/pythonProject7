import requests
import json


#POST-запрос

url = 'https://petstore.swagger.io/v2/pet'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
    "id": 0,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "franky",
    "photoUrls": ["string"],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}

res = requests.post(url, headers=headers, data=json.dumps(data))
print(res.status_code)
print(res.json())


#GET-запрос

status ='available'
headers = {'accept': 'application/json'}

res1 = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers=headers)
print(res1.status_code)
print(res1.text)
print(res1.json())
print(type(res1.json()))



#PUT-запрос

username = 'Robby'
url = 'https://petstore.swagger.io/v2/user/{username}'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
  "id": 0,
  "username": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}

res2 = requests.put(url, headers=headers, data=json.dumps(data))

print(res2.status_code)
print(res2.json())

#DELETE-запрос

url = 'https://petstore.swagger.io/v2/user/Robby'

headers = {
    'accept': 'application/json'
}
res3 = requests.delete(url, headers=headers)
print(res3.status_code)
print(res3.json())
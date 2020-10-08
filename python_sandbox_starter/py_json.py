# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

myInfo={
    'name': 'Rehman Aziz',
    'age':23,
    'university': 'G.C University',
    'semester':7
}

myInfoStr='{"name":"Sunny","age":20,"dob":"29-jan-1997"}'

print(myInfo)

user=json.dumps(myInfo)
userJson=json.loads(myInfoStr)

print(user)

print(userJson)
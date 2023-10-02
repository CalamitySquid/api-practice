# Rest apis
# Application Programming Interface
import requests # request something from the internet
import json # json stands for javascript object notation

response = requests.get("https://randomuser.me/api/")
# print(response.json())
gender = response.json()['results'][0]['gender']
print(gender)
title = response.json()['results'][0]['name']['title']
print(title)
first = response.json()['results'][0]['name']['first']
last = response.json()['results'][0]['name']['last']
print(first +" "+  last)
email = response.json()['results'][0]['email']
print(email)
phone = response.json()['results'][0]['phone']
print(phone)
city = response.json()['results'][0]['location']['city']
print(city)
postcode = response.json()['results'][0]['location']['postcode']
print(postcode)
street = response.json()['results'][0]['location']['street']
print(street)
dob = response.json()['results'][0]['dob']['date']
print(dob)
uuid = response.json()['results'][0]['login']['uuid']
print(uuid)
reg_age = response.json()['results'][0]['registered']['age']
print(reg_age)
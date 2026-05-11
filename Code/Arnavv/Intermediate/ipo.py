import json
import requests
with open("request","r") as file:
    data=json.load(requests)

print(data)
print(data["current_weather"])
print(data["current_weather"]["temperature"])
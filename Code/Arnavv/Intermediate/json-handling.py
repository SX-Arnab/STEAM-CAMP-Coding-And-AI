import json

with open('test.json') as f:
    json_read = json.load(f)
    print(json_read)
    

with open('test.json', 'a') as file:
    json.dump('urguheguheagherguergu', file, indent= 5)
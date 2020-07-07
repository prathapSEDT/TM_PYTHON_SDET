import json

file=open("samplejson.json",'r')

jsonObj=json.load(file)


print(type(jsonObj))


for result in jsonObj["results"]:

    print(result['name'])


import os
import json
import datetime


def relative_path(file_name):
    script_path = os.path.abspath(os.path.dirname(__file__))
    joint_path = os.path.join(script_path, file_name)
    return joint_path

now = datetime.datetime.now() # This will return current year month day
jdate = { "year": now.year, "month": now.month, "day": now.day}
jdict = { "content": "hello world", "date": jdate }

xxx = json.dumps(jdict, sort_keys=True, indent=3)
print (xxx)

with open(relative_path("data.json"), 'w') as outfile:
    json.dump(jdict, outfile)

'''
print('serialization')
myDictObj = { "name":"John", "age":30, "car":None }
##convert object to json
serialized= json.dumps(myDictObj, sort_keys=True, indent=3)
print(serialized)
## now we are gonna convert json to object
deserialization=json.loads(serialized)
print(deserialization)
'''


import json

jdate = { "year": "2000", "month": "12", "day": "1" }
jdict = { "content": "hello world", "date": jdate }


print (json.dumps(jdict))


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
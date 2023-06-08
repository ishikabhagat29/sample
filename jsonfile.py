import json
f = open('nested_dict.json')
data = json.load(f)
print(data)

#writting json into file
json_object = json.dumps(data,indent = 4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)


for element in data:
    if 'sparklistD1' in element:
        del element['sparklistD1']

for key in nested_dict:
    if nested_dict[key] is NULL:
         nested_dict.pop(key)







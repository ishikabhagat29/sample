import json
from math import isnan
def open_file():
    try:
        f = open('nested_dict.json')
        data = json.load(f)
        f.close()
        return data
    except Exception as e:
        print(e)

data = open_file()
for key, value in data.items():
    if isinstance(value,dict):
        
        




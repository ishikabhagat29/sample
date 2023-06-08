testing = {
    "test1":{
        "sum":1,
        "avg":2,
        "min":"NA"
    },
        "test2":{
        "sum":1,
        "avg":"NA",
        "min":2
    },
     "test3":{
        "sum":"NA",
        "avg":5,
        "min":2
    },

}

#remove NA values from above  nested dictionary

for key , values in testing.items():
    if isinstance(values,dict):
        for a,value in values.items():
            #if value == 'NA':
             #value.pop(key)
             if value != "NA":
                print(a,value)

   
    #elif isinstance(,dict)

    

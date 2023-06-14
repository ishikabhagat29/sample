x = {
    "A": 30,
    "B": 60,
    "C": 15  
}

class value():
    value = {a for a in x if x[a] == 60}
    print("key for value is:",value)
    """ this function looks for the key in the dictionary"""
      

    def sum_values(a):
        """ this function adds up all the values of keys  in the dictionary"""
        try:
         return sum(x.values())
        except Exception as e:
         print(e)
    print(sum(x.values()))


    def multiply_values(x,factor):
     """ this function multiplies the value by a factor in the dictionary"""
     try:
        for key in x:
            return x[key]
        x[key] = x[key]* factor
     except Exception as e:
        print(e)
    print(x[key].values)


    def new_values(x,new_data):
     """ this function adds new data in the dictionary"""
     try:
        x.update(new_data)
     except Exception as e :
        print(e)
    print(x)


x = {
    "A": 30,
    "B": 60,
    "C": 15  
}

factor = 2
multiply_values(x,factor)
print("multiply_values:",x)

new_data = {"D":56,"E":35}
(x,new_data)
print("Updated values:",x)









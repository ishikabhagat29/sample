class xyz():
    
    def upper(a):
        """ This function takes the string and convert it into upper case and returns it"""
        try:
            x = a.upper()
            return x
        except Exception as e:
            print(e)

    def lower(b):
        """"" This function takes the string and converts it into lower case and returns it"""
        try:
            y = b.lower()
            return y
        except Exception as e :
            print(e)


    def title(c):
        """"This function takes the string and convert into a title and returns it"""
        try:
            z = c.title()
            return z
        except Exception as e:
            print(e)

i = input("Enter a string:")
print("The string is:",i)
print("The uppered case is",xyz.upper(i))
print("The lowered case is",xyz.lower(i))
print("The titled case is",xyz.title(i))



    

    



#simple calculator using class
class Calculator:
#operations 
    def add(self,a,b):
        try:             #try and exception 
            return a+b
        except Exception as e:
              print(e)

    def subtract(self,a,b):
         s = (a-b)
         try:
          if s < 0:
               return s
         except Exception as e:
            print(e)
               
             
    def multiply(self,a,b):
        try:
            return a*b
        except Exception as e:
             print(e)
    
    def divide(self,a,b):
        try:
            return a/b
        except Exception as e:
             print(e)    

calc_obj = Calculator()
#selection for user
while True:
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.divide")
    print("5.Exit")
   
    select = int(input("Select operation to be performed:"))

    if(select == 5):
            break

   
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))

    if(select == 1):
            print(a, "+", b, "=", calc_obj.add(a, b))
    
    elif( select == 2):
            print(a, "-", b, "=", calc_obj.subtract(a, b))
    
    elif(select == 3):
            print(a, "*", b, "=", calc_obj.multiply(a, b))
   
    elif(select == 4):
            print(a, "/", b, "=", calc_obj.divide(a, b))
    

    else:
        print("Invalid Input")


    
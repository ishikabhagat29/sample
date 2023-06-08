# swap two numbers without using third value
a = int(input("Enter a value:"))
b = int(input("Enter another value:"))
a = a+b
b = a-b
a = a-b
print("After swapping a is:",a)
print("After swapping b is:",b)



#swapping of numbers using generators
def swap_values(a,b):
    a = int(input("Enter a value:"))
    b = int(input("Enter another value:"))
    #swapping values
    a,b = b,a
    #after swapping values
    print("a is:",a)
    print("b is:",b)




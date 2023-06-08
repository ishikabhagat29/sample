#fibonacci series using generators
def fibonacciGenerator():
    a=0
    b=1
    count = 0
    for i in range(6):
        yield a
        a,b= b,a+b

obj = fibonacciGenerator()
 
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj)) 


































# sum of squares of numbers in the Fibonacci series


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))
i = int(input("Enter a string:"))
   
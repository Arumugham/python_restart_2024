#Day 5: Functions
#Task: Understand how to define and call functions.

#Exercise 5.1: Simple function
# problem statement: Write a function that takes a list of numbers and returns their average.
def calculate_average(numbers):
    total = sum(numbers)
    return total/len(numbers)

list = [10,20,30,40]
print("The average of list",list,"is",calculate_average(list))

#Exercise 5.2: Returing multiple values
# Problem statement: Write a function that takes a list of numbers as input and 
# returns the sum, average, and maximum value of the numbers.

def math_ops(numbers):
    total = sum(numbers)
    avg = total/len(numbers)
    max_number = max(numbers)
    return (total, avg, max_number)

list = [10,20,30,40]
result = math_ops(list)
print("For the list {}, sum is {}, average is {} and max_number is {}".format(list,result[0],result[1],result[2]))

#Exercise 5.3: Default argument
#Problem statement: Create a function that takes a name and age as input,
# with a default age of 18 if not provided. The function should print out the name and age.

def age_printer(person):
    if person["age"] == "":
        person["age"] = 18
    print("Hello",person["name"],". Congratulation for turning age",person["age"])

human = {"name": input("Please enter name: "),"age": input("Please enter age: ")}
age_printer(human)

#Exercise 5.4: Variable-Length Arguments:
# Write a function that takes any number of arguments and returns their sum.

def addition(*args):
    print("The sum of values",args,"is",sum(args))

addition(4,5,6,0,4,5,6)

# Exercise 5.5 Lambda Functions:
# Use a lambda function to square a given number.

square = lambda x: x**2
num = 5
result = square(num)
print("The square of",num,"is",result)

# Exercise 5.6: Recursion:
# Write a recursive function to calculate the factorial of a number.

def factorial(num):
    if num <0:
        return "Factorial is not defined for negative numbers"
    elif num == 0:
        return 1
    elif num > 1000:
        return "Value is too large to calculate factorial"
    else:
        return num * factorial(num-1)

num = 10000
print("factorial of",num,":",factorial(num))

# Exercise 5.7: Decorators:
# Create a decorator that converts the result of a function to uppercase

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello,{name}!"

#calling the decorated function

print(greet("Arumugham"))

# Exercise 5.8: Generators:
# Implement a generator function that yields the Fibonacci sequence up to a certain limit.

def fibonacci_generator(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a, b = b, a + b

for num in fibonacci_generator(100):
    print(num)
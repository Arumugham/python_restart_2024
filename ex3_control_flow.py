#Day 3: Control Flow (if-else)**
#Task:** Understand if-else statements and comparison operators.
#Exercise:** Write a program that checks if a number is positive, negative, or zero.
try:
    num = float(input("Enter a number:"))
    num = float(num)   
    if num > 0:
        print(num," is a positive number")
    elif num < 0:
        print(num," is a negative number")        
    elif num == 0:
        print(num," is a zero")
except ValueError:
    print("This is invalid input, kindly enter a number")
#Data Types and Operators
#Task: Learn about different data types (int, float, string, list, tuple, dict, set) and operators.
#Exercise: Write a script that performs basic arithmetic operations and prints the results.


val1 = input("Enter input value 1: ")
val2= input("Enter input value 2: ")

#isdigit check if it is a number
if val1.isdigit() and val2.isdigit():
    
    # int(val1) check if a value is integer
    print("The integer sum is", int(val1) + int(val2))
elif isinstance(float(val1),float) and isinstance(float(val2),float):
    print("The float sum is", float(val1) + float(val2))
elif isinstance(val1,str) and isinstance(val2,str):
    print("The string sum is", val1 + val2)

    
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average


#List have properties like they are mutable. 
# declaring a list
numbers = [1,2,3,4,5]

#calculate  and print the average
avg = calculate_average(numbers)
print("The average value of ",numbers," is: ", avg)

#apparently you can append in a list
numbers.append(6)
print("The updated numbers list after apending is",numbers)

# I can also print number of a specific position. Keep in mind that index start with 0
print("Element of ",numbers,"at index 2 is",numbers[2])

#List can also remove a value by mentioning in the bracket
numbers.remove(3)
print("The updated number list after removing is",numbers)


#Tuples are immutable and efficient. They are faster that list and its values cannot be changed.
#There are various usecase to use them

#1. Returning multiple value from function

def get_coordinates():
    return(10,30)

x,y = get_coordinates()
print("Coordinates:",x,y)

#2. Dictionary key
location = {(10,20):"Home", (30,40):"Work"}
print("What is the location of 10,20?",location[10,20])

#3. Varable swapping
a = 10
b = 30
a, b = b,a
print("a:",a)
print("b:",b)

#4. Unpacking arguments in function calls
def calculate_total(*args):
    return sum(args)

numbers_tuple=(10,20,30,40,50)
total = calculate_total(*numbers_tuple)
print("Total of (10,20,30,40,50):", total)

# Exploring dictionary

student1 = {"name":"Ram", "age":20, "percentage":"90%"}
student2 = {"name":"Sita", "age":19, "percentage":"78%"}

students = [student1, student2]

for student in students:
    print(student["name"])

# Exploring sets

#1. Sets for removing duplicates

numbers = [1,2,3,4,2,3,5,4,1]
unique_numbers = set(numbers)

print("original list:",numbers)
print("unique numbers after removing duplicates using set",unique_numbers)

#2. Membership testing

fruits = {"apple","orange","mango"}

#check if apple is present in the set
print("apple" in fruits)
print("grape" in fruits)

#3. Finding intersections

set1 = {1,2,3,4}
set2 = {3,4,5,6}

#find the common elements between tw0 sets
print("Intersection:",set1.intersection(set2))

#finding difference

set1 = {1,2,3,4}
set2 = {3,4,5,6}

#find the difference between two sets
print("Difference:",set1.difference(set2))

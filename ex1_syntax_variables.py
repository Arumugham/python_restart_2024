
#Task: Review basic syntax, comments, and variables.
#Exercise: Create a script that takes user input for their name and age, then prints a greeting.

# The function for getting input in input(), enter the text inside the bracked to get it printed.
name = input("Enter your name:")

#caste input to specific type
age = int(input("Enter your age:"))

#Get multiple input

gender, nationality = input("enter you gender and nationality (separated by space)").split()


#print statement with multiple arguments
print("Vannakam",name,"!","\nHow does ",age,"yrs feel like?\n")

#print statement with string concatenation
print("What makes you a true " + nationality +"?")

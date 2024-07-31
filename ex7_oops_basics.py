#Exercise 7: Object-Oriented Programming (OOP) Basics**
#Task: Learn about classes, objects, and methods.
#Activity: Create a class for a `Book` with properties like title, author, 
#and methods to display details.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)

#Create an instance of the book class
book1 = Book("Python Programming", "John Doe")

#Display the details of the book
book1.display_details()
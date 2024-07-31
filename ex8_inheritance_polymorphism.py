# Exercise 8: Inheritance and Polymorphism
# Task: Understand inheritance and polymorphism.
# Activity: Create a class hierarchy for vehicles (e.g., Car, Truck) 
# with common and specific attributes.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        
        #Intiate the previous class
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_details(self):
        super().display_details()
        print(f"Number of Doors: {self.num_doors}")

class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity

    def display_details(self):
        super().display_details()
        print(f"Cargo Capacity: {self.cargo_capacity} tons")

#Create an instances of car and truck
car1 = Car("Toyata", "Camry", 2021, 4)
truck1 = Truck("Ford", "F-150", 2020, 5)

#Display details of car and truck
car1.display_details()
truck1.display_details()


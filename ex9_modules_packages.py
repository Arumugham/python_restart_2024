#Exercise 9: Modules and Packages
#Task: Learn how to import and use modules and packages.
#Activity: Write a script that uses the `math` and `random` modules for various operations.

import math, random

#calculate the square root of a number
num = 25
sqrt_num = math.sqrt(num)
print(f"Square root of {num} is: {sqrt_num}")

#generate a random between 1 & 10
random_num = random.randint(1, 10)
print(f"Random number between 1 & 10: {random_num}")
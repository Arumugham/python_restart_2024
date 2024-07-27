#Day 4: Loops (for and while)**
#Task: Learn about for and while loops.
#Exercise: Write a script that prints the first 10 numbers of the Fibonacci sequence.

# finboacci series with while loop. this is not efficient as there as additional variable

print("Printing 10 fiboacci sequence using while loop")
a = 1
b = 1
n = 8
print(a)
print(b)
while n>0:    
    c = a + b
    print(c)
    a,b = b,c
    n -=1

print("Printing 10 fiboacci sequence using for loop")
a, b = 1, 1
print(a)
print(b)
for _ in range(8):
    c = a + b
    print(c)
    a,b = b,c

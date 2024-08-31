#Exercise 11: Regular Expressions**
#Task: Learn about regular expressions for pattern matching.
#Activity: Write a script that validates email addresses using regular expressions.

#Exercise 11.1 Write a Python program to check that a string 
#contains only a certain set of characters (in this case a-z, A-Z and 0-9).

# | Symbol | Meaning |
# |--------|---------|
# | . | Matches any single character except newline |
# | ^ | Anchors the regex at the start of a string |
# | $ | Anchors the regex at the end of a string |
# | * | Matches zero or more occurrences of the preceding element |
# | + | Matches one or more occurrences of the preceding element |
# | ? | Matches zero or one occurrence of the preceding element |
# | [] | Matches any single character within the brackets |
# | () | Groups multiple tokens together |
# | \d | Matches any digit (equivalent to [0-9]) |
# | \w | Matches any word character (alphanumeric + underscore) |
# | \s | Matches any whitespace character |
# | \b | Matches a word boundary |
# | | | Alternation, matches either the expression before or after the | |
# | {} | Specifies the number of occurrences of the preceding element |

import re

def is_allowed_characters_and_numbers(input_string):
    pattern = re.compile(r'[a-zA-Z0-9]')
    if pattern.search(input_string):
        return True
    return False
print("the below string contains only a certain set of characters (in this case a-z, A-Z and 0-9)")
print("ABCDEFabcdef123450:",is_allowed_characters_and_numbers("ABCDEFabcdef123450")) 
print("*&%@#!}{:",is_allowed_characters_and_numbers("*&%@#!}{"))


#Exercise 11.2 Write a Python program that matches a string 
#that has an "a" followed by zero or more b's

def check_string(input_string):
    pattern = re.compile(r'a+b*')
    if pattern.search(input_string):
        return True
    return False
print("the below string contains an 'a' followed by zero or more b's")
print("ac:",check_string("ac")) 
print("abc:",check_string("abc"))
print("abbc:",check_string("abbc"))
print("bc:",check_string("bc"))
print("dab:",check_string("dab"))

      


#Exercise 11.3 Write a Python program that matches a string 
#that has an "a" followed by one or more b's

def check_string(input_string):
    pattern = re.compile(r'ab+')
    if pattern.search(input_string):
        return True
    return False
print("the below string contains an 'a' followed by one or more b's")
print("ac:",check_string("ac")) 
print("a:",check_string("a")) 
print("ba:",check_string("ba")) 
print("ab",check_string("ab"))


#Exercise 11.4 Write a Python program that matches a string 
#that has an "a" followed by "zero" or one 'b'

def check_string(input_string):
    pattern = re.compile(r'ab?')
    if pattern.search(input_string):
        return True
    return False
print("the below string contains an 'a' followed by one or more b's")
print("ac:",check_string("ac")) 
print("abb:",check_string("abb")) 
print("b:",check_string("b")) 
print("ab:",check_string("ab"))


#Exercise11.5 Write a Python program that matches a string 
#that has an "a" followed by three 'b'
def check_string(input_string):
    pattern = re.compile(r'ab{3}')
    if pattern.search(input_string):
        return True
    return False
print("the below string contains an 'a' followed by three 'b'")
print("ac:",check_string("ac")) 
print("abbb:",check_string("abbb")) 
print("ba:",check_string("ba")) 
print("ab:",check_string("ab"))

# Exercise 11.6
# Write a Python program that matches a string that has an 'a' followed by two to three 'b's.

def check_string(input_string):
    pattern = re.compile(r'ab{2,3}')
    if pattern.search(input_string):
        return True
    return False
print("the below string contains an 'a' followed by two to three 'b's")
print("ac:",check_string("ac")) 
print("abbb:",check_string("abbb")) 
print("ba:",check_string("ba")) 
print("ab:",check_string("ab"))
print("abb:",check_string("abb"))



# Exercise 11.7
# Write a Python program to find sequences of lowercase letters joined with an underscore.

def check_string(input_string):
    pattern = re.compile(r'[a-z]+_[a-z]+')
    if pattern.search(input_string):
        return True
    return False
print("the below string find sequences of lowercase letters joined with an underscore")
print("ac_ac",check_string("ac_ac")) 
print("_abbb",check_string("_abbb")) 
print("ba_",check_string("ba_")) 
print("ab:",check_string("ab"))
print("a_b_b",check_string("a_b_b"))


# Exercise 11.8
# Write a Python program to find the sequences of one uppercase letter followed by lowercase letters.

def check_string(input_string):
    pattern = re.compile(r'[A-Z][a-z]+')
    if pattern.search(input_string):
        return True
    return False
print("the below string find the sequences of one uppercase letter followed by lowercase letters")
print("Bac:",check_string("Bac"))
print("ac:",check_string("ac"))



# Exercise 11.9
# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.


def check_string(input_string):
    pattern = re.compile(r'a.*b$')
    if pattern.search(input_string):
        return True
    return False
print("the below string has an 'a' followed by anything, ending in 'b")
print("Bac:",check_string("Bac"))
print("ac:",check_string("ac"))
print("acb:",check_string("acb"))

# Exercise 11.10
# Write a Python program that matches a word at the beginning of a string.

def match_word_beginning(input_string):
    pattern = re.compile(r'^[a-zA-Z]+')
    if pattern.match(input_string):
        return True
    return False

print("Matching a word at the beginning of a string")
print("Hello World:" , match_word_beginning("Hello World"))
print("Python Programming:", match_word_beginning("Python Programming"))
print("123 Start with number:", match_word_beginning("123 Start with number"))


# Exercise 11.11
# Write a Python program that matches a word at the end of a string, with optional punctuation.

def match_word_end(input_string):
    pattern = re.compile(r'\b\w+\b[.,;:]*$')
    if pattern.search(input_string):
        return True
    return False

print("Matching a word at the end of a string with optimal punctuation")
print("The end.", match_word_end("The end."))
print("Finish;", match_word_end("Finish;"))
print("Last", match_word_end("Last"))
print("No match!", match_word_end("No match!"))


# Exercise 11.12
# Write a Python program that matches a word containing 'z'.

def match_word_with_z(input_string):
    pattern = re.compile(r'\b\w*z\w*\b')
    if pattern.search(input_string):
        return True
    return False

print("Matching a word containing 'z':")
print("zebra:", match_word_with_z("zebra"))
print("apple:", match_word_with_z("apple"))
print("amazing:", match_word_with_z("amazing"))
print("jazz:", match_word_with_z("jazz"))
print("zebra:", match_word_with_z("zebra"))
print("apple:", match_word_with_z("apple"))
print("amazing:", match_word_with_z("amazing"))
print("jazz:", match_word_with_z("jazz"))


# Exercise 11.13
# Write a Python program that matches a word containing 'z', not at the start or end of the word.
def match_word_with_z(input_string):
    pattern = re.compile(r'\b\w+[^z\s]z[^z\s]\w+\b')
    if pattern.search(input_string):
        return True
    return False

print("Matching a word containing 'z':")
print("zebra:", match_word_with_z("zebra"))
print("apple:", match_word_with_z("apple"))
print("amazing:", match_word_with_z("amazing"))
print("jazz:", match_word_with_z("jazz"))
print("zebra:", match_word_with_z("zebra"))
print("apple:", match_word_with_z("apple"))
print("amazing:", match_word_with_z("amazing"))
print("jazz:", match_word_with_z("jazz"))

# Exercise 11.14
# Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

def match_alphanumeric_underscore(input_string):
    pattern = re.compile(r'^[a-zA-Z0-9_]+$')
    if pattern.match(input_string):
        return True
    return False

print("Matching a string with only letters, numbers, and underscores:")
print("Hello 123:", match_alphanumeric_underscore("Hello 123"))
print("Python_Programming:", match_alphanumeric_underscore("Python_Programming"))
print("Test@123:", match_alphanumeric_underscore("Test@123"))

# Exercise 11.15
# Write a Python program where a string will start with a specific number.

def starts_with_number(input_string, specific_number):
    pattern = re.compile(r'^' + str(specific_number))
    if pattern.match(input_string):
        return True
    return False

specific_number = 123

print(f"check if string starts with {specific_number}:")
print("12345Test",":", starts_with_number("12345Test",specific_number))
print("Test",":", starts_with_number("Test",specific_number))

# Exercise 11.16
# Write a Python program to remove leading zeros from an IP address.

def remove_leading_zeros(ip_address):
    #\b is used to match word boundaries.
    #0+ matches one or more leading zeros.
    #(\d+) captures one or more digits following the leading zeros.
    pattern = re.compile(r'\b0+(\d+)')
    
    #pattern.sub(r'\1', ip_address) substitutes the match with the captured digits, 
    #removing leading zeros. 
    result = pattern.sub(r'\1', ip_address)
    return result

ip_address = "192.168.001.001"
update_ip = remove_leading_zeros(ip_address)
print(f"Original IP address: {ip_address}")
print(f"Updated IP address: {update_ip}")


# Exercise 11.17
# Write a Python program to check for a number at the end of a string.

def check_number_at_end(input_string):
    

# Exercise 11.18
# Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.

# Exercise 11.19
# Write a Python program to search some literal strings in a string.

# Exercise 11.20
# Write a Python program to search a literal string in a string and also find the location within the original string where the pattern occurs.

# Exercise 11.21
# Write a Python program to find the substrings within a string.

# Exercise 11.22
# Write a Python program to find the occurrence and position of the substrings within a string.

# Exercise 11.23
# Write a Python program to replace whitespaces with an underscore and vice versa.

# Exercise 11.24
# Write a Python program to extract year, month, and date from a URL.

# Exercise 11.25
# Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

# Exercise 11.26
# Write a Python program to match if two words from a list of words start with the letter 'P'.

# Exercise 11.27
# Write a Python program to separate and print the numbers of a given string.

# Exercise 11.28
# Write a Python program to find all words starting with 'a' or 'e' in a given string.

# Exercise 11.29
# Write a Python program to separate and print the numbers and their positions of a given string.

# Exercise 11.30
# Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.





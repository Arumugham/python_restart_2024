#Exercise 6: File I/O**
#Task: Learn how to read from and write to files.
#Exercise 6.1: Write a program that reads a text file and counts the number of words.

file_path = "sample.txt"
try:
    file = open(file_path,'r')

    for line in file:
        print(line.strip()) # strip removes any leading/trailing whitespaces.

    file.close()
except FileNotFoundError:
    print("File not found. Please check the file path.")

except PermissionError:
    print("Permission denied. You do not have the required permissions to access the file.")


# Exercise 6.2: Counting Words in a File:
# Write a program that reads a text file and counts the number of words in it.


file_path = "sample.txt"
word_count = 0
try:
    file = open(file_path,'r')
    for line in file:
        words = line.strip() 
        word_count += len(words)
    print("Total word count is",word_count)

    file.close()
except FileNotFoundError:
    print("File not found. Please check the file path.")

except PermissionError:
    print("Permission denied. You do not have the required permissions to access the file.")


# Exercise 6.3: Display the word count at the end.
# Copying Files:
# Write a program that copies the contents of one file to another.
# Ensure that the program can handle large files efficiently.

source_file_path ="large_text_file.txt"
destination_file_path = "new_file.txt"
try:
    source_file = open(source_file_path,'r')
    destination_file = open(destination_file_path,'w')
    
    for line in source_file:
        destination_file.write(line)
    
    print("File copied successfully")
    source_file.close()
    destination_file.close()
except FileNotFoundError:
    print("File not found. Please check the file path.")

except PermissionError:
    print("Permission denied. You do not have the required permissions to access the file.")

#Exercise 6.4: CSV File Processing:
# Read a CSV file using the csv module and perform operations like calculating the sum of a column or filtering rows based on a condition.


import csv
#csv file path
csv_file_path = "student_data.csv"
total_sum = 0
filtered_rows = []

try:
    with open(csv_file_path,'r') as file:
        csv_reader = csv.reader(file)
        #skipping the header row
        next(csv_reader)

        for row in csv_reader:
            #row[3] indicate the column
            total_sum += float(row[4])

            if int(row[2])>=25:
                filtered_rows.append(row)
    print(f"Total sum of the colum: {total_sum}")
    print("Filtered row based on condition:")
    for row in filtered_rows:
        print(row)

except FileNotFoundError:
    print("File not found. Please check the file path.")

except PermissionError:
    print("Permission denied. You do not have the required permissions to access the file.")
# Exercise 6.5: JSON File Handling:
# Read a JSON file, extract specific data, modify the data, and write it back to the file.

import json
from datetime import datetime

#json file path
json_file_path = "interview_schedule.json"
today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
try:
    #with statement ensure that the file closes automatically
    with open(json_file_path,'r') as file:
        dataset = json.load(file)
        for data in dataset:
            if data["CandidateID"] == "C00003":
                print("changing candidateID",data["CandidateID"],",interview date from",data["InterviewDate"],"to",today)
                data["InterviewDate"] == today

except FileNotFoundError:
    print("File not found. Please check the file path.")

except PermissionError:
    print("Permission denied. You do not have the required permissions to access the file.")



# Exercise 6.6: File Compression:
# Compress a large text file using modules like gzip or zipfile and then decompress it back to its original form.

import gzip

large_file_path = "large_text_file.txt"
compressed_file_path = "compressed_file.txt.gz"
decompressed_file_path = "decompressed_file.txt"


try:
    # r is read in text mode, rb is read in binary mode
    # For non text files like images, zip it is better to read in binary mode to avoid encoding/decoding issues
    with open(large_file_path,'rb') as f_in:
        with gzip.open(compressed_file_path,'wb') as f_out:
            f_out.writelines(f_in)
    print("File compressed successfully!")

    with gzip.open(compressed_file_path,'rb') as f_in:
        with open(decompressed_file_path,'wb') as f_out:
            f_out.writelines(f_in)

    print("File decompressed successfully!")

except FileNotFoundError:
    print("File not found. Please check the file path.")

except PermissionError:
    print("Permission denied. You do not have the required permissions to access the file.")


# Exercise 6.7: Log File Analysis:
# Analyze a log file to extract specific information such as error messages, timestamps, or user activities.
log_file_path = "log_file.log"

try:
    with open(log_file_path,'r') as file:
        for line in file:
            if "ERROR" in line:
                print("Error message found:",line.strip())
            if "INFO" in line:
                print("User activity found:",line.strip())

except FileNotFoundError:
    print("File not found. Please check the file path.")

except PermissionError:
    print("Permission denied. You do not have the required permissions to access the file.")


# Exercise 6.8: File Encryption:
# Implement a program that encrypts a file using a chosen encryption algorithm and then decrypts it back to its original form.

from cryptography.fernet import Fernet

#Generate a key for encryption
key = Fernet.generate_key()
cipher = Fernet(key)

#path to the file to encrpt

filepath = "sample.txt"
encrypted_file_path = "encrypted_file.txt"

with open(file_path, 'rb') as file:
    data = file.read()
    encrypted_data = cipher.encrypt(data)

with open(encrypted_file_path,'wb') as encrypted_file:
    encrypted_file.write(encrypted_data)

print("File encrypted successfully!")

decrypted_file_path = "decrypted_sample.txt"

with open(encrypted_file_path,'rb') as encrypted_file:
    encrypted_data = encrypted_file.read()
    decrypted_data = cipher.decrypt(encrypted_data)

with open(decrypted_file_path,'wb') as decrypted_file:
    decrypted_file.write(decrypted_data)

print("File encrypted successfully!")

# Exercise 6.9: File Search and Replace:
# Create a program that searches for a specific string in a file and replaces it with another string.

file_path = "sample.txt"
new_file_path ="new_sample.txt"
existing_string = "2"

try:
    with open(file_path,"r") as file:
        file_data = file.read()
        new_file_data = file_data.replace(existing_string,"")

    with open(new_file_path,"w") as file:
        file.write(new_file_data)

    print("Search and replace completed")

except FileNotFoundError:
    print("File not found. Please check the file path.")

except PermissionError:
    print("Permission denied. You do not have the required permissions to access the file.")
 
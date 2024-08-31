#Exercise 10: Working with APIs
#Task: Understand how to make HTTP requests and work with APIs.
#Activity: Write a program that fetches and displays weather data from an API.

import requests

book_bib_key = "ISBN:0201558025"
#Make a get request to the book API
response = requests.get("https://openlibrary.org/api/books?bibkeys=ISBN:0201558025&format=json")

#check if the request was sucessful
if response.status_code == 200:
    data = response.json()
    #print(data)
    info_url = data[book_bib_key]['info_url']
    print("info_url:", info_url)
else:
    print("Failed to retrieve weather data")
    #extract data fabout books from the public API

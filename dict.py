# Python program to demonstrate
# Conversion of JSON data to
# dictionary
 
# importing the module
import json
from difflib import get_close_matches
 
# Opening JSON file
with open('data.json') as json_file:
    data = json.load(json_file)

# data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn =  input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

words = input("Enter a word to define: ")

output = translate(words)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


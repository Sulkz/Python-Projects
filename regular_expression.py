import re

def validate_Email():
    userInput = str(input("Enter your email: "))
    gmail_Valid = re.findall("@gmail.com", userInput)
    yahoo_Valid = re.findall("@yahoo.com", userInput)

    if (gmail_Valid, yahoo_Valid):
        print("match found")
    else:
        print("email not in correct format")

validate_Email()
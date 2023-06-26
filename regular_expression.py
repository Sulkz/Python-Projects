import re

def validate_Email():
    userInput = str(input("Enter your email: "))

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, userInput):
        print("email format correct")
    

    gmail_Valid = re.findall("@gmail.com", userInput)
    yahoo_Valid = re.findall("@yahoo.com", userInput)
    outlook_Valid = re.findall("@outlook.com", userInput)

    if (gmail_Valid):
        print("I detect a gmail account")
    elif (yahoo_Valid):
        print("i detect a yahoo account")
    elif (outlook_Valid):
        print("i detect a Outlook account")
    else:
        print("ermm i dont kniow which u are mate")
    


validate_Email()
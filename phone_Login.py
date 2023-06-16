import time
import random
count  = 0


def login(setence):
    print("Welcome to the beta caller id")
    sentence = str(input("Enter your phone number: "))

    #makes sure number is standard length
    length = len(sentence)


    if length != 13 and length != 11:
        print("Incorrect amount of numbers")
    else:
        print("continue")

    time.sleep(1.75)
    #makes sure number has Uk standard 
    trueOrFalse = "+44" in sentence or "07" in sentence

    randNum = random.randrange(1,100)

    time.sleep(1.75)
    if trueOrFalse:
        print("Welcome here is your qeue number: ", "#",randNum )
        time.sleep(1.3)
    else:
        print("Um idk u could be any country")

login(setence="")


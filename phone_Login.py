import time
import random

count = 0
numbersLog = []

while count < 5:
    def login():
        print("Welcome to the beta caller id")
        sentence = str(input("Enter your phone number: "))

        # makes sure number is standard length
        length = len(sentence)

        if length != 13 and length != 11:
            print("Incorrect amount of numbers")
            exit()
        else:
            print("continue")

        time.sleep(1.75)
        # makes sure number has UK standard
        trueOrFalse = "+44" in sentence or "07" in sentence

        randNum = random.randrange(1, 100)

        time.sleep(1.75)
        if trueOrFalse:
            print("Welcome! Here is your queue number:", "#", randNum)
            time.sleep(1.3)
        else:
            print("Um, I don't know. You could be from any country.")

        return sentence

    sentence = login()
    print(count)

    numbersLog.append(sentence)
    print(numbersLog)

    if count == 3:
        break

    count += 1

import random

def login():
    print("Welcome to the beta caller ID")
    sentence = input("Enter your phone number: ")

    # Make sure number is a standard length
    if len(sentence) not in (11, 13):
        print("Incorrect amount of numbers")
        exit()
    else:
        print("Continue")

    # Check if the number has UK standard
    trueOrFalse = "+44" in sentence or "07" in sentence

    randNum = random.randrange(1, 100)

    if trueOrFalse:
        print("Welcome! Here is your queue number:", "#", randNum)
    else:
        print("Um, I don't know. You could be from any country.")

    return sentence

numbersLog = []
for count in range(5):
    sentence = login()
    print(count)
    numbersLog.append(sentence)

    if count == 3:
        break

print(numbersLog)
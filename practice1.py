import time
import random
count  = 0

print("Welcome to the beta caller id")
sentence = str(input("Enter your phone number: "))

#makes sure number is standard length
length = len(sentence)


if length != 13:
    print("Incorrect amount of numbers")
    count += 1
    if count == 1:
        print("Yourrr out")
        time.sleep(1.5)
        exit()
    else:
        print()
else:
    print("continue")

time.sleep(1.75)
#makes sure number has Uk standard 
trueOrFalse = "+44" in sentence
randNum = random.randrange(1,100)

time.sleep(1.75)
if trueOrFalse == True:
    print("Welcome here is your qeue number: ", randNum )
else:
    print("Um idk u could be any country")

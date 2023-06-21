import random

    

#useful variables min and max values and random number gen
lowBound = 0
highBound = 101
actualNum = random.randrange(1,100)
trueOrfalse = False

while not trueOrfalse:
    guess = input("Guess a number between 1-100: ")
    
    if guess == "":
        print("Empty input! Please enter a number.")
        continue
    
    guess = int(guess)
    
    if guess <= lowBound:
        print("Gonna need to choose something else, mate.")
    elif guess >= highBound:
        print("Gonna need to choose something else, mate.")
    else:
        if guess == actualNum:
            print(":0 You guessed it right! Wahoo!")
            trueOrfalse = True
        elif guess > actualNum:
            print("Bit too big, mate.")
        elif guess < actualNum:
            print("Bro, it's too small now.")
        else:
            print("Um... I don't know what to say.")




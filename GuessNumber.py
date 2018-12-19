import random
number = random.randint(1,9)
guess = input("Try to guess my number:  ")
guess = int(guess)
count = 0
while guess != number and guess != "exit":
    if guess < number:
        count =+1
        guess = input("Two low, try again:  ")
        guess = int(guess)
    elif guess > number:
        count =+1
        guess = input("Too high, try again:  ")
        guess = int(guess)
    else:
        print("You got it! It only took " + count + "tries!")

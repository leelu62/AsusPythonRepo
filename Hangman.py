import random
with open("sowpods.txt", "r") as file:
    words = list(file)
word = str(random.choice(words).split())
print(word)

print("Welcome to Hang Man!")
print(len(word))
print("_ " * len(word))

#letters = []
#for letter in word:
    #if letter not in letters:
        #letters.append(letter)

#print(letters)



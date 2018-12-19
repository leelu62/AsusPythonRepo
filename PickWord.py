import random
with open("sowpods.txt", "r") as file:
    words = list(file)
print(random.choice(words).split())
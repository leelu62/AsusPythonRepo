with open ('nameslist.txt', "r") as nameslist:
    names = {}
    count = 0
    for name in nameslist:
        name = name.strip()
        if name in names:
            names[name] = names[name] + 1
        else:
            names[name] = count
print(names)

max_occurrences = 0
for key, value in names.items():
    if max_occurrences < value:
        max_occurrences = value
        name = key
print(key, ":", max_occurrences) 
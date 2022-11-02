letter = input()
block = 0
counter = False
for x in letter:
    if x == "H" or x == "P":
        if counter:
            break
        counter = True
    elif counter:
        block += 1
print(block)
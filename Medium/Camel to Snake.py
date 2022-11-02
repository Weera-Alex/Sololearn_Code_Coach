capital = False
letter = input()
new_word = letter[0].lower()
for x in letter[1:]:
    if x == "_":
        capital = True
    elif capital:
        capital = False
        new_word += x.upper()
    elif x == x.upper():
        new_word += "_" + x.lower()
    else:
        new_word += x
print(new_word)

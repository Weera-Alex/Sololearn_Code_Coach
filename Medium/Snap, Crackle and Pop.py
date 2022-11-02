num = []
for x in range(6):
    num.append(int(input()))
sounds = ""
for y in num:
    if y % 3 == 0:
        sounds += "Pop "
    elif y % 2 == 0:
        sounds += "Crackle "
    else:
        sounds += "Snap "
print(sounds)

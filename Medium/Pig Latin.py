pig_latin = input()
new_pig = pig_latin.split()
for x in new_pig:
    print(x[1:] + x[0], end="ay ")

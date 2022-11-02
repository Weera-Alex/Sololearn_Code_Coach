letter = input()
num = int(input())
new_letter = ""
counter = 0
for x in letter:
    if counter == num:
        counter = 1
        new_letter += "-" + x
    else:
        new_letter += x
        counter += 1
print(new_letter)
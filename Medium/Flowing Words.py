letters = input()
num = 1
last_letter = letters[0]
checker = False
for x in letters:
    if x != " ":
        new_letter = x
    if x == " ":
        checker = True
        continue
    if checker:
        checker = False
        if last_letter != new_letter:
                print("false")
                num = 0
                break
    if x != " ":
        last_letter = new_letter
if num:
    print("true")

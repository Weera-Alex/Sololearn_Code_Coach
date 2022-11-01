import string
x = input()
for a in x:
    if a in string.ascii_letters:
        print(a, end="")
    if a.isnumeric():
        print(a, end="")
    if a == " ":
        print(" ", end="")

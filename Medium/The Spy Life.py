import string
x = input()[::-1].lower()

for a in x:
    if a in string.ascii_lowercase:
        print(a, end="")
    elif a == " ":
        print(" ")

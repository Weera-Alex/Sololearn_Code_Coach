letter = input()
unique = len(set(letter)) == len(letter)
if not unique:
    print("Deja Vu")
else:
    print("Unique")


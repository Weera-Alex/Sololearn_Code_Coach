text = input()
stored = ""
comp = ""
for x in text:
    if not x.isdigit():
        stored = x
    else:
        comp += stored * int(x)
print(comp)


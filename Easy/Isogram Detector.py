keeper = []
isogram = True
for x in input():
    if x in keeper:
        print("false")
        isogram = False
        break
    else:
        keeper.append(x)
if isogram:
    print("true")
